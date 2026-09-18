"""Validate the P0-8 design registry without reading market data."""

from __future__ import annotations

import json
import hashlib
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "research" / "factor-zoo" / "FACTOR_REGISTRY_V1.json"
CARDS = ROOT / "research" / "factor-zoo" / "FACTOR_CARDS"
EXPECTED_REGISTRY_SHA256 = "8e2aca49d8ab7e0a65e886eb8b8792b716d6259b18600ad014718ad66166837b"

RAW_FIELDS = {
    "trade_date",
    "symbol",
    "open",
    "high",
    "low",
    "close",
    "preclose",
    "volume",
    "amount",
    "turnover",
    "pct_change",
    "trade_status",
    "st_status",
    "suspension_status",
    "price_basis",
    "source_provider",
    "source_endpoint",
    "evidence_type",
    "pit_status",
    "adj_factor",
    "event_ratio",
    "factor_change_event",
    "source",
    "convention",
}

REQUIRED_FIELDS = {
    "factor_id",
    "canonical_name",
    "family",
    "concept",
    "parameterization_group",
    "variant_role",
    "formula_pseudocode",
    "required_raw_fields",
    "derived_inputs",
    "lookback_input_horizon",
    "signal_availability_timing",
    "expected_direction",
    "hypothesis",
    "literature_common_usage_note",
    "expected_turnover",
    "potential_execution_sensitivity",
    "likely_related_redundant_factors",
    "pit_lookahead_risks",
    "data_readiness_status",
    "abstraction",
    "provenance",
    "planned_tests",
    "lifecycle",
    "definition_status",
    "evaluation_stage",
}


def main() -> None:
    registry_bytes = REGISTRY.read_bytes()
    assert hashlib.sha256(registry_bytes).hexdigest() == EXPECTED_REGISTRY_SHA256
    payload = json.loads(registry_bytes)
    factors = payload["factors"]
    assert payload["factor_count"] == len(factors) == 103
    assert payload["atomic_transformed_count"] == sum(f["evaluation_stage"] == "P0_8B" for f in factors) == 99
    assert payload["conditional_prototype_count"] == sum(f["evaluation_stage"] == "P0_8D" for f in factors) == 4
    assert "SEALED_UNACCESSED_UNCONSUMED" in payload["protected_holdout"]

    ids = [f["factor_id"] for f in factors]
    assert len(ids) == len(set(ids))
    concepts_to_groups: dict[str, set[str]] = defaultdict(set)

    for factor in factors:
        missing = REQUIRED_FIELDS - set(factor)
        assert not missing, (factor.get("factor_id"), sorted(missing))
        assert re.fullmatch(r"FZ1_[A-Z0-9]+_[0-9]{3}", factor["factor_id"]), factor["factor_id"]
        assert set(factor["required_raw_fields"]) <= RAW_FIELDS, (factor["factor_id"], set(factor["required_raw_fields"]) - RAW_FIELDS)
        assert not re.search(r"\bt\s*\+\s*[0-9]", factor["formula_pseudocode"]), factor["factor_id"]
        assert factor["definition_status"] == "DRAFT_DESIGN"
        assert factor["lifecycle"] == "DISCOVERED"
        assert factor["data_readiness_status"] in {"LIMITED", "READY_WITH_WARNINGS", "DEFERRED_TO_P0_8D"}
        assert factor["abstraction"] in {"ATOMIC", "TRANSFORMED", "CONDITIONAL"}
        assert factor["planned_tests"]
        concepts_to_groups[factor["concept"]].add(factor["parameterization_group"])

        card = CARDS / f"{factor['factor_id']}.md"
        assert card.is_file(), card
        text = card.read_text(encoding="utf-8")
        assert text.startswith(f"# {factor['factor_id']} —")
        assert factor["formula_pseudocode"] in text

    assert all(len(groups) == 1 for groups in concepts_to_groups.values()), concepts_to_groups
    card_files = sorted(CARDS.glob("FZ1_*.md"))
    assert len(card_files) == 103, len(card_files)
    assert payload["concept_count"] == len(concepts_to_groups) == 89
    assert payload["parameterization_group_count"] == len({f["parameterization_group"] for f in factors}) == 89
    assert payload["family_counts"] == dict(__import__("collections").Counter(f["family"] for f in factors))
    print("FACTOR_REGISTRY_V1_VALIDATION=PASS")
    print("FACTORS=103 ATOMIC_TRANSFORMED=99 CONDITIONAL=4 CONCEPTS=89 PARAMETER_GROUPS=89")


if __name__ == "__main__":
    main()

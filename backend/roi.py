"""
roi.py

ROI computation and aggregation logic for AI ROI Ledger.
"""

from typing import List, Dict, Optional

HUMAN_COST_PER_UNIT = 0.5  # USD per unit (assumption)


def _compute_event_roi(event: Dict, outcome: Optional[Dict]) -> Dict:
    """
    Compute ROI for a single AI event.
    """
    if outcome is None:
        return {
            "roi": None,
            "status": "UNKNOWN"
        }

    ai_cost = float(event.get("estimated_cost_usd", 0))
    measured_value = float(outcome.get("measured_value", 0))

    human_cost = measured_value * HUMAN_COST_PER_UNIT
    value_created = measured_value * HUMAN_COST_PER_UNIT

    roi_value = value_created - (ai_cost + human_cost)

    return {
        "roi": roi_value,
        "status": "POSITIVE" if roi_value > 0 else "NEGATIVE"
    }


def generate_weekly_summary(
    events: List[Dict],
    kpis: List[Dict],
    outcomes: List[Dict]
) -> Dict:
    """
    Generate a weekly-style ROI summary.

    Returns:
    - top_positive: top 3 positive ROI events
    - bottom_negative: bottom 3 negative ROI events
    - unknown: events without outcome data
    """

    outcome_map = {o["event_id"]: o for o in outcomes}
    results = []

    for event in events:
        outcome = outcome_map.get(event["event_id"])
        roi_result = _compute_event_roi(event, outcome)

        results.append({
            "event_id": event["event_id"],
            "use_case": event["use_case"],
            **roi_result
        })

    positive = sorted(
        [r for r in results if r["status"] == "POSITIVE"],
        key=lambda x: x["roi"],
        reverse=True
    )

    negative = sorted(
        [r for r in results if r["status"] == "NEGATIVE"],
        key=lambda x: x["roi"]
    )

    unknown = [r for r in results if r["status"] == "UNKNOWN"]

    return {
        "top_positive": positive[:3],
        "bottom_negative": negative[:3],
        "unknown": unknown
    }

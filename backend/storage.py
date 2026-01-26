"""
CSV-based ledger storage for the AI ROI Ledger.

Design choices:
- CSV for transparency and auditability
- No external database dependency
- Append-only writes for events, KPIs, and outcomes

This is intentional for early-stage ROI tracking systems.
"""

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

AI_EVENTS_FILE = os.path.join(DATA_DIR, "ai_events.csv")
KPI_FILE = os.path.join(DATA_DIR, "kpi_hypotheses.csv")
OUTCOMES_FILE = os.path.join(DATA_DIR, "outcomes.csv")


def _ensure_file(file_path, headers):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(file_path):
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()


def _append_row(file_path, headers, row):
    _ensure_file(file_path, headers)
    with open(file_path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow(row)


def append_ai_event(event: dict):
    headers = [
        "event_id",
        "timestamp",
        "user",
        "team",
        "use_case",
        "model_name",
        "tokens_used",
        "estimated_cost_usd",
        "execution_time_sec",
    ]
    _append_row(AI_EVENTS_FILE, headers, event)


def append_kpi_hypothesis(kpi: dict):
    headers = [
        "event_id",
        "kpi_type",
        "baseline_value",
        "baseline_unit",
        "expected_impact",
    ]
    _append_row(KPI_FILE, headers, kpi)


def append_outcome(outcome: dict):
    headers = [
        "event_id",
        "actual_outcome",
        "measured_value",
        "unit",
        "confidence_level",
        "notes",
    ]
    _append_row(OUTCOMES_FILE, headers, outcome)


def _read_all(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_all_events():
    return _read_all(AI_EVENTS_FILE)


def read_all_kpis():
    return _read_all(KPI_FILE)


def read_all_outcomes():
    return _read_all(OUTCOMES_FILE)

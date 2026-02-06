"""
FastAPI entry point for the AI ROI Ledger backend.
Provides endpoints for logging AI usage, KPIs, outcomes,
and generating ROI-based weekly summaries.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from backend.storage import (
    append_ai_event,
    append_kpi_hypothesis,
    append_outcome,
    read_all_events,
    read_all_kpis,
    read_all_outcomes,
)
from backend.roi import generate_weekly_summary

app = FastAPI(title="AI ROI Ledger")


# ---------- Data Models ----------

class AIEvent(BaseModel):
    event_id: str
    timestamp: str
    user: str
    team: str
    use_case: str
    model_name: str
    tokens_used: int
    estimated_cost_usd: float
    execution_time_sec: int


class KPIHypothesis(BaseModel):
    event_id: str
    kpi_type: str
    baseline_value: float
    baseline_unit: str
    expected_impact: str


class Outcome(BaseModel):
    event_id: str
    actual_outcome: str
    measured_value: float
    unit: str
    confidence_level: float
    notes: Optional[str] = ""


# ---------- Routes ----------

@app.get("/")
def health_check():
    return {"status": "AI ROI Ledger running"}


@app.post("/log_event")
def log_event(event: AIEvent):
    append_ai_event(event.dict())
    return {"message": "AI event logged"}


@app.post("/add_kpi")
def add_kpi(kpi: KPIHypothesis):
    append_kpi_hypothesis(kpi.dict())
    return {"message": "KPI hypothesis added"}


@app.post("/add_outcome")
def add_outcome(outcome: Outcome):
    append_outcome(outcome.dict())
    return {"message": "Outcome recorded"}


@app.get("/weekly_report")
def weekly_report():
    events = read_all_events()
    kpis = read_all_kpis()
    outcomes = read_all_outcomes()

    report = generate_weekly_summary(events, kpis, outcomes)
    return report

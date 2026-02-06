-- AI ROI Ledger Schema
-- Conceptual database design (not production)

-- Stores each AI usage event
CREATE TABLE ai_events (
    event_id TEXT PRIMARY KEY,
    timestamp TEXT,
    user_name TEXT,
    team TEXT,
    use_case TEXT,
    model_name TEXT,
    tokens_used INTEGER,
    estimated_cost_usd REAL,
    execution_time_sec INTEGER
);

-- Stores KPI hypothesis per AI event
CREATE TABLE kpi_hypotheses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT,
    kpi_type TEXT,
    baseline_value REAL,
    baseline_unit TEXT,
    expected_impact TEXT,
    FOREIGN KEY (event_id) REFERENCES ai_events(event_id)
);

-- Stores actual outcome evidence
CREATE TABLE outcomes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT,
    actual_outcome TEXT,
    measured_value REAL,
    unit TEXT,
    confidence_level REAL,
    notes TEXT,
    FOREIGN KEY (event_id) REFERENCES ai_events(event_id)
);

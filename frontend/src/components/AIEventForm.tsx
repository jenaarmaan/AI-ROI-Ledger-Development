import { useState } from "react";

export default function AIEventForm() {
  const [useCase, setUseCase] = useState("");
  const [aiCost, setAiCost] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    const event = {
      event_id: crypto.randomUUID(),
      timestamp: new Date().toISOString(),
      user: "demo_user",
      team: "finance_ai",
      use_case: useCase,
      model_name: "gpt-4-mock",
      tokens_used: 1500,
      estimated_cost_usd: Number(aiCost),
      execution_time_sec: 2
    };

    try {
      const response = await fetch("http://localhost:8000/log_event", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(event),
      });

      if (response.ok) {
        setUseCase("");
        setAiCost("");
        window.location.reload(); // Refresh to update dashboard
      }
    } catch (err) {
      console.error("Failed to log event:", err);
    }
  }

  return (
    <section className="card">
      <h2>Log AI Event</h2>

      <form onSubmit={handleSubmit}>
        <label>Use Case</label>
        <input
          placeholder="Customer support reply"
          value={useCase}
          onChange={(e) => setUseCase(e.target.value)}
          required
        />

        <label>Estimated AI Cost (USD)</label>
        <input
          type="number"
          step="0.01"
          placeholder="0.04"
          value={aiCost}
          onChange={(e) => setAiCost(e.target.value)}
          required
        />

        <button type="submit">Save Event</button>
      </form>
    </section>
  );
}

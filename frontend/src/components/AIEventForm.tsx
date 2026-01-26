import { useState } from "react";

export default function AIEventForm() {
  const [useCase, setUseCase] = useState("");
  const [aiCost, setAiCost] = useState("");

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    const events = JSON.parse(localStorage.getItem("events") || "[]");

    events.push({
      id: crypto.randomUUID(),
      useCase,
      aiCostUsd: Number(aiCost),
    });

    localStorage.setItem("events", JSON.stringify(events));

    setUseCase("");
    setAiCost("");
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

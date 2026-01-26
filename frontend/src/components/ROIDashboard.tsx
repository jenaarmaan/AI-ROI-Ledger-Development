import { useEffect, useState } from "react";
import { calculateROI } from "../lib/roiCalculations";

type Event = {
  id: string;
  useCase: string;
  aiCostUsd: number;
};

export default function ROIDashboard() {
  const [events, setEvents] = useState<Event[]>([]);

  useEffect(() => {
    const stored = JSON.parse(localStorage.getItem("events") || "[]");
    setEvents(stored);
  }, []);

  return (
    <section className="card">
      <h2>ROI Summary</h2>

      {events.length === 0 && (
        <p className="muted">No AI events logged yet.</p>
      )}

      <ul className="list">
        {events.map((e) => {
          const result = calculateROI(e.aiCostUsd);

          return (
            <li key={e.id} className={`row ${result.status.toLowerCase()}`}>
              <span>{e.useCase}</span>
              <span className="status">{result.status}</span>
            </li>
          );
        })}
      </ul>
    </section>
  );
}

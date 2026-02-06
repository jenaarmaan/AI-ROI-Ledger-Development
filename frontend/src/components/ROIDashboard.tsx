import { useEffect, useState } from "react";

type Event = {
  event_id: string;
  use_case: string;
  roi: number | null;
  status: string;
};

export default function ROIDashboard() {
  const [events, setEvents] = useState<Event[]>([]);

  useEffect(() => {
    async function refreshData() {
      try {
        const response = await fetch("http://localhost:8000/weekly_report");
        if (response.ok) {
          const data = await response.json();
          // Flatten all reports into one list for the simple dashboard
          const allEvents = [
            ...(data.top_positive || []),
            ...(data.bottom_negative || []),
            ...(data.unknown || [])
          ];
          setEvents(allEvents);
        }
      } catch (err) {
        console.error("Failed to fetch ROI report:", err);
      }
    }
    refreshData();
  }, []);

  return (
    <section className="card">
      <h2>ROI Summary</h2>

      {events.length === 0 && (
        <p className="muted">No AI events logged yet.</p>
      )}

      <ul className="list">
        {events.map((e) => (
          <li key={e.event_id} className={`row ${e.status.toLowerCase()}`}>
            <span>{e.use_case}</span>
            <span className="status">
              {e.status} {e.roi !== null ? `($${e.roi.toFixed(2)})` : ""}
            </span>
          </li>
        ))}
      </ul>
    </section>
  );
}

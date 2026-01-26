import AIEventForm from "./components/AIEventForm";
import ROIDashboard from "./components/ROIDashboard";
import "./index.css";

export default function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>AI ROI Ledger</h1>
        <p>Measure AI like a financial asset</p>
      </header>

      <main className="grid">
        <AIEventForm />
        <ROIDashboard />
      </main>
    </div>
  );
}

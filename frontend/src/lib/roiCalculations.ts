export type ROIStatus = "POSITIVE" | "NEGATIVE" | "UNKNOWN";

export interface ROIResult {
  roi: number | null;
  status: ROIStatus;
}

const HUMAN_COST_PER_UNIT = 0.5;

export function calculateROI(
  aiCostUsd: number,
  measuredValue?: number
): ROIResult {
  if (measuredValue === undefined) {
    return { roi: null, status: "UNKNOWN" };
  }

  const humanCost = measuredValue * HUMAN_COST_PER_UNIT;
  const valueCreated = measuredValue * HUMAN_COST_PER_UNIT;

  const roi = valueCreated - (aiCostUsd + humanCost);

  return {
    roi,
    status: roi > 0 ? "POSITIVE" : "NEGATIVE",
  };
}

const API_BASE = "http://127.0.0.1:8000/api";

export async function fetchInsights() {
  const res = await fetch(`${API_BASE}/insights/`);
  if (!res.ok) {
    throw new Error("Failed to fetch insights");
  }
  return res.json();
}

const BASE_URL = "http://127.0.0.1:8000/api";

export async function fetchAnalytics() {
  const res = await fetch(`${BASE_URL}/insights/analytics/`);
  if (!res.ok) {
    throw new Error("Failed to fetch analytics");
  }
  return res.json();
}

export async function fetchRecommendations() {
  const res = await fetch("http://127.0.0.1:8000/api/insights/recommendations/");
  if (!res.ok) throw new Error("Failed to fetch recommendations");
  return res.json();
}


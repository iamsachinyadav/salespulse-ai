import React, { useEffect, useState } from "react";
import { fetchAnalytics } from "../services/api";
import RevenueCard from "../components/RevenueCard";
import SentimentChart from "../components/SentimentChart";

export default function Analytics() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchAnalytics()
      .then(setData)
      .catch(err => setError(err.message));
  }, []);

  if (error) return <p>{error}</p>;
  if (!data) return <p>Loading analytics...</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Analytics Overview</h2>

      <RevenueCard revenue={data.revenue} />

      <div style={{ width: 350 }}>
        <SentimentChart sentiments={data.sentiments} />
      </div>
    </div>
  );
}

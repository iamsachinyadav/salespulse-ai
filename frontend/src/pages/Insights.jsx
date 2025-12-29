import React, { useEffect, useState } from "react";
import { fetchInsights } from "../services/api";
import InsightCard from "../components/InsightCard";
import Loader from "../components/Loader";

export default function Insights() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchInsights()
      .then(setData)
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <p>Error: {error}</p>;
  if (!data) return <Loader />;

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Business Insights</h2>

      {data.insights.map((insight, index) => (
        <InsightCard
          key={index}
          message={insight.message}
          type={insight.type}
        />
      ))}
    </div>
  );
}


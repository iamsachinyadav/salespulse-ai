import React, { useEffect, useState } from "react";
import { fetchRecommendations } from "../services/api";

function Recommendations() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchRecommendations().then(setData);
  }, []);

  if (!data) return <p>Loading recommendations...</p>;

  return (
    <div>
      <h2>AI Recommendations</h2>
      <h4>What you should do next</h4>

      <p><strong>{data.title}</strong></p>
      <p>{data.message}</p>

      <p>
        Priority: <strong>{data.priority}</strong> | Confidence:{" "}
        <strong>{data.confidence}%</strong>
      </p>
    </div>
  );
}

export default Recommendations;

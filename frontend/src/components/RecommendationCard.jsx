import React from "react";

export default function RecommendationCard({ rec }) {
  const priorityColor =
    rec.priority === "HIGH" ? "#dc3545" : "#ffc107";

  return (
    <div
      style={{
        borderLeft: `6px solid ${priorityColor}`,
        padding: 16,
        background: "#fff",
        borderRadius: 8,
        marginBottom: 12,
        boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
      }}
    >
      <h3>{rec.title}</h3>
      <p>{rec.action}</p>
      <small>
        Priority: <b>{rec.priority}</b> | Confidence:{" "}
        <b>{Math.round(rec.confidence * 100)}%</b>
      </small>
    </div>
  );
}

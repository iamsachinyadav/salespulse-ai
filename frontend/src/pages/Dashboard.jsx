import React from "react";
import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>SalesPulse AI Dashboard</h1>

      <div style={{ marginTop: "20px" }}>
        <Link to="/insights">👉 View AI Insights</Link>
      </div>
    </div>
  );
}

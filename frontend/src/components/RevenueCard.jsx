import React from "react";

export default function RevenueCard({ amount }) {
  return (
    <div style={{ padding: 20, background: "#eef", borderRadius: 8 }}>
      <h3>Total Revenue</h3>
      <h2>₹ {amount}</h2>
    </div>
  );
}

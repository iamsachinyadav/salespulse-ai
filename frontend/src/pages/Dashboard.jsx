import React, { useEffect, useState } from "react";
import api from "../api/client";

const Dashboard = () => {
  const [health, setHealth] = useState(null);
  const [sales, setSales] = useState([]);

  useEffect(() => {
    api.get("health/").then(res => setHealth(res.data));
    api.get("sales/").then(res => setSales(res.data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>SalesPulse AI Dashboard</h1>

      {health && (
        <p style={{ color: "green" }}>
          Backend Status: {health.status}
        </p>
      )}

      <h2>Sales</h2>
      <ul>
        {sales.map(sale => (
          <li key={sale.id}>
            {sale.product_name} — {sale.quantity} × ₹{sale.price}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;

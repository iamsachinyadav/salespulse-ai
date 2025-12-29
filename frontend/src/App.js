import React from "react";
import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Insights from "./pages/Insights";
import Analytics from "./pages/Analytics";
import Recommendations from "./pages/Recommendations";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/insights" element={<Insights />} />
      <Route path="/analytics" element={<Analytics />} />
      <Route path="/recommendations" element={<Recommendations />} />
    </Routes>
  );
}

export default App;

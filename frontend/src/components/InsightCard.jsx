// import React from "react";

// const typeStyles = {
//   success: "bg-green-100 border-green-500 text-green-800",
//   alert: "bg-red-100 border-red-500 text-red-800",
//   opportunity: "bg-yellow-100 border-yellow-500 text-yellow-800",
//   info: "bg-blue-100 border-blue-500 text-blue-800",
// };

// const InsightCard = ({ type, message }) => {
//   return (
//     <div className={`border-l-4 p-4 rounded shadow ${typeStyles[type] || ""}`}>
//       <h3 className="font-bold capitalize">{type}</h3>
//       <p className="mt-1">{message}</p>
//     </div>
//   );
// };

// export default InsightCard;

import React from "react";

export default function InsightCard({ message, type }) {
  const color =
    type === "success"
      ? "#d4edda"
      : type === "warning"
      ? "#fff3cd"
      : "#f8d7da";

  return (
    <div
      style={{
        background: color,
        padding: "16px",
        borderRadius: "8px",
        marginBottom: "12px",
      }}
    >
      <strong>AI Insight:</strong>
      <p>{message}</p>
    </div>
  );
}

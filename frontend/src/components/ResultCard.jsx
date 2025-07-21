// frontend/src/components/ResultCard.jsx

import React from "react";

function ResultCard({ salary }) {
  if (!salary) return null;

  return (
    <div style={cardStyle}>
      <h3 style={{ margin: 0, fontSize: "1.2rem", color: "#444" }}>
        Predicted Salary
      </h3>
      <p style={{ fontSize: "1.8rem", fontWeight: "bold", color: "#2b9348", marginTop: "10px" }}>
        ₹ {salary}
      </p>
    </div>
  );
}

const cardStyle = {
  border: "1px solid #ddd",
  borderRadius: "10px",
  padding: "20px",
  marginTop: "20px",
  boxShadow: "0 4px 6px rgba(0,0,0,0.1)",
  background: "#f9f9f9",
  textAlign: "center"
};

export default ResultCard;

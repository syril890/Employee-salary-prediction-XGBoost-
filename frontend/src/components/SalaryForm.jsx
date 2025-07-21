// frontend/components/SalaryForm.jsx

import React, { useState } from "react";

function SalaryForm() {
  const [formData, setFormData] = useState({
    education_level: "",
    job_role: "",
    location: "",
    years_of_experience: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setPrediction(null);

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          education_level: Number(formData.education_level),
          job_role: Number(formData.job_role),
          location: Number(formData.location),
          years_of_experience: Number(formData.years_of_experience),
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setPrediction(data.predicted_salary.toFixed(2));
      } else {
        setError(data.error || "Something went wrong.");
      }
    } catch (err) {
      setError("Failed to connect to server.");
    }
  };

  return (
    <div style={{ maxWidth: "500px", margin: "auto" }}>
      <h2>Employee Salary Prediction</h2>
      <form onSubmit={handleSubmit}>
        <label>Education Level:</label>
        <input
          type="number"
          name="education_level"
          value={formData.education_level}
          onChange={handleChange}
          required
        />

        <label>Job Role:</label>
        <input
          type="number"
          name="job_role"
          value={formData.job_role}
          onChange={handleChange}
          required
        />

        <label>Location:</label>
        <input
          type="number"
          name="location"
          value={formData.location}
          onChange={handleChange}
          required
        />

        <label>Years of Experience:</label>

import React, { useState } from "react";

const MealForm = ({ setResults }) => {
  const [query, setQuery] = useState("");
  const [preferredIngredients, setPreferredIngredients] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:5000/recommend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query,
          preferred_ingredients: preferredIngredients
            .split(",")
            .map((s) => s.trim())
            .filter((s) => s),
          tags: [],
          max_budget: null,
          max_time: null,
        }),
      });

      const data = await response.json();
      console.log("📦 Received from backend:", data); // Debug log
      setResults(data);
    } catch (error) {
      console.error("⚠️ Error fetching recommendations:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-xl shadow-md space-y-4">
      <div>
        <label className="block font-semibold text-gray-700 mb-1">
          What do you feel like eating?
        </label>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g. chicken, pasta, curry"
          className="w-full border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-500"
        />
      </div>

      <div>
        <label className="block font-semibold text-gray-700 mb-1">
          Preferred Ingredients
        </label>
        <input
          type="text"
          value={preferredIngredients}
          onChange={(e) => setPreferredIngredients(e.target.value)}
          placeholder="e.g. rice, tomato, cheese"
          className="w-full border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-500"
        />
      </div>

      <button
        type="submit"
        className="w-full bg-green-600 text-white font-semibold py-2 px-4 rounded hover:bg-green-700 transition"
      >
        Get Recommendations
      </button>
    </form>
  );
};

export default MealForm;

import React, { useState } from "react";

const MealForm = ({ setResults }) => {
  const [query, setQuery] = useState("");
  const [preferredIngredients, setPreferredIngredients] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

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
      console.log("📦 Received from backend:", data);
      setResults(data);
    } catch (err) {
      console.error("⚠️ Error during fetch:", err);
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white p-6 rounded-xl shadow-md space-y-4"
    >
      <div>
        <label className="block font-semibold text-gray-700 mb-1">
          Describe what you feel like eating
        </label>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g. something creamy with garlic and chicken"
          className="w-full border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-500"
        />
      </div>

      <div>
        <label className="block font-semibold text-gray-700 mb-1">
          (Optional) Must-have ingredients
        </label>
        <input
          type="text"
          value={preferredIngredients}
          onChange={(e) => setPreferredIngredients(e.target.value)}
          placeholder="e.g. rice, tomato, avocado"
          className="w-full border border-gray-300 rounded p-2 focus:outline-none focus:ring-2 focus:ring-green-500"
        />
      </div>

      <button
        type="submit"
        className="w-full bg-green-600 text-white font-semibold py-2 px-4 rounded hover:bg-green-700 transition"
        disabled={loading}
      >
        {loading ? "Searching..." : "Get Recommendations"}
      </button>

      {error && <p className="text-red-500 text-sm">{error}</p>}
    </form>
  );
};

export default MealForm;

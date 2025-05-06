import React, { useState } from "react";
import MealForm from "./components/MealForm";
import MealGrid from "./components/MealGrid";

export default function App() {
  const [results, setResults] = useState([]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-white to-blue-50 text-gray-800 font-sans">
      <header className="py-8 text-center shadow-md bg-white">
        <h1 className="text-4xl font-extrabold text-green-700">
          🥗 AI Meal Planner
        </h1>
        <p className="text-sm mt-2 text-gray-500">
          Get smart recipe recommendations based on your cravings.
        </p>
      </header>

      <main className="max-w-4xl mx-auto px-6 py-10">
        <MealForm setResults={setResults} />

        {results.length > 0 && (
          <section className="mt-12">
            <h2 className="text-2xl font-semibold mb-4 text-gray-700">
              Recommended Meals
            </h2>
            <MealGrid meals={results} />
          </section>
        )}
      </main>
    </div>
  );
}

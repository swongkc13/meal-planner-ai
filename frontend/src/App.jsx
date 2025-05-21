import React, { useState } from "react";
import MealForm from "./components/MealForm";
import MealGrid from "./components/MealGrid";

export default function App() {
  const [results, setResults] = useState([]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-white to-blue-50 text-gray-800 font-sans">
      {/* Navbar */}
      <nav className="bg-white shadow-md px-6 py-4 flex justify-between items-center">
        <div className="text-xl font-bold text-green-700">🍽️ MealMate</div>
        <ul className="flex space-x-6 text-sm text-gray-600 font-medium">
          <li className="hover:text-green-600 cursor-pointer">Home</li>
          <li className="hover:text-green-600 cursor-pointer">About</li>
          <li className="hover:text-green-600 cursor-pointer">Contact</li>
        </ul>
      </nav>

      {/* Hero Section */}
      <section className="text-center py-16 px-4 bg-gradient-to-r from-green-100 via-white to-blue-100">
        <h1 className="text-4xl sm:text-5xl font-extrabold text-gray-800 leading-tight mb-4">
          Wake Up Early, <br className="hidden sm:inline" /> Eat Fresh & Healthy
        </h1>
        <p className="max-w-xl mx-auto text-gray-600 text-lg">
          Get personalized, nutritious meal ideas instantly—powered by AI and your favorite ingredients.
        </p>
      </section>

      {/* Form + Results */}
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

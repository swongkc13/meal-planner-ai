export default function MealResults({ meals }) {
    if (!meals.length) return <p className="mt-4 text-gray-500">No results yet.</p>;
  
    return (
      <div className="grid gap-4 mt-4">
        {meals.map((meal, i) => (
          <div key={i} className="border p-4 rounded bg-white shadow">
            <h2 className="text-xl font-bold">{meal.name}</h2>
            <p>{meal.description}</p>
            <p className="text-sm text-gray-600">Prep Time: {meal.prep_time} min • Budget: €{meal.budget}</p>
            <p className="text-sm text-green-700 mt-1">Tags: {meal.tags.join(", ")}</p>
            <p className="text-sm text-gray-700">Ingredients: {meal.ingredients.join(", ")}</p>
          </div>
        ))}
      </div>
    );
  }
  
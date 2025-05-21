export default function MealGrid({ meals }) {
  console.log("🧪 Rendering meals:", meals);

  if (!meals || meals.length === 0) {
    return <p className="text-center text-gray-500 mt-10">No meals found. Try a different search.</p>;
  }

  return (
    <div className="max-w-6xl mx-auto px-6 py-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
      {meals.map((meal, i) => (
        <div key={i} className="bg-white rounded-2xl shadow-lg overflow-hidden flex flex-col">
          {meal.thumbnail && (
            <img
              src={meal.thumbnail}
              alt={meal.name}
              className="w-full h-48 object-cover"
            />
          )}

          <div className="p-6 flex flex-col flex-grow">
            <h3 className="text-xl font-bold text-green-700 mb-2">{meal.name}</h3>

            <p className="text-gray-600 flex-grow">
              {meal.description ? meal.description.slice(0, 120) + "..." : "No description available."}
            </p>

            <p className="text-sm text-gray-500 mt-2">
              🕒 {meal.prep_time ?? "?"} min • 💸 €{meal.budget ?? "?"}
            </p>

            {meal.tags?.length > 0 && (
              <p className="text-sm mt-1 text-yellow-600">Tags: {meal.tags.join(", ")}</p>
            )}

            {meal.ingredients?.length > 0 && (
              <p className="text-sm text-gray-700 mt-1">Ingredients: {meal.ingredients.join(", ")}</p>
            )}
          </div>
        </div>
      ))}
    </div>
  );
}

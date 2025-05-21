export default function MealCard({ meal, active }) {
  return (
    <div
      className={`bg-white rounded-2xl p-6 text-center w-64 shadow-xl transition-all duration-300 
        ${active ? 'border-4 border-yellow-400 scale-105' : 'hover:scale-105'}
      `}
    >
      <img
        src={meal.thumbnail || meal.image || "/default-meal.jpg"}
        alt={meal.name}
        className="w-20 h-20 object-cover rounded-full mx-auto mb-4 shadow-md"
      />

      <h3 className="text-lg font-bold text-gray-800">{meal.name}</h3>
      <p className="text-gray-500 text-sm mt-1">{meal.category} • {meal.area}</p>

      <p className="text-gray-500 text-xs mt-2">{meal.description}</p>

      <div className="flex justify-center gap-3 mt-4 text-gray-400 text-xs">
        <span>{meal.calories || 60} cal</span>
        <span>•</span>
        <span>{meal.servings || 4} persons</span>
      </div>

      {meal.ingredients?.length > 0 && (
        <div className="mt-4 text-left text-xs text-gray-600">
          <strong>Ingredients:</strong>
          <ul className="list-disc list-inside mt-1">
            {meal.ingredients.slice(0, 5).map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        </div>
      )}

      {meal.youtube && (
        <a
          href={meal.youtube}
          target="_blank"
          rel="noopener noreferrer"
          className="block mt-3 text-blue-600 text-sm hover:underline"
        >
          ▶ Watch on YouTube
        </a>
      )}
    </div>
  );
}

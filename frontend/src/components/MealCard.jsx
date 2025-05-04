export default function MealCard({ meal, active }) {
  return (
    <div
      className={`bg-white rounded-2xl p-6 text-center w-64 shadow-xl transition-all duration-300 
        ${active ? 'border-4 border-yellow-400 scale-105' : 'hover:scale-105'}
      `}
    >
      <img
        src={meal.image || "/default-meal.jpg"}
        alt={meal.name}
        className="w-20 h-20 object-cover rounded-full mx-auto mb-4 shadow-md"
      />

      <h3 className="text-lg font-bold text-gray-800">{meal.name}</h3>
      <p className="text-gray-500 text-sm mt-1">{meal.description}</p>

      <div className="flex justify-center gap-3 mt-4 text-gray-400 text-xs">
        <span>{meal.calories || 60} cal</span>
        <span>•</span>
        <span>{meal.servings || 4} persons</span>
      </div>

      <div className="mt-4 flex justify-between items-center px-4">
        <span className="text-md font-semibold text-gray-700">€{meal.cost.toFixed(2)}</span>
        <button className="bg-yellow-400 text-white rounded-full w-8 h-8 font-bold hover:bg-yellow-500">
          +
        </button>
      </div>
    </div>
  );
}

import MealCard from './MealCard';

export default function MealGrid({ meals }) {
  return (
    <section className="w-full max-w-7xl mx-auto px-4 py-12">
      {meals.length > 0 ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 justify-items-center">
          {meals.map((meal, i) => (
            <MealCard key={i} meal={meal} active={i === 1} />
          ))}
        </div>
      ) : (
        <p className="text-center text-gray-600 text-lg">
          No meals found. Try searching something tasty!
        </p>
      )}
    </section>
  );
}

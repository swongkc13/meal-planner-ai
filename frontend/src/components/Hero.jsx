export default function Hero({ query, setQuery, onSearch }) {
  return (
    <section className="flex flex-col-reverse md:flex-row items-center justify-between gap-10 px-6 py-12 bg-white rounded-3xl shadow-xl max-w-7xl mx-auto mt-8">
      {/* Text Section */}
      <div className="flex-1 text-center md:text-left">
        <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800 leading-tight">
          It’s not just <span className="text-red-500">Food</span>, It’s an <br className="hidden md:block" />
          <span className="text-yellow-500">Experience.</span>
        </h1>
        <p className="text-gray-600 mt-4 text-md md:text-lg">
          Discover personalized meals with our AI-powered planner
        </p>

        <div className="mt-6 flex flex-col sm:flex-row items-center gap-4 max-w-md">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="e.g. something quick and spicy"
            className="flex-1 px-4 py-2 rounded-xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-yellow-400 transition"
          />
          <button
            onClick={onSearch}
            className="bg-green-500 hover:bg-green-600 text-white font-semibold px-5 py-2 rounded-xl transition"
          >
            Find Meals
          </button>
        </div>
      </div>

      {/* Image Section */}
      <div className="flex-1 flex justify-center">
        <img
          src="https://source.unsplash.com/400x300/?healthy-food"
          alt="Meal Preview"
          className="rounded-2xl shadow-lg object-cover w-full max-w-sm"
        />
      </div>
    </section>
  );
}

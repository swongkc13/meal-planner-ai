export default function Navbar() {
  return (
    <nav className="flex justify-between items-center px-8 py-4 bg-white rounded-b-3xl shadow-md">
      <div className="flex items-center gap-4">
        <img
          src="/assets/flag-usa.png"
          alt="USA"
          className="w-6 h-6 object-cover rounded-full"
        />
        <span className="text-gray-600 text-sm">Login as Sham</span>
      </div>

      <h1 className="text-3xl font-extrabold tracking-wide text-gray-800">
        <span className="text-yellow-500">•</span> Bell Meals
      </h1>

      <div className="relative">
        <button className="bg-black text-white px-5 py-2 rounded-lg font-semibold hover:bg-gray-800 transition">
          My Cart
        </button>
        <span className="absolute -top-2 -right-2 bg-yellow-400 text-xs text-black font-bold rounded-full px-2 shadow-md">
          3
        </span>
      </div>
    </nav>
  )
}

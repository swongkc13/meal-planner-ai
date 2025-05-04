import { useState } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import MealGrid from './components/MealGrid';

function App() {
  const [query, setQuery] = useState('');
  const [meals, setMeals] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const getMeals = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await fetch('http://localhost:5000/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });

      if (!res.ok) throw new Error('Failed to fetch');

      const data = await res.json();
      setMeals(data);
    } catch (err) {
      setError('Something went wrong. Please try again!');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-[#fef7ee] min-h-screen font-sans text-gray-800">
      <Navbar />
      <Hero query={query} setQuery={setQuery} onSearch={getMeals} />
      
      <section className="max-w-7xl mx-auto px-4 text-center">
        {loading && (
          <p className="text-yellow-500 font-medium text-lg animate-pulse my-4">
            Searching for tasty meals...
          </p>
        )}
        {error && (
          <p className="text-red-500 font-medium text-lg my-4">{error}</p>
        )}
      </section>

      <MealGrid meals={meals} />
    </div>
  );
}

export default App;

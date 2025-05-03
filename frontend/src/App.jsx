import { useState } from 'react';

function App() {
  const [query, setQuery] = useState('');
  const [meals, setMeals] = useState([]);

  const getMeals = async () => {
    const res = await fetch('http://localhost:5000/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query }),
    });
    const data = await res.json();
    setMeals(data);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Meal Planner AI 🍽️</h1>
      <input
        type="text"
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="e.g. something quick and spicy"
      />
      <button onClick={getMeals}>Get Meals</button>

      <ul>
        {meals.map((meal, i) => (
          <li key={i}>
            <strong>{meal.name}</strong> - {meal.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

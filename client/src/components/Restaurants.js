import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Restaurants() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch("/restaurants")
      .then((r) => r.json())
      .then(setRestaurants);
  }, []);

  return (
    <section>
      <h1>All Restaurants</h1>
      <button><Link to={`/`}>HOME</Link></button>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <p><Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}</Link></p>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Restaurants;

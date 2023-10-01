import { useEffect, useState } from "react";

function RestaurantPizzas() {
    const [restaurants, setRestaurants] = useState([]);
    const [pizzas, setPizzas] = useState([]);
    const [restaurantId, setRestaurantId] = useState("");
    const [pizzaId, setPizzaId] = useState("");

    useEffect(() => {
        fetch("/restaurants")
          .then((r) => r.json())
          .then(setRestaurants);
      }, []);
    
      useEffect(() => {
        fetch("/pizzas")
          .then((r) => r.json())
          .then(setPizzas);
      }, []);

      function handleSubmit(e) {
        e.preventDefault();
        const formData = {
          restaurany_id: restaurantId,
          pizza_id: pizzaId,
        };
        fetch("/restaurant_pizzas", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        })
        }
        return (
            <form onSubmit={handleSubmit}>
              <label htmlFor="pizza_id">Pizza:</label>
              <select
                id="pizza_id"
                name="pizza_id"
                value={pizzaId}
                onChange={(e) => setPizzaId(e.target.value)}
              >
                <option value="">Select a pizza</option>
                {pizzas.map((pizza) => (
                  <option key={pizza.id} value={pizza.id}>
                    {pizza.name}
                  </option>
                ))}
              </select>
              <label htmlFor="restaurant_id">Restaurant:</label>
              <select
                id="restaurant_id"
                name="restaurant_id"
                value={restaurantId}
                onChange={(e) => setRestaurantId(e.target.value)}
              >
                <option value="">Select a restaurant</option>
                {restaurants.map((restaurant) => (
                  <option key={restaurant.id} value={restaurant.id}>
                    {restaurant.name}
                  </option>
                ))}
              </select>
              
              <button type="submit">Add Restaurant Pizza</button>
            </form>
          );

}

export default RestaurantPizzas;
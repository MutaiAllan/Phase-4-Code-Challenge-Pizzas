import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
// import { useHistory } from "react-router-dom";

function Restaurant() {
  const [{ data: restaurant, error, status }, setRestaurant] = useState({
    data: null,
    error: null,
    status: "pending",
  });
  const { id } = useParams();

  useEffect(() => {
    fetch(`/restaurants/${id}`).then((r) => {
      if (r.ok) {
        r.json().then((restaurant) =>
          setRestaurant({ data: restaurant, error: null, status: "resolved" })
        );
      } else {
        r.json().then((err) =>
          setRestaurant({ data: null, error: err.error, status: "rejected" })
        );
      }
    });
  }, [id]);

  if (status === "pending") return <h1>Loading...</h1>;
  if (status === "rejected") return <h1>Error: {error.error}</h1>;

  function handleDelete(e) {
    e.preventDefault();
    fetch(`/restaurants/${restaurant.id}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    }).then((r) => {
        //const history = useHistory();
        //history.push("/restaurants");
    })
  }

  return (
    <section>
      <h2>Restaurant Name: {restaurant.name}</h2>
      <h2>Restaurant Address: {restaurant.address}</h2>

      <h3>Restaurant Pizzas: </h3>
      <ul>
        {restaurant.pizzas.map((pizza) => (
          <li key={pizza.id}>
            <Link to={`/pizzas/${pizza.id}`}>{pizza.name}</Link>
          </li>
        ))}
      </ul>
      <button onClick={handleDelete}>DELETE</button>

    </section>
  );
}

export default Restaurant;

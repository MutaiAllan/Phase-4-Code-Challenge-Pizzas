import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Pizzas() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    fetch("/pizzas")
      .then((r) => r.json())
      .then(setPizzas);
  }, []);

  return (
    <section>
      <h1>All Pizzas</h1>
      <button><Link to={`/`}>HOME</Link></button>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            <p>Name: {pizza.name} </p>
            <p>Ingredients: {pizza.ingredients} </p>
            <br></br>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Pizzas;

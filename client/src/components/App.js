import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Home";
import Restaurants from "./Restaurants";
import Restaurant from "./Restaurant";
import Pizzas from "./Pizzas";
import RestaurantPizzas from "./RestaurantPizzas";

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/restaurants" element={<Restaurants />} />
          <Route path="/restaurants/:id" element={<Restaurant />} />
          <Route path="/pizzas" element={<Pizzas />} />
          <Route path="/restaurant_pizzas" element={<RestaurantPizzas />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

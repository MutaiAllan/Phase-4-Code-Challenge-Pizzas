import { Link } from "react-router-dom";

function Home() {
    return (
        <div>
            <h1>
                <Link to="/restaurants">RESTAURANTS</Link>
                <br></br>
                <Link to="/pizzas">PIZZAS</Link>
                <br></br>
                <Link to="/restaurant_pizzas">New Restaurant Pizzas</Link>
            </h1>
        </div>
    )
}
export default Home;
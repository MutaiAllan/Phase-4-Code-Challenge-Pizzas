from flask import Flask, make_response, jsonify, request, redirect, url_for
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to Restaurant Pizzas'

@app.route('/restaurants')
def restaurants():
    restaurants_list = []
    restaurants = Restaurant.query.all()
    for restaurant in restaurants:
        restaurant_dict = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
        restaurants_list.append(restaurant_dict)
    response_body = restaurants_list
    response = make_response(jsonify(response_body), 200)
    return response

@app.route('/restaurants/<int:id>', methods = ["GET", "DELETE"])
def retaurant_id(id):
    restaurant = Restaurant.query.filter_by(id=id).first()
    restaurant_pizzas = RestaurantPizza.query.filter_by(restaurant_id=id).all()
    if restaurant:
        if request.method == "GET":
            pizza_ids = []
            pizzas_list = []
            for restaurant_pizza in restaurant_pizzas:
                pizza_ids.append(restaurant_pizza.restaurant_id)
            for pizza_id in pizza_ids:
                pizza = Pizza.query.filter_by(id=pizza_id).first()
                pizza_dict = {
                    "id": pizza.id,
                    "name": pizza.name,
                    "ingredients": pizza.ingredients
                }
                pizzas_list.append(pizza_dict)
            pizzas = Pizza.query.filter_by()
            response_body = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": pizzas_list
            }
            response = make_response(jsonify(response_body), 200)
        elif request.method == "DELETE":
            for restaurant_pizza in restaurant_pizzas:
                db.session.delete(restaurant_pizza)
            db.session.delete(restaurant)
            db.session.commit()
            response = make_response('', 200)
    else:
        response_body = {"error": "Restaurant not found"}
        response = make_response(jsonify(response_body), 200)

    return response

@app.route('/pizzas')
def pizzas():
    pizzas_list = []
    pizzas = Pizza.query.all()
    for pizza in pizzas:
        pizza_dict = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        pizzas_list.append(pizza_dict)
    response = make_response(jsonify(pizzas_list), 200)
    return response

@app.route('/restaurant_pizzas', methods = ["POST"])
def restaurant_pizzas():
    if request.method == "POST":
        json_data = request.json
        pizza_id = json_data.get("pizza_id")
        restaurant_id = json_data.get("restaurant_id")

        pizza = Pizza.query.filter_by(id=pizza_id).first()
        if not pizza:
            error = {"error":  "Pizza not found"}
            response = make_response(jsonify(error), 404)
            return response
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
        if not restaurant:
            error = {"error":  "Restaurant not found"}
            response = make_response(jsonify(error), 404)
            return response
        
        new_restaurant_pizza = RestaurantPizza(
            price = json_data.get("price"),
            pizza_id = pizza_id,
            restaurant_id = restaurant_id
        )
        db.session.add(new_restaurant_pizza)
        try:
            db.session.commit()
        
            pizza_dict = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            response = make_response(jsonify(pizza_dict), 200)
        except Exception as e:
            db.session.rollback()
            error = {"errors": ["validation errors"]}
            response = make_response(jsonify(error), 400)

        return response


if __name__ == '__main__':
    app.run(port=5555)
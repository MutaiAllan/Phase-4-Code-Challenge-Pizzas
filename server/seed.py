from models import db
from app import app
from models import Restaurant, Pizza, RestaurantPizza


with app.app_context():

    restaurant1 = Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201")
    restaurant2 = Restaurant(name="PizzArte", address="69 W 55th St, New York, NY 10019")


    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")


    restaurant_pizza1 = RestaurantPizza(price=15, restaurant=restaurant1, pizza=pizza1)
    restaurant_pizza2 = RestaurantPizza(price=18, restaurant=restaurant1, pizza=pizza2)
    restaurant_pizza3 = RestaurantPizza(price=16, restaurant=restaurant2, pizza=pizza1)


    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2, restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])


    db.session.commit()

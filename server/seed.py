from models import db
from app import app
from models import Restaurant, Pizza, RestaurantPizza


with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    restaurant1 = Restaurant(name="Stellato", address="01100, Nairobi")
    restaurant2 = Restaurant(name="Sottocasa NYC", address="Brooklyn, NY 11201")
    restaurant3 = Restaurant(name="PizzArte", address="New York, NY 10019")
    restaurant4 = Restaurant(name="FFG", address="298 Atlantic Ave")



    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    pizza3 = Pizza(name="Vegetarian Pizza", ingredients="Dough, Mozzarella cheese, Bell peppers, Onions, Black olives, Mushrooms,Spinach")
    pizza4 = Pizza(name="Quattro Formaggi", ingredients="Tomato sauce, Mozzarella cheese, Parmesan cheese, Gorgonzola cheese, Ricotta cheese")

    restaurant_pizza1 = RestaurantPizza(price=15, restaurant=restaurant1, pizza=pizza4)
    restaurant_pizza2 = RestaurantPizza(price=18, restaurant=restaurant1, pizza=pizza2)
    restaurant_pizza3 = RestaurantPizza(price=12, restaurant=restaurant2, pizza=pizza1)
    restaurant_pizza4 = RestaurantPizza(price=10, restaurant=restaurant4, pizza=pizza3)
    restaurant_pizza5 = RestaurantPizza(price=19, restaurant=restaurant2, pizza=pizza3)
    restaurant_pizza6 = RestaurantPizza(price=11, restaurant=restaurant3, pizza=pizza1)
    restaurant_pizza7 = RestaurantPizza(price=10, restaurant=restaurant4, pizza=pizza2)
    restaurant_pizza8 = RestaurantPizza(price=16, restaurant=restaurant2, pizza=pizza1)


    db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, pizza1, pizza2, pizza3, pizza4, restaurant_pizza1, restaurant_pizza2, restaurant_pizza3,  restaurant_pizza4, restaurant_pizza5, restaurant_pizza6, restaurant_pizza7, restaurant_pizza8])

    db.session.commit()

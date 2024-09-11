from coffee import Coffee
from order import Order

class Customer:
    def __init__(self, name):

        # Initializes a Customer instance with a name.
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        
        self._name = name
        self._orders = []

    @property
    def name(self):

        return self._name # Returns customer's name

    @name.setter
    def name(self, new_name):

        # Set the customer's name.
        # Ensures that the name is a string, between 1 and 15 characters long, and doesn't contain any special characters.
        # Raises a ValueError if the name doesn't meet these criteria.

        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        if len(new_name) < 1 or len(new_name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = new_name


    def orders(self):

        # Returns a list of orders for the customer.
        return self._orders

    def coffees(self):

        # Returns a list of all coffees the customer has ordered.
        
        return list(set(order.coffee for order in self._orders))
    
    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee) or not isinstance(price, (float, int)):
            raise ValueError("Invalid coffee or price.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        
        # Creates a new Order instance for the customer and coffee, and adds it to the customer's orders list.
        order = Order(self, coffee, price)
        self._orders.append(order)

        return order
    
    def __repr__(self) -> str:
        return f"Customer(name='{self.name}')"
        
    
    # Create instances of Customer and Coffee
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")
coffee3= Coffee("cappuccino")

customer1 = Customer("Alice")
customer2 = Customer("Bob")
customer3 = Customer("Charlie")

# Create orders
order1 = customer1.create_order(coffee1, 5.0)
order2 = customer1.create_order(coffee2, 4.5)
order3 = customer2.create_order(coffee1, 3.0)
order4 = customer3.create_order(coffee3, 2.5)
order5 = customer2.create_order(coffee3, 2.0)

# Access orders
print(customer1.orders())  
print(customer2.orders())  
print(customer3.orders())

print(coffee1.num_orders())  # Output: 2
print(coffee2.num_orders())  # Output: 1
print(coffee3.num_orders())  # Output: 2

print(customer1.coffees()) 
print(customer2.coffees()) 
print(customer3.coffees())

print(coffee1.average_price())  # Output: 4.0
print(coffee2.average_price())  # Output: 4.5
print(coffee3.average_price())  # Output: 2.25

print([c.name for c in customer1.coffees()])  # Output: ['Espresso', 'Latte']
print([c.name for c in customer2.coffees()])  # Output: ['Espresso', 'cappuccino']
print([c.name for c in customer3.coffees()])  # Output: ['cappuccino']


print(coffee1.customers())  # Output: [Customer(name='Bob'), Customer(name='Alice')]
print(coffee2.customers())  # Output: [Customer(name='Alice')]
print(coffee3.customers())  # Output: [Customer(name='Bob'), Customer(name='Charlie')]

    

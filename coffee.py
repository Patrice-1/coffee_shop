from order import Order

class Coffee:
    def __init__(self, name):

        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string of at least 3 characters.")
    
        #Initializes a Coffee instance with a name.
        self._name = name
        self._orders = []

    @property
    def name(self):
    
        return self._name # Returns the coffee's name.

    @property
    def orders(self):

        return self._orders #Returns a list of all orders for this coffee.

    def customers(self):

        # Returns a list of customers who have ordered this coffee.
        return list(set(order.customer for order in self.orders))

    def num_orders(self):

        return len(self._orders) # Returns the number of times this coffee has been ordered.

    def average_price(self):

        # Returns the average price for this coffee based on its orders.
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)
    
    def add_order(self, order):
        if not isinstance(order, Order):
            raise ValueError("Must be an instance of Order.")
        self._orders.append(order)


    def __repr__(self) -> str:
        return f"Coffee(name={self._name})"




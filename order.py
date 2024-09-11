class Order:
    def __init__(self, customer, coffee, price):

        if not isinstance(price, (float, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        
        # Initializes an Order instance with a customer, coffee, and price.
        
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        coffee.add_order(self)

    @property
    def customer(self):
        
        return self._customer # Returns the customer object for this order.

    @property
    def coffee(self):

        return self._coffee # Returns the coffee object for this order.

    @property
    def price(self):
        
        return self._price # Returns the price for this order.

    def __repr__(self):
        return f"Order(customer={self._customer.name}, coffee={self._coffee.name}, price={self._price})"
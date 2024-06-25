class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        if isinstance(other, Order):
            self.cart.append(other)
            return self.cart

    def __radd__(self, other):
        if isinstance(other, Order):
            self.cart.append(other)
            return self.cart

    def __sub__(self, other):
        if isinstance(other, Order):
            self.cart.remove(other)
            return self.cart

    def __rsub__(self, other):
        if isinstance(other, Order):
            self.cart.remove(other)
            return self.cart
        


order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')
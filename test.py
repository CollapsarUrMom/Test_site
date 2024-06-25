# Напишите определение класса Order       
class Order:

    def __init__(self, product: list, customer) -> None:
        self.cart = product
        self.customer = customer


    def __add__(self, product: str):
        return Order(self.cart + product.split(), self.customer)


    def __radd__(self, product: str):
        return Order(product.split(',') + self.cart, self.customer)
    

    # def __sub__(self, product: str):
    #     return Order(self.cart - product.split(), self.customer)


    def __sub__(self, product: str):
        lst = []
        for elem in self.cart:
            if product not in elem:
                lst.append(elem)
        return Order(lst, self.customer)
    




# Ниже код для проверки методов класса Order

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
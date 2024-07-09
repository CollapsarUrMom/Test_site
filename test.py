<<<<<<< HEAD
# Напишите определение класса ShoppingCart   
class ShoppingCart:

    def __init__(self):
        self.items = {}


    def __getitem__(self, name):
        if name in self.items:
            return self.items[name]
        elif name not in self.items:
            return 0


    def __setitem__(self, name, quantity):
        self.items[name] = quantity


    def __delitem__(self, name):
        del self.items[name]
            

    def add_item(self, name, quantity= 1):
        if name in self.items:
            self.items[name] = self.items.get(name, 0) + quantity
        elif name not in self.items:
            self.items[name] = quantity


    def remove_item(self, name, quantity= 1):
        if name not in self.items:
            return ValueError
        elif quantity < self.items[name]:
            self.items[name] = self.items.get(name, 0) - quantity
        elif quantity >= self.items[name]:
            del self.items[name]






# Ниже код для проверки методов класса ShoppingCart

# Create a new shopping cart
cart = ShoppingCart()

# Add some items to the cart
cart.add_item('Apple', 3)
cart.add_item('Banana', 2)
cart.add_item('Orange')

assert cart['Banana'] == 2
assert cart['Orange'] == 1
assert cart['Kivi'] == 0

cart.add_item('Orange', 9)
assert cart['Orange'] == 10

print("Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

cart['Apple'] = 5
cart['Banana'] = 7
cart['Kivi'] = 11
assert cart['Apple'] == 5
assert cart['Banana'] == 7
assert cart['Kivi'] == 11

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# Remove an item from the cart
cart.remove_item('Banana')
assert cart['Banana'] == 6

cart.remove_item('Apple', 4)
assert cart['Apple'] == 1

cart.remove_item('Apple', 2)
assert cart['Apple'] == 0
assert 'Apple' not in cart.items

cart.remove_item('Potato')

del cart['Banana']
assert cart['Banana'] == 0
assert 'Banana' not in cart.items

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")
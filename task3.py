class Product:

    def __init__(self, n , p) -> None:
        self.name = n
        self.price = p


class User:

    def __init__(self, l, b= 0) -> None:
        self.login = l
        self.__balance = b


    def __str__(self) -> str:
        return f'Пользователь {self.login}, баланс - {self.__balance}'
    

    @property
    def balance(self):
        return self.__balance
    

    @balance.setter
    def balance(self, value: int):
        self.__balance = value


    def deposit(self, value: int):
        self.__balance += value


    def is_money_enough(self, value: int):
        return value <= self.__balance
    

    def payment(self, value):
        if User.is_money_enough(self, value):
            self.__balance -= value
            return True
        else:
            print('Не хватает средств на балансе. Пополните счет')


class Cart:

    def __init__(self, u: User) -> None:
        self.user = u
        self.goods = {}
        self.__total = 0


    def add(self, product: Product, number_of_product= 1):
        if product in self.goods:
            self.goods[product] += number_of_product
        else:
            self.goods.setdefault(product, number_of_product)
        self.__total += product.price * number_of_product


    def remove(self, product: Product, number_of_product= 1):
        if self.goods[product] > number_of_product:
            self.goods[product] -= number_of_product
            self.__total -= product.price * number_of_product
        else:
            self.__total -= product.price * self.goods[product]
            self.goods.pop(product)


    @property
    def total(self):
        return self.__total
    

    def order(self):
        if User.payment(self.user, self.__total):
            print(f'Заказ оплачен')
        else:
            print(f'Проблема с оплатой')


    def print_check(self):
        print(f'---Your check---')
        for key, value in sorted(self.goods.items(), key=lambda x: x[0].name):
            print(f'{key.name} {key.price} {value} {key.price * value}')
        print(f'---Total: {self.__total}---')





billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20
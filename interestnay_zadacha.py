# Stepik 3.7 Декоратор Property

class Money:

    def __init__(self, dollars, cents) -> None:
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100
    
    @dollars.setter
    def dollars(self, new_dollars):
        if isinstance(new_dollars, int) and new_dollars >= 0:
            self.total_cents = new_dollars * 100 + self.cents
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100
    
    @cents.setter   
    def cents(self, new_cents):
        if isinstance(new_cents, int) and 100 > new_cents >= 0:
            self.total_cents = self.dollars * 100 + new_cents
        else:
            print('Error cents')

    
    def __str__(self) -> str:
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'
    



bill = Money(101, 99)
bill.dollars
bill.cents
assert isinstance(bill, Money)

print(bill)  # Ваше состояние составляет 101 долларов 99 центов
print(bill.dollars, bill.cents)  # 101 99
bill.dollars = 666
print(bill)  # Ваше состояние составляет 666 долларов 99 центов
bill.cents = 12
print(bill)  # Ваше состояние составляет 666 долларов 12 центов
assert bill.total_cents == 66612
assert list(bill.__dict__.keys()) == ['total_cents']

ken = Money(111, 90)
assert isinstance(ken, Money)
print(ken)
ken.dollars = 'hello'  # Error dollars
ken.dollars = 0
print(ken)
ken.cents = [1, 2, 3]  # Error cents
ken.cents = 100  # Error cents
ken.cents = 99
print(ken)
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, (BankAccount, Numbers)):
            return self.balance + other.balance
        elif isinstance(other, (int, float)):
            return self.balance + other
        
    def __radd__(self, other):
        if isinstance(other, (BankAccount, Numbers)):
            return other.balance + self.balance
        elif isinstance(other, (int, float)):
            return other + self.balance

class Numbers:
    def __init__(self, values: list):
        self._values = values

    def __add__(self, other):
        if isinstance(other, (Numbers, BankAccount)):
            return self._values + other._values
        elif isinstance(other, (int, float)):
            return [val + other for val in self._values]
    
    def __radd__(self, other):
        if isinstance(other, (Numbers, BankAccount)):
            return other._values + self._values
        elif isinstance(other, (int, float)):
            return [other + val for val in self._values]
        

#=======================================================================================

lst = [4, BankAccount('Petr', 100), 5]
print(sum(lst)) # 109

lst = [500, BankAccount('Vanya', 200), 7, BankAccount('Ivan', 300), 3]
print(sum(lst)) # 1010
lst = [
    BankAccount('Vanya', 20),
    BankAccount('Ivan', 30),
    BankAccount('Frank', 40),
]
print(sum(lst)) # 90

lst = [
    Numbers([10, 20, 10]),
    BankAccount('Ivan', 30),
    Numbers([30, 40]),
]

print(sum(lst)) # 140

lst = [
    BankAccount('Jack', 1000),
    Numbers([1, 2, 3, 4, 5]),
    BankAccount('Ivan', 30),
    7.5,
    Numbers([10, 20, 30, 40, 50]),
    BankAccount('Frank', 2000),
    10
]
print(sum(lst)) # 3212.5

lst = [
    10,
    Numbers([1, 2, 3, 4, 5]),
    12.5,
    Numbers([10, 20, 30, 40, 50]),
    39,
    Numbers([35]),
]

print(sum(lst)) # 261.5

lst = [
    Numbers([1, 2, 3, 4, 5]),
    Numbers([10, 20, 30, 40, 50]),
    Numbers([35]),
]

print(sum(lst)) # 200
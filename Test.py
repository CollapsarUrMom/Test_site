def calculate(x, y, operation= 'a'):
    
    def addition(x, y):
        print(x + y)

    def subtraction(x, y):
        print(x - y)

    def division(x, y):
        print(x / y)

    def multiplication(x, y):
        print(x * y)

    if y == 0:
        print('На ноль делить нельзя!')
    elif operation == 'a':
        addition(x, y)
    elif operation == 's':
        subtraction(x, y)
    elif operation == 'd':
        division(x, y)
    elif operation == 'm':
        multiplication(x, y)
    elif operation != 'a' and 's' and 'd' and 'm':
        print('Данной операции не существует')



#assert calculate(2, 5) == 7.0
assert calculate(2.2, 15, 'a') == 17.2
assert calculate(22, 15, 's') == 7.0
assert calculate(2, 3.2, 'm') == 6.4
assert calculate(10, 0.4, 'd') == 25.0


#addition - печатаем сложение двух чисел,
#subtraction - печатаем вычитание из первого переданного параметра второго;
#division - печатаем деление первого на второго,
#multiplication - печатаем умножение двух чисел.
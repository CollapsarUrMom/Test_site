class Vector:

    def __init__(self, *num):
        lst = []
        [lst.append(i) for i in num if isinstance(i, int)]
        self.values = sorted(lst)


    def __str__(self):
        if self.values:
            my_lst = [str(i) for i in self.values]
            return f'Вектор({", ".join(my_lst)})'
        else:
            return 'Пустой вектор'
        

    def __add__(self, other_vector):
        if isinstance(other_vector, int):
            lst_int = [num + other_vector for num in self.values]
            return Vector(*lst_int)
        elif isinstance(other_vector, Vector):
            if len(other_vector.values) == len(self.values):
                lst_vec = [sum(i) for i in zip(self.values, other_vector.values)]
                return Vector(*lst_vec)
            else:
                print('Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other_vector}')


    def __mul__(self, other_vector):
        if isinstance(other_vector, int):
            lst_mul = [num * other_vector for num in self.values]
            return Vector(*lst_mul)
        elif isinstance(other_vector, Vector):
            if len(other_vector.values) == len(self.values):
                lst_vec = [i[0] * i[1] for i in zip(self.values, other_vector.values)]
                return Vector(*lst_vec)
            else:
                print('Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножать с {other_vector}')



v1 = Vector(1, 2, 3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
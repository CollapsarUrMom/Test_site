def handle_case_1():
    print("Создание базы дааных")

def handle_case_2():
    print("Создание объекта")

def handle_case_3():
    print("Добавление данных в базу данных")

def handle_case_4():
    print("Конец")

def handle_default():
    print("Нет такой команды")

switch_case = {
    1: handle_case_1, # Создание базы данных
    2: handle_case_2, # Добавь данные в базу данных
    3: handle_case_3, # Добавление данных в базу данных
    4: handle_case_4, # Конец
}
condition = '1'

while condition != 4:
    condition = int(input("Введите команду: "))
    action = switch_case.get(condition, handle_default)
    action()
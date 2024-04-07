import CheckList
import myjson
import data_base


celendar_day = {1:'c', 2:'d', 3:'e', 4:'f', 5:'g', 6:'h', 7:'i', 8:'j', 9:'k', 10:'l', 11:'m', 12:'n',
             13:'o', 14:'p', 15:'q', 16:'r', 17:'s', 18:'t', 19:'u', 20:'v', 21:'w', 22:'x', 23:'y',
             24:'z', 25:'aa', 26:'ab', 27:'ac', 28:'ad', 29:'ae', 30:'af', 31:'ag'}

celendar_month = {1:'Январь', 2:'Февраль', 3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь',
                    7:'Июль', 8:'Август', 9:'Сентябрь', 10:'Октябрь', 11:'Ноябрь', 12:'Декабрь'}

#D:\\Alex\\Python\\Test_site\\programma_dly_obrabotki_chekov  Компьютер

#C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov  Ноутбук

basket = CheckList.CheckList()
comand = '1'
file = 'programma_dly_obrabotki_chekov\\project\\extract.json'


def handle_case_1():
    data_base.Data_base.file_search(basket, file)

def handle_case_2():
    data_base.Data_base.adding_data_to_the_database(basket, myjson.Json.json_converting(basket))

def handle_case_3():
    myjson.Json.adding_data_to_an_object(basket, myjson.Json.json_converting(basket))

def handle_case_4():
    print("Конец")

def handle_default():
    print("Нет такой команды")

switch_case = {
    1: handle_case_1, # Найди файл
    2: handle_case_2, # Добавь данные в базу данных
    3: handle_case_3, # Добавление данных в объект
    4: handle_case_4, # Конец
}


while comand != 4:
    comand = int(input("Введите команду: "))
    action = switch_case.get(comand, handle_default)
    action()


print('Stop!!!')
print('Stop!!!')
print('Stop!!!')
print('Stop!!!')





print('Good')
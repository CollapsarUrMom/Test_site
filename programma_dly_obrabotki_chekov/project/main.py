import openpyxl
import json

#===============================================
#  Json файла с чеками

with open('C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov\\project\\extract.json', mode= 'r', encoding= 'UTF-8') as file:
    my_file = json.load(file)
    new_json = json.dumps(my_file, ensure_ascii= False, indent= 4)
    my_json = json.loads(new_json)
    with open('C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov\\project\\cheque.json', 'w', encoding= 'UTF-8') as out_file:
        json.dump(my_file, out_file, ensure_ascii= False, indent= 4)\


celendar_day = {1:'c', 2:'d', 3:'e', 4:'f', 5:'g', 6:'h', 7:'i', 8:'j', 9:'k', 10:'l', 11:'m', 12:'n',
             13:'o', 14:'p', 15:'q', 16:'r', 17:'s', 18:'t', 19:'u', 20:'v', 21:'w', 22:'x', 23:'y',
             24:'z', 25:'aa', 26:'ab', 27:'ac', 28:'ad', 29:'ae', 30:'af', 31:'ag'}

celendar_month = {1:'Январь', 2:'Февраль', 3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь',
                    7:'Июль', 8:'Август', 9:'Сентябрь', 10:'Октябрь', 11:'Ноябрь', 12:'Декабрь'}

#===============================================
#  Открытие сущетвующего файла exel и его наполнение чеками

wb = openpyxl.load_workbook(filename= 'C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov\\my_finances.xlsx')

expenses = wb['Расходы']
income = wb['Доходы']


class Check:

    def __init__(self, inf, data) -> dict:
        self.inf = inf
        self.data = data

    def searching_for_an_empty_cell(self, name, price, month, day):
        count = 1
        while expenses[f'A{count}'].value != celendar_month[month]:
            count += 1
        while expenses[f'B{count + 1}'].value != None or name:
            count += 1
        expenses[f'B{count}'] = name
        expenses[f'{celendar_day[day]}{count}'] = price

class CheckList:

    def __init__(self) -> list:
        self.purchases = []

    def add_product(self, product) -> list:
        self.purchases.append(product)


basket = CheckList()

for i in range(len(my_json)):
    product = Check(my_json[i]['ticket']['document']['receipt']['items'][0],
                    my_json[i]['ticket']['document']['receipt']['dateTime'][:10].split('-'))
    basket.add_product(product)
    product.searching_for_an_empty_cell(product.inf['name'], product.inf['price'] / 100 * product.inf['quantity'],
                                        int(product.data[1]), int(product.data[2]))

for i in basket.purchases:
    print(i.inf['name'])
    

print('Yes')
  

wb.save('C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov\\my_finances.xlsx')
wb.close()
print('Good')
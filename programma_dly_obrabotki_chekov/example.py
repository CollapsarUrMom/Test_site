import openpyxl
import json

with open('C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov\\extract.json', mode= 'r', encoding= 'UTF-8') as file:
    my_file = json.load(file)
    new_json = json.dumps(my_file, ensure_ascii=False, indent= 4)
    my_json = json.loads(new_json)

cheque = my_json[0]

data_purchase = cheque['createdAt']
product_name = cheque["ticket"]["document"]["receipt"]["items"][1]["name"]
price_product = cheque["ticket"]["document"]["receipt"]["items"][0]["price"]
quantity = cheque["ticket"]["document"]["receipt"]["items"][0]["quantity"]

count_items = len(cheque["ticket"]["document"]["receipt"]["items"])

dict_product = {}

for i in range(count_items):
    #dict_product = {cheque["ticket"]["document"]["receipt"]["items"][i]["name"] : [cheque["ticket"]["document"]["receipt"]["items"][i]["price"], cheque["ticket"]["document"]["receipt"]["items"][i]["quantity"]]}
    dict_product[cheque["ticket"]["document"]["receipt"]["items"][i]["name"]] = [cheque["ticket"]["document"]["receipt"]["items"][i]["price"] / 100,
                                                                                  cheque["ticket"]["document"]["receipt"]["items"][i]["quantity"], 
                                                                                  cheque['createdAt'][0:-15]]

print(dict_product)

#wb = Workbook()
#income = wb.active
#expenses = wb.create_sheet('Расходы')
#income.title = 'Доходы'
#income['A1'] = product_name
#expenses['A1'] = 'Январь'
#expenses['A2'] = 'Категория'
#expenses['B2'] = 'Подкатегория'
#expenses['A3'] = 'Продукты'
celendar = {1:'c', 2:'d', 3:'e', 4:'f', 5:'g', 6:'h', 7:'i', 8:'j', 9:'k', 10:'l', 11:'m', 12:'n',
             13:'o', 14:'p', 15:'q', 16:'r', 17:'s', 18:'t', 19:'u', 20:'v', 21:'w', 22:'x', 23:'y',
             24:'z', 25:'aa', 26:'ab', 27:'ac', 28:'ad', 29:'ae', 30:'af', 31:'ag'}
#print(wb.sheetnames)


wb = openpyxl.load_workbook(filename= 'test.xlsx')

expenses = wb['Расходы']
income = wb['Доходы']

i = 3

for product in dict_product.keys():
    month = int(dict_product[product][2][5:7])
    day = int(dict_product[product][2][8:])
    expenses[f'B{i}'] = product
    expenses[f'{celendar[day]}{i}'] = dict_product[product][0] #price
    i += 1

#expenses.move_range("A4:C6", rows= -1, cols= 1)


wb.save('test.xlsx')
wb.close()
print('Good')







#'C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\My.json'

#'C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov\\extract.json'
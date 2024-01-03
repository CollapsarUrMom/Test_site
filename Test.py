import json

with open('D:\\Alex\\Сегодня\\manager_sales.json', 'r') as file:
    print(type(file))
    string = json.load(file)
    print(type(string))
    my_file = json.dumps(string, indent= 4)
    
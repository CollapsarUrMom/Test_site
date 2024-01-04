import json

with open('D:\\Alex\\Сегодня\\manager_sales.json', 'r') as file_json:
    data = json.load(file_json)
a = []
for i in data:
    a.append((i['manager']['first_name'], i['manager']['last_name'], sum(s['price'] for s in i['cars'])))

print(*sorted(a, key=lambda x: x[2], reverse=True)[0])
import json
from pprint import pprint
from random import randint

str_json = """
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina",
                "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod",
                "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
            }
        ]
    }
}
"""

data = json.loads(str_json)

for item in data["response"]["items"]:
  del item["id"]
  item["likes"] = randint(100, 200)
  
new_json = json.dumps(data)
print(new_json)
print(type(new_json))

print('Ниже json с параметром indent'.center(40, '-'))

json_indent = json.dumps(data, indent = 2)
print(json_indent)
print(type(json_indent))
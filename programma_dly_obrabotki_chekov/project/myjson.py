import json
import Check
import CheckList

class Json:

    def json_converting(self) -> None:
        """Обрабатывает json файл в Python json"""
        with open('C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov\\project\\extract.json', mode= 'r', encoding= 'UTF-8') as file:
            my_file = json.load(file)
            new_json = json.dumps(my_file, ensure_ascii= False, indent= 4)
            return json.loads(new_json)
            #with open('D:\\Alex\\Python\\Test_site\\programma_dly_obrabotki_chekov\\project\\cheque.json', 'w', encoding= 'UTF-8') as out_file:
                #json.dump(my_file, out_file, ensure_ascii= False, indent= 4)
  
    def adding_data_to_an_object(self, my_json):
        """Добавляет покупки в объект"""
        for i in range(len(my_json)):
            for j in range(len(my_json[i]['ticket']['document']['receipt']['items'])):
                product = Check.Check(
                    int(my_json[i]['ticket']['document']['receipt']['dateTime'][:4]),
                    int(my_json[i]['ticket']['document']['receipt']['dateTime'][5:7]),
                    int(my_json[i]['ticket']['document']['receipt']['dateTime'][8:10]),
                    my_json[i]['ticket']['document']['receipt']['items'][j]['name'],
                    my_json[i]['ticket']['document']['receipt']['items'][j]['price'],
                    my_json[i]['ticket']['document']['receipt']['items'][j]['quantity']
                )
                CheckList.CheckList.add_product(self, product)



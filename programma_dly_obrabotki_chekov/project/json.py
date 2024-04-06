import json
import data_base
import Check
import CheckList


class Json:

    def json_converting(self, file) -> None:
        with open('D:\\Alex\\Python\\Test_site\\programma_dly_obrabotki_chekov\\project\\extract.json', mode= 'r', encoding= 'UTF-8') as file:
            my_file = json.load(file)
            new_json = json.dumps(my_file, ensure_ascii= False, indent= 4)
            my_json = json.loads(new_json)
            with open('D:\\Alex\\Python\\Test_site\\programma_dly_obrabotki_chekov\\project\\cheque.json', 'w', encoding= 'UTF-8') as out_file:
                json.dump(my_file, out_file, ensure_ascii= False, indent= 4)



    basket = CheckList.CheckList()
    
    def asdf(self, my_json):
        for i in range(len(my_json)):
            for j in range(len(my_json[i]['ticket']['document']['receipt']['items'])):
                lst = []

                lst.append(int(my_json[i]['ticket']['document']['receipt']['dateTime'][:4]))
                lst.append(int(my_json[i]['ticket']['document']['receipt']['dateTime'][5:7]))
                lst.append(int(my_json[i]['ticket']['document']['receipt']['dateTime'][8:10]))
                lst.append(my_json[i]['ticket']['document']['receipt']['items'][j]['name'])
                lst.append(my_json[i]['ticket']['document']['receipt']['items'][j]['price'])
                lst.append(my_json[i]['ticket']['document']['receipt']['items'][j]['quantity'])

                data_base.Data_base.add_inf(str(lst))
                product = Check.Check(int(my_json[i]['ticket']['document']['receipt']['dateTime'][:4]),
                int(my_json[i]['ticket']['document']['receipt']['dateTime'][5:7]),
                int(my_json[i]['ticket']['document']['receipt']['dateTime'][8:10]),
                my_json[i]['ticket']['document']['receipt']['items'][j]['name'],
                my_json[i]['ticket']['document']['receipt']['items'][j]['price'],
                my_json[i]['ticket']['document']['receipt']['items'][j]['quantity']
                )
                basket.add_product(product)
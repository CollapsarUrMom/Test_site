import data_base
import os.path
import myjson

class Data_base:

    def file_search(self, file):
        """Проверяет наличие файла json"""
        if os.path.isfile(file):
            print('Есть такой файл!')
        else:
            print('Нет такого файла :(')


    def add_data(self, data):
        """Добавляет нужные данные в базу данных"""
        with open('C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov\\project\\Base.txt', mode='a', encoding= 'UTF-8') as file:
            file.write(str(data) + '\n')


    def adding_data_to_the_database(self, my_json):
        """Вытягивает нужные данные из json"""
        for i in range(len(my_json)):
            for j in range(len(my_json[i]['ticket']['document']['receipt']['items'])):
                lst = []
                lst.append(int(my_json[i]['ticket']['document']['receipt']['dateTime'][:4]))
                lst.append(int(my_json[i]['ticket']['document']['receipt']['dateTime'][5:7]))
                lst.append(int(my_json[i]['ticket']['document']['receipt']['dateTime'][8:10]))
                lst.append(my_json[i]['ticket']['document']['receipt']['items'][j]['name'])
                lst.append(my_json[i]['ticket']['document']['receipt']['items'][j]['price'])
                lst.append(my_json[i]['ticket']['document']['receipt']['items'][j]['quantity'])
                data_base.Data_base.add_data(self, lst)
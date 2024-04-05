class Data_base:

    def add_inf(inf, data= '0'):
        with open('D:\\Alex\\Python\\Test_site\\programma_dly_obrabotki_chekov\\project\\Base.txt', mode='a') as file:
            if isinstance(inf, str) and isinstance(data, list):
                file.write(inf)
            elif isinstance(inf, dict) and isinstance(data, list):
                file.writelines(inf, data)
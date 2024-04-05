class Data_base:

    def add_inf(inf, data):
        with open('C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\programma_dly_obrabotki_chekov\\project\\Base.txt', mode='a') as file:
            if isinstance(inf, str):
                file.write(inf, data)
            elif isinstance(inf, list):
                file.writelines(inf, data)
class Building:

    def __init__(self, args):
        self.lst_floors = []
        self.lst_floors.extend([0] * args)


    def __setitem__(self, floor, name):
        self.lst_floors[floor] = name
        return self.lst_floors


    def __getitem__(self,floor):
        if 0 < floor < len(self.lst_floors):
            return self.lst_floors[floor]
        else:
            raise IndexError("Индекс за пределами коллекции")


    def __delitem__(self, floor):
        if 0 <= floor < len(self.lst_floors):
            self.lst_floors[floor] = None
            # del self.lst_floors[floor]
        else:
            raise IndexError("Индекс за пределами коллекции")


print('==================')
iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
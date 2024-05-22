class Robot:
    population = 0

    def __init__(self, n) -> None:
        self.name = n
        self.population += 1
        print(f'Робот {self.name} был создан')

    def destroy(self):
        self.population -= 1
        print(f'Робот {self.name} был уничтожен')

    

    

# код ниже не нужно удалять, в нем находятся проверки

droid1 = Robot("R2-D2")
assert droid1.name == 'R2-D2'
assert Robot.population == 1
droid1.say_hello()
Robot.how_many()
droid2 = Robot("C-3PO")
assert droid2.name == 'C-3PO'
assert Robot.population == 2
droid2.say_hello()
Robot.how_many()
droid1.destroy()
assert Robot.population == 1
droid2.destroy()
assert Robot.population == 0
Robot.how_many()
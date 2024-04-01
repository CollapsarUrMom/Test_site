class Example1:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
 
    def out(self):
        print("Взыван метод класса {}".format(self.__class__.__name__))
 
 
class Example2:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
 
    def print_data(self):
        print([getattr(self, 'data{}'.format(i)) for i in (1, 2)])
 
 
inst1 = Example1('agg', 'foo')
inst1.out()
 
inst2 = Example2('1234', '687')
inst2.print_data()
class DepartmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def hiring_python_dev(self):
        self.PYTHON_DEV = self.PYTHON_DEV + 1


    @classmethod
    def add_python_dev(cls):
        cls.PYTHON_DEV = cls.PYTHON_DEV + 10

    @classmethod
    def add_attr(cls, name_attr, val_attr):
        setattr(cls, name_attr, val_attr)

    @classmethod
    def add_attr_1(cls):
        cls.new_attr = cls.new_attr + 100

    @classmethod
    def add_attr_2(cls, name_attr, val_attr):
        setattr(cls, name_attr, val_attr) 


it1 = DepartmentIT()
it2 = DepartmentIT()
print(it1.__dict__)
print(DepartmentIT.__dict__)
it1.hiring_python_dev() 
it1.hiring_python_dev()
print(it1.PYTHON_DEV)
print(DepartmentIT.PYTHON_DEV)
print('++++++++++++++++++++++++++++++')

it1.add_python_dev()
print(it1.PYTHON_DEV)
print(DepartmentIT.PYTHON_DEV)
DepartmentIT.add_python_dev()
print(it1.PYTHON_DEV)
print(DepartmentIT.PYTHON_DEV)
print('++++++++++++++++++++++++++++++')

it3 = DepartmentIT()
it1.add_attr('new_attr', 100)
print(it1.__dict__)
print(DepartmentIT.__dict__)
print(it1.new_attr)
print(it1.GO_DEV)
print(it1.__dict__)
print('++++++++++++++++++++++++++++++')

it1.add_attr_1()
print(it1.new_attr)
print(it2.new_attr)
print(it3.new_attr)
print(DepartmentIT.new_attr)
class Numbers:

    def __init__(self, *args):
        self.lst = list(args)

    def get_positive(self):
        return [i for i in self.lst if i > 0]
    
    def get_negative(self):
        return [i for i in self.lst if i < 0]
    
    def get_zeroes(self):
        return [i for i in self.lst if i == 0]
    
    def add_number(self, num):
        self.lst.append(num)
    

nums = Numbers(1, 2, -4, -5, 3)
assert nums.lst == [1, 2, -4, -5, 3]
assert nums.get_positive() == [1, 2, 3]
assert nums.get_negative() == [-4, -5]

nums2 = Numbers(10, 20, 30, 0, 0, 5)

assert nums2.get_positive() == [10, 20, 30, 5]
assert nums2.get_zeroes() == [0, 0]
nums2.add_number(100)
nums2.add_number(0)
nums2.add_number(7)
assert nums2.get_positive() == [10, 20, 30, 5, 100, 7]
assert nums2.get_zeroes() == [0, 0, 0]

nums = Numbers(7, 8, 9)
nums_2 = Numbers(7, 8, 9)

nums.add_number(10)
nums_2.add_number(11)
nums_2.add_number(12)
assert nums.get_positive() == [7, 8, 9, 10]
assert nums_2.get_positive() == [7, 8, 9, 11, 12]

nums_3 = Numbers(-1, -2, -3, 0, -6, -4, 0, 0)

assert nums_3.get_positive() == []
assert nums_3.get_negative() == [-1, -2, -3, -6, -4]
assert nums_3.get_zeroes() == [0, 0, 0]
print('Good')
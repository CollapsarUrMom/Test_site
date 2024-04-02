class Triangle:
    def __init__(self, *args):
        self.sides = args

    def is_exists(self):
        print(sum(self.sides))
        print(max(self.sides))
        print(min(self.sides))
        return sum(self.sides) > 2 * max(self.sides) and min(self.sides) > 0
    
    def unique_sides(self):
        print(set(self.sides))
        return len(set(self.sides))

    def is_equilateral(self):
        return self.is_exists() and self.unique_sides() == 1

    def is_isosceles(self):
        return self.is_exists() and self.unique_sides() <= 2
    

triangle = Triangle(3, 4, 5)
print(f"Is Triangle exist: {triangle.is_exists()}")
print(f"Is Equilateral: {triangle.is_equilateral()}")
print(f"Is Isosceles: {triangle.is_isosceles()}")

triangle = Triangle(5, 5, 5)
print(f"Is Triangle exist: {triangle.is_exists()}")
print(f"Is Equilateral: {triangle.is_equilateral()}")
print(f"Is Isosceles: {triangle.is_isosceles()}")

triangle = Triangle(5, 4, 5)
print(f"Is Triangle exist: {triangle.is_exists()}")
print(f"Is Equilateral: {triangle.is_equilateral()}")
print(f"Is Isosceles: {triangle.is_isosceles()}")

triangle = Triangle(5, 16, 5)
print(f"Is Triangle exist: {triangle.is_exists()}")
print(f"Is Equilateral: {triangle.is_equilateral()}")
print(f"Is Isosceles: {triangle.is_isosceles()}")
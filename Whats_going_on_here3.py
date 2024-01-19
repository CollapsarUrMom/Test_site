# Напишите определение функции zip_with_function
def zip_with_function(lst, f) -> list[str, int]:
    return list(map(lambda args: f(*args), zip(*lst)))




def combine_strings(a: str, b: str) -> str:
    return a + b


def get_sum_two_numbers(a: int, b: int) -> int:
    return a + b


def get_sum_three_numbers(a: int, b: int, c: int) -> int:
    return a + b + c


assert zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers) == [4, 7, 12]
assert zip_with_function([[10, 20], [30, 0]], get_sum_two_numbers) == [40, 20]
assert zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers) == [10, 15, 20]
assert zip_with_function([[1, 2, 3], [4, 5, 6], [7, 8, 9]], get_sum_three_numbers) == [12, 15, 18]
assert zip_with_function([["a", "b"], ["1", "2"]], combine_strings) == ['a1', 'b2']
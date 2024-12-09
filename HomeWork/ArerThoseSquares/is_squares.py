import math


def is_list_squares(lst):
    for num in lst:
        if num < 0:
            return False
        n = math.isqrt(num)
        if not n * n == num:
            return False
    return True

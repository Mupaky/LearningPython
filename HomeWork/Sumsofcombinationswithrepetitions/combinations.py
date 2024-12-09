from itertools import product

def sums_of_n(n, lst):
    sums = set()

    for k in range(n, n + 1):
        for roll in product(lst, repeat=k):
            sums.add(sum(roll))
    return sums

print(sums_of_n(3, [1, 2]))
# print(sums_of_n(3, [1, 2])) # {3, 4, 5, 6}
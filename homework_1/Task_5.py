from functools import reduce


def count_find_num(primesL, limit):
    """
    Returns the number of variants of the product of numbers from the list that does
    not exceed the specified limit, as well as the maximum product of these numbers.
    The numbers from the list can be used multiple times.
    """
    multiply = reduce(lambda x, y: x * y, primesL)
    res_list = [multiply]

    if multiply > limit:
        return []

    for i in primesL:
        for j in res_list:
            j *= i
            while j <= limit and j not in res_list:
                res_list.append(j)
                j *= i

    max_num = max(res_list)
    count = len(res_list)

    return [count, max_num]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

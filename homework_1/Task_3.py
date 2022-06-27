def zeros(n):
    """Calculates the number of finite zeros in the factorial"""
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
assert zeros(6) == 1
assert zeros(12) == 2

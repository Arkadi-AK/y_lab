def cache_func(function):
    cache = {}

    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result
            return result

    return inner


@cache_func
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(10))
    print(multiplier(2))
    print(multiplier(5))
    print(multiplier(10))
    print(multiplier(4))

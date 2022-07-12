from itertools import cycle


class CyclicIterator:
    def __init__(self, iterable):
        self.data = cycle(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)


class Range2:
    def __init__(self, stop: int):
        self.index = -1
        self.stop = stop - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.stop:
            self.index += 1
            return self.index
        raise StopIteration("Stop Iteration occured")


if __name__ == '__main__':
    # cyclic_iterator = CyclicIterator(range(3))
    # cyclic_iterator = CyclicIterator([1, 2, 3, 4, 5])
    # cyclic_iterator = CyclicIterator(["A", "B", "C"])
    # cyclic_iterator = CyclicIterator((1, 2, 3, 4, 5))
    # cyclic_iterator = CyclicIterator({a, b, c, d, e})
    cyclic_iterator = CyclicIterator(Range2(4))

    for i in cyclic_iterator:
        print(i)

from itertools import combinations


def bananas(s) -> set:
    result = set()
    default = 'banana'
    couples = enumerate(s)
    comb = combinations(couples, 6)
    for i in comb:
        dash_word = ['-' for i in range(len(s))]
        add_word = ''.join(j[1] for j in i)
        if add_word == default:
            for y in i:
                dash_word[y[0]] = y[1]
            result.add(''.join(dash_word))
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

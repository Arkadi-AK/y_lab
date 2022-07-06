from itertools import permutations

point_1 = (0, 2)  # Почтовое отделение – (0, 2)
point_2 = (2, 5)  # Ул. Грибоедова, 104/25 – (2, 5)
point_3 = (5, 2)  # Ул. Бейкер стрит, 221б – (5, 2)
point_4 = (6, 6)  # Ул. Большая Садовая, 302-бис – (6, 6)
point_5 = (8, 3)  # Вечнозелёная Аллея, 742 – (8, 3)

my_route = [[None, [], None], []]
points = [point_2, point_3, point_4, point_5]


def add_start_point(path: list, point: tuple):
    path[0][0] = point


def add_stop_point(path: list, point: tuple):
    path[0][2] = point


def add_point(path: list, point: tuple):
    path[0][1].append(point)


def calculate_length_between_two_points(point_a: tuple, point_b: tuple) -> float:
    return ((point_b[0] - point_a[0]) ** 2
            + (point_b[1] - point_a[1]) ** 2
            ) ** 0.5


def calculate_length_between_all_points(path: list):
    n = len(path[0][1]) + 1
    for i in range(n):
        if i == 0:
            length_path = calculate_length_between_two_points(path[0][0], path[0][1][i])
            path[1].append(length_path)
        elif i < len(path[0][1]):
            length_path = calculate_length_between_two_points(path[0][1][i - 1], path[0][1][i])
            path[1].append(length_path + path[1][i - 1])
        else:
            length_path = calculate_length_between_two_points(path[0][1][i - 1], path[0][2])
            path[1].append(length_path + path[1][i - 1])


def get_combinations(path: list) -> list:
    combination_list = []
    for i in permutations(path[0][1]):
        temp_path = [[None, [], None], []]
        temp_path[0][0] = path[0][0]
        temp_path[0][2] = path[0][2]
        temp_path[0][1] = list(i)
        combination_list.append(temp_path)
    return combination_list


def calculate_min_route(path: list) -> list:
    if len(path[0][1]) == 0:
        length_path = calculate_length_between_two_points(path[0][0], path[0][2])
        path[1].append(length_path)
        return path
    elif len(path[0][1]) == 1:
        calculate_length_between_all_points(path)
        return path
    else:
        min_path = None
        combination_list = get_combinations(path)
        for i in combination_list:
            calculate_length_between_all_points(i)
            if min_path is None:
                min_path = i
            elif min_path[1][-1:] > i[1][-1:]:
                min_path = i
        return min_path


def print_route(path: list):
    n = len(path[0][1]) + 1
    for i in range(n):
        if i == 0:
            print(f'{path[0][0]} -> {path[0][1][i]}[{path[1][i]}] -> ', end='')
        elif i < len(path[0][1]):
            print(f'{path[0][1][i]}[{path[1][i]}] -> ', end='')
        else:
            print(f'{path[0][2]}[{path[1][i]}] = {path[1][i]}')


if __name__ == "__main__":
    add_start_point(my_route, point_1)
    add_stop_point(my_route, point_1)
    for i in points:
        add_point(my_route, i)
    finish_route = calculate_min_route(my_route)
    print_route(finish_route)

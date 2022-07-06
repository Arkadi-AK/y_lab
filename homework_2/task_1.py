point_1 = (0, 2)  # Почтовое отделение – (0, 2)
point_2 = (2, 5)  # Ул. Грибоедова, 104/25 – (2, 5)
point_3 = (5, 2)  # Ул. Бейкер стрит, 221б – (5, 2)
point_4 = (6, 6)  # Ул. Большая Садовая, 302-бис – (6, 6)
point_5 = (8, 3)  # Вечнозелёная Аллея, 742 – (8, 3)

# route
points = [(0, 2), (2, 5), (6, 6), (8, 3), (5, 2)]

# starting point
start_point = min(points)


def calculate_points(first_point: tuple, second_point: tuple) -> float:
    """calculates distances between points"""
    return (
                   (second_point[0] - first_point[0]) ** 2
                   + (second_point[1] - first_point[1]) ** 2
           ) ** 0.5


def calculate_short_path(route):
    """Iterates through all the points and outputs the path"""
    calculated_points = 0
    last_point = 0
    print(start_point, end=" -> ")
    for current_point in range(len(route) - 1):
        last_point = current_point
        next_point = current_point + 1
        current_path = calculate_points(route[current_point], route[next_point])
        calculated_points += current_path
        print(f"{route[next_point]}[{calculated_points}]", end=" -> ")
    finish_point = calculated_points + calculate_points(
        route[last_point + 1], start_point
    )
    print(f"{start_point}, [{finish_point}] = {finish_point}")


if __name__ == "__main__":
    calculate_short_path(points)

from itertools import permutations
from functools import lru_cache


@lru_cache()
def calculate_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def get_shortest_route_description(points: list) -> str:
    """Get a string describing the shortest route to visit all points once.

    Starting from points[0] and returning to points[0].
    No more than 11 points due to high CPU load.
    """
    number_of_points = len(points)
    if number_of_points > 11:
        raise ValueError('Too many points, maximum 11 points supported.')

    # store each possible route as a list of points
    goals = points[1:]
    partial_routes = permutations(goals)
    full_routes = []
    for partial_route in partial_routes:
        full_routes.append([points[0]] + list(partial_route) + [points[0]])

    # calculate the total distance for each route
    full_distances = []
    for full_route in full_routes:
        full_distance = 0
        for i in range(number_of_points):
            point1 = full_route[i]
            point2 = full_route[i + 1]
            full_distance += calculate_distance(point1, point2)
        full_distances.append(full_distance)

    index_min = min(range(len(full_distances)), key=full_distances.__getitem__)
    shortest_route = full_routes[index_min]

    shortest_route_description = f'{points[0]}'
    full_distance = 0
    for i in range(number_of_points):
        point1 = shortest_route[i]
        point2 = shortest_route[i + 1]
        full_distance += calculate_distance(point1, point2)
        shortest_route_description += f' -> {point2}[{full_distance}]'
    shortest_route_description += f' = {full_distances[index_min]}'

    return shortest_route_description


if __name__ == "__main__":
    points = [
        (0, 2),
        (2, 5),
        (5, 2),
        (6, 6),
        (8, 3),
    ]
    print(get_shortest_route_description(points))
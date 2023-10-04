points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    coord_count = len(coordinates)
    if coord_count <= 1:
        return 0
    
    dist = 0
    for i in range(1, coord_count):
        dist += points.get(tuple(sorted((coordinates[i], coordinates[i - 1]))))
    
    return dist

print(calculate_distance([0, 1, 3, 2, 0]))
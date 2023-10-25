from random import randrange
from comparison import Point, Vector


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = Iterable.generate_vectors(
            vector_count=max_vectors, max_point=max_points)
        self.__MAX_VECTORS = max_vectors
        self.__max_points = max_points

    @staticmethod
    def generate_vectors(vector_count: int, max_point: int):
        vectors = [vector_count]
        for i in range(vector_count + 1):
            point = Point(randrange(0, stop=max_point),
                          randrange(0, stop=max_point))
            vectors.append(Vector(point))
        return vectors

    def __next__(self):
        if self.current_index < self.__MAX_VECTORS:
            self.current_index += 1
            return self.vectors[self.current_index]
        raise StopIteration


class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)


if __name__ == "__main__":
    vectors = RandomVectors(5, 10)

    for vector in vectors:
        print(vector)

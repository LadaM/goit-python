class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, int) or isinstance(x, float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, int) or isinstance(y, float):
            self.__y = y

if __name__ == "__main__":
    point = Point("a", 10)

    print(point.x)  # None
    print(point.y)  # 10
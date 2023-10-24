class Multiplicator:
    def doubler(self, x):
        print('Mul on 2: %s' % self)
        return x * 2

    def tripler(self, x):
        print('Mul on 3: %s' % self)
        return x * 3
    
    @classmethod
    def class_method(cls):
        print('Working on class and object the same way %s' % cls)

    # is the same as a function that could be written outside
    # can be used for Factory pattern
    @staticmethod
    def static_method(int):
        print("Can print a number %d" % int)

multi = Multiplicator()
print(multi.doubler(10))
Multiplicator.class_method()
multi.class_method()
Multiplicator.static_method(8)
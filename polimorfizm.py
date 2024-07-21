class Shape:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        raise NotImplementedError()


class Square(Shape):
    def area(self):
        return self.a * self.a


class Circle(Shape):

    def area(self):
        return 3.14 * self.r * self.r



lst = [Square(a=5), Circle(r=10), Square(a=1), Circle(r=3)]
for item in lst:
    print(item.area())

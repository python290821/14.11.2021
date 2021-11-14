class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __add__(self, other):
        # c1 = Cirlce(2)
        # c2 = Circle(3)
        # c3 <= c1 + c2
        # print(c1 + c2)
        # Circle + 4 [int]
        # Circle + 4.2 [float]
        # c = c + 'hello'
        if type(other) == int or type(other) == float:
            return Circle(self.radius + other)
        if type(self) != type(other):
            return Circle(self.radius)
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        # Circle - 4 [int]
        # Circle - 4.2 [float]
        # Circle - Circle
        # Cirlce - 'hello' ==> do nothing
        if type(other) == int or type(other) == float:
            return Circle(self.radius - other)
        if type(self) != type(other):
            return Circle(self.radius)
        return Circle(self.radius - other.radius)

    def __mul__(self, other):
        # Circle * 4 [int]
        # Circle * 4.2 [float]
        # c = c * 'hello'
        if type(other) == int or type(other) == float:
            return Circle(self.radius * other)
        if type(self) != type(other):
            return Circle(self.radius)
        return Circle(self.radius * other.radius)

    # c1 = Cirlce(2)
    # c1 == 2
    # c2 = Cirlce(2)
    # c1 == c2
    def __eq__(self, other):
        if type(other) == int or type(other) == float:
            return self.radius == other
        if type(self) != type(other):
            return False
        return self.radius == other.radius

    def __gt__(self, other):
        if type(other) == int or type(other) == float:
            return self.radius > other
        if type(self) != type(other):
            return False
        return self.radius > other.radius

    def __repr__(self):
        return f'Circle({self.radius})'

    def __str__(self):
        return f'Circle radius:{self.radius}'

c1 = Circle(3)
print('__str__',c1)
c2 = Circle(8.7)
_lst = [c2, c1]
print('before sort',_lst)
_lst.sort()
print('after sort',_lst)
print('__repr__', _lst)
print(c1, '> gt ', c2,  '=', c1.__gt__(c2))
print(c1, '>', c2,  '=', c1 > c2) # __gt__
c3 = Circle(8.7)
print(c2, '==', c3,':', c2 == c3) # __eq__
print(c2, '==', 8.7,':', c2 == 8.7)
print(c1, '+', c3,':', c1 + c3)




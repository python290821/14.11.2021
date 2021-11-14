class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # self == other ?
    # left is self p1 == p4 right is other
    def __eq__(self, other):
        #if self.x == other.x and self.y == other.y:
         #   return True
        #else:
         #   return False
        if type(other) != type(self):
            return False
        return self.x == other.x and self.y == other.y

    # p3 = p1 + p2
    # p3 = p1 + None
    def __add__(self, other):
        if other == None:
            return self
        if type(other) == int:
            return Point(self.x + other, self.y + other)
        if type(other) == tuple:
            return Point(self.x + other[0], self.y + other[1])
        if type(other) != type(self):
            return self
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'Point x:{self.x} y:{self.y}'

class Circle:
    pass


p1 = Point(3.4, 12.1)
p2 = Point(2.1, 2.22)
p4 = Point(3.4, 12.1)
c1 = Circle()
print('p1 == None', p1 == None)
print('p1 == c1 [circle]', p1 == c1)
print('p1 == p4', p1 == p4) # True
print('p1 == Point(3.4, 12.1)', p1 == Point(3.4, 12.1)) # True
p3 = p1 + p2
print('p3 = p1 + p2',p3)
p4 = p1 + 5 # p1.x + 5, p2 + 5
p5 = p1 + (5, 1) # p1.x + 5, p2 + 1
# __add__ (self, other)
print ('Point(1,2) + None', Point(1,2) + None)
print('Point(1, 1) + 5', Point(1, 1) + 5)
print('Point(1, 1) + (2, 3)', Point(1, 1) + (2, 3))
# how to create a similar point
print(p1) # __str__
# print(p1.__repr__()) # __str__ is the default implementation
p6 = eval(p1.__repr__())
print('p6', p6)
_p1 = Point(1, 3)
_p2 = Point(5, 9.9)
_lst = [_p1 , _p2]
print(_lst)
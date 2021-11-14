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
        if other is None or type(other) != type(self):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        # check
        return Point(...)

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
# p3 = p1 + p2
# how to create a similar point
print(p1) # __str__

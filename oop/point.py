class Point:
    def __init__(self, x, y):
        self.move(x, y)

    def reset(self):
        self.move(0, 0)

    def move(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x, p1.y)
print(p2.x, p2.y)

p = Point()
p.reset()
print(p.x, p.y)

p = Point()
Point.reset(p)
print(p.x, p.y)

point1 = Point()
point2 = Point()

point1.reset()
point2.move(5, 0)
print(point1.calculate_distance(point2))
assert point1.calculate_distance(point2) == point1.calculate_distance(point2)

point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))

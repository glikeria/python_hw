##############32#######################
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad

    def distance(self, x1,y1):
        distance = math.sqrt((self.x-x1)**2 + (self.y-y1)**2)
        return distance

    def in_circle(self, distance):
        self.distance = distance
        if distance < self.rad:
            print ("Point in circle")
        else:
            print ("Not in circle")

p = Point(38,56)
c = Circle(4,4,6)

c.in_circle(c.distance(p.x, p.y))

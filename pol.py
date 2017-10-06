from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getAngle(origin, p1, p2):
    sol = atan2((origin.y - p2.y), (origin.x - p1.x))
    return sol if sol > 0 else -sol


ori = Point(5, 7)
poly = [Point(6, 5), Point(4, 5), Point(6, 3), Point(4, 4)]

acum = 0

for i in range(len(poly)-1):
    acum += getAngle(ori, poly[i], poly[i+1])

print(acum)

if acum >= 2*pi:
    print("In")
else:
    print("Out")

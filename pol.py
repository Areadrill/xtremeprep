class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getAngle(origin, p1, p2):
    return (origin.x - p2.x)/(origin.y - p1.y)


ori = Point(5, 5)
p1 = Point(2, 1)
p2 = Point(3, 1)

print(getAngle(ori, p1, p2))

import math

class Circle:
    def __init__(self,_radius):
        self.radius = _radius

    def findArea(self):
        area = math.pi*self.radius*self.radius
        return area


if __name__ == "__main__":

    r = float(raw_input("Give the radius of the circle"))

    c = Circle(r)
    print "Area of the circle is ", c.findArea()

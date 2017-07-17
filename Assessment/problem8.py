import math

class Circle:
    def __init__(self,_radius):
        self.radius = _radius

    def __add__(self,cir):
        return Circle(self.radius+cir.radius)


if __name__ == "__main__":

    r1 = float(raw_input("Give the radius of the 1st circle"))
    r2 = float(raw_input("Give the radius of the 2nd circle"))

    c1 = Circle(r1)
    c2 = Circle(r2)

    c3 = c1+c2
    print "Radius of the third circle is ", c3.radius


from abc import ABC, abstractmethod
import math
import turtle
class shape(ABC): #shape is an abstract base class
    _sides = 0
    _area = 0
    _perimeter = 0
    @abstractmethod
    def getarea(self):
        pass
    @abstractmethod
    def getperimeter(self):
        pass 
    @abstractmethod
    def draw_shape(self): 
        pass
class rectangle(shape):
    def __init__(self, side1, side2):
        self._side1 = side1
        self._side2 = side2
        self._sides = 4
    def getarea(self):
        self._area = (self._side1*self._side2)
        print("Area = {}".format(self._area))
    def getperimeter(self):
        self._perimeter = 2*(self._side1+self._side2)
        print("Perimeter = {}".format(self._perimeter))
    def draw_shape(self):
        t = turtle
        t.forward(self._side1)
        t.left(90)
        t.forward(self._side2)
        t.left(90)
        t.forward(self._side1)
        t.left(90)
        t.forward(self._side2)
        t.left(90)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

class square(rectangle):
    def __init__(self, side1):
        self._side1 = side1
        self._side2 = side1

class triangle(shape):
    def __init__(self, side1, side2, side3, angle1, angle2):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        self._angle1 = angle1
        self._angle2 = angle2
        self._sides = 3
    def getperimeter(self):
        self._perimeter = self._side1 + self._side2 + self._side3
        print("Perimeter = {}".format(self._perimeter))
    def getarea(self):
        sp = (self._side1 + self._side2 + self._side3)/2
        self._area = math.sqrt((sp)*(sp-self._side1)*(sp-self._side2)*(sp-self._side3))
        print("Area = {}".format(self._area))
    def draw_shape(self):
        t = turtle
        t.forward(self._side1)
        t.left(2*self._angle1)
        t.forward(self._side2)
        t.left(2*self._angle2)
        t.forward(self._side3)
        t.done()
        try:
            t.exitonclick()
        except:
            pass
class rhombus(rectangle):
    def __init__(self, diag1, diag2):
        self.diag1 = diag1
        self.diag2 = diag2
        self._side1 = (self.diag1**2 + self.diag2**2)**(0.5)/2
        self._side2 = (self.diag1**2 + self.diag2**2)**(0.5)/2

    def getarea(self): #function overriding
        self._area = (0.5*self.diag1*self.diag2)
        print("Area = {}".format(self._area))

    def draw_shape(self):
        side = self._side1
        angle1 = math.acos(((side**2)*2 - self.diag1**2)/(2*side*side))
        angle1 = math.degrees(angle1)
        angle2 = (360 - 2*angle1)/2
        t = turtle
        t.forward(side)
        t.right(angle1)
        t.forward(side)
        t.right(angle2)
        t.forward(side)
        t.right(angle1)
        t.forward(side)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

class parallelogram(rectangle):
    def __init__(self, side1, side2, angle1):
        self._side1 = side1
        self._side2 = side2
        self._angle1 = angle1

    def draw_shape(self):
        t = turtle
        t.forward(self._side1)
        t.left(self._angle1)
        t.forward(self._side2)
        t.left(180-self._angle1)
        t.forward(self._side1)
        t.left(self._angle1)
        t.forward(self._side2)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

class circle(shape):
    def __init__(self, radius):
        self._radius = radius
    def getarea(self):
        self._area = (math.pi*self._radius*self._radius)
        print("Area = {}".format(self._area))
    def getperimeter(self):
        self._perimeter = (2*(math.pi)*self._radius)
        print("Perimeter = {}".format(self._perimeter))
    def draw_shape(self):
        t = turtle
        t.circle(self._radius)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

class ellipse(shape):
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def getarea(self):
        self._area = (math.pi*self._a*self._b)
        print("Area = {}".format(self._area))
    def getperimeter(self):
        self._perimeter = ((math.pi)*(self._a + self._b))
        print("Perimeter(Crude Approximation) = {}".format(self._perimeter))
    def draw_shape(self):
        t = turtle
        t.right(45)
        for i in range(2):
            t.circle(self._a,90)
            t.circle(self._b,90)
        try:
            t.exitonclick()
        except:
            pass

class polygon(shape):
    def __init__(self, n, l):
        self._sides = n
        self._length = l
    def getarea(self):
        self._area = (math.pow(self._length,2)*self._sides)/(4*abs(math.tan(180/self._sides)))
        print("Area = {}".format(self._area))
    def getperimeter(self):
        self._perimeter = (self._sides*self._length)
        print("Perimeter = {}".format(self._perimeter))
    def draw_shape(self):
        t = turtle
        for i in range(self._sides): 
            t.forward(self._length) 
            t.right(360 / self._sides)
        t.done()
        try:
            t.exitonclick()
        except:
            pass            		
r = rectangle(100, 200)
r.draw_shape()
s = square(100)
s.draw_shape()
t = triangle(100, 100, 100, 60, 60)
t.draw_shape()
r = rhombus(250,200)
r.draw_shape()
p = parallelogram(200, 100, 60)
p.draw_shape()
c = circle(100)
c.draw_shape()
e = ellipse(100, 50)
e.draw_shape()
p = polygon(6, 100)
p.draw_shape()
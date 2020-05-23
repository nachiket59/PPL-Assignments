#Base class
import turtle
class Shapes:
    def __init__(self):
        self._Type = '' #Protected member

    def get_Type(self):
        print(self._Type)

#Triangle
class triangle(Shapes):
    def __init__(self):
        self._side = 3
        self._side_length = 30
    #We can modify protected members via base class    
    def set_type(self):
        self._Type = 'Polygon with 3 sides'
    #Only member functions can have access to private members    
    def get_side(self):
        print(self._side)
    def draw(self):
        t = turtle
        for i in range(3):
            t.forward(self._side_length)
            t.left(120)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

#Equilateral traingle inherited from triangle
class equilateral(triangle):
    #We can modify protected members via base class    
    def set_type(self):
        self._Type = 'Polygon with 3 sides and all three are equal'
    #Only member functions can have access to private members    
    def get_side(self):
        print(self._side)
    def draw(self):
        t = turtle
        for i in range(3):
            t.forward(self._side_length)
            t.left(120)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

#Rectangle
class rectangle(Shapes):
    def __init__(self):
        self.__side = 4
        self._a = 40
        self._b = 50
    def set_sides(self,a,b):
        self._a = a
        self._b = b   
    #We can modify protected members via base class    
    def set_type(self,typ):
        self._Type = 'Polygon with 2 equal and 2 unequal sides'
    #Only member functions can have access to private members    
    def get_side(self):
        print(self.__side)
    def draw(self):
        t = turtle
        t.forward(self._a)
        t.left(90)
        t.forward(self._b)
        t.left(90)
        t.forward(self._a)
        t.left(90)
        t.forward(self._b)
        t.left(90)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

#Square inherited from rectangle
class square(rectangle):
    def __init__(self):
        self.set_sides(40,40)
    #We can modify protected members via base class    
    def set_type(self):
        self._Type = 'Polygon with 4 sides all of which are equal'

#Rhombus inherited from square
class rhombus(square):
    def set_type(self):
        self._Type = 'Polygon with 4 sides all of which are equal but angles are not 90'

    def draw(self):
        t = turtle
        t.forward(self._a * 2)
        t.left(60)
        t.forward(self._b * 2)
        t.left(120)
        t.forward(self._a * 2)
        t.left(60)
        t.forward(self._b * 2)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

#Circle
class circle(Shapes):
    def __init__(self):
        self.f = 0
        self.__r = 0
        self.__eqn = 'x^2 + y^2 = r^2'
    def set_type(self):
        self._Type = 'Conic'
    #Setter function for accessing private member
    def set_radius(self,r):
        self.__r = r
        self.f = self.__r
    def get_area(self):
        print(3.14 * (self.__r)**2)
    def draw(self):
        t = turtle
        t.circle(self.f)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

#Ellipse
class ellipse(Shapes):
    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__eqn = 'x^2/a^2 + y^2/b^2 = 1'
    def set_type(self):
        self._Type = 'Conic with a major and minor axis'
    #Setter function for accessing private member
    def set_params(self,a,b):
        self.__a = a
        self.__b = b
    def get_area(self):
        print(3.14 * self.__a * self__b)
    def draw(self):
        t = turtle
        t.right(45)
        for i in range(2):
            t.circle(self.__a,90)
            t.circle(self.__b,90)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

class flower(Shapes):
    def drawflower(self):
        t = turtle
        for i in range(8):
            t.circle(60)
            t.left(45)
        t.done()
        try:
            t.exitonclick()
        except:
            pass
#driver code
triangle().draw()
equilateral().draw()

rectangle().draw()
square().draw()
rhombus().draw()

c = circle()
c.set_radius(20)
c.draw()
e = ellipse()
e.set_params(30,80)
e.draw()




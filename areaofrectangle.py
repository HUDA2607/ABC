<<<<<<< HEAD
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print("Dimension of Rectangle - Length : %d Width : %d" % (newRectangle.length, newRectangle.width))
=======
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print("Dimension of Rectangle - Length : %d Width : %d" % (newRectangle.length, newRectangle.width))
>>>>>>> 3920a7233fe64405a628e1fc7cc9ed6f85077a04
print("Area of Rectangle :", newRectangle.rectangle_area())
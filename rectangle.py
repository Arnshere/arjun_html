class Restangle():
    def __init__(self,l, w):
        self.lentgth = l
        self.width = w
    
    
    def rectangle_area(self):
        return self.length*self.width
    
    
    
newRectangle = Rectangle(12, 10)
print("Dimension of Rectangle - length : %d Width : %d" % (newRectangle.length,
newRectangle.width))
print("Area of rectangle :", newRectangle.rectangle_area)
    
    
    
    
    
    
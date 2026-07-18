class circle:
    PI = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        
    def Accept(self):
        self.Radius = float(input("Enter Radius :"))
        
    def CalculateArea(self):
        self.Area = circle.PI * self.Radius * self.Radius
        
    def CalculateCircumference(self):
        self.Circumference = 2 * circle.PI * self.Radius
        
    def Display(self):
        print("Radius is :", self.Radius)
        print("Area of circle is :",self.Area)
        print("Circumference of circle is :",self.Circumference)
        
obj1 = circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2 = circle()
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
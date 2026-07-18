class Arithmetic:
    
    def __init__(self):
        
        self.Value1 = 0
        self.Value2 = 0
        
    def Accept(self):
        self.Value1 = int(input("Enter first number :"))
        self.Value2 = int(input("Enter second number :"))
        
    def Addition(self):
        return self.Value1 + self.Value2 
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not possible"
        else:
            return self.Value1 / self.Value2
    
    def Display(self):
        print("Addition is :", self.Addition())
        print("Substraction is :", self.Substraction())
        print("Multiplication is :", self.Multiplication())
        print("Division is :", self.Division())
    
obj1 = Arithmetic()
obj1.Accept()
obj1.Display()

print()

obj2 = Arithmetic()
obj2.Accept()
obj2.Display()
    
    
    
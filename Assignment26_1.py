class Demo:
    value = 11
    
    def __init__(self , No1 , No2):
        self.No1 = No1
        self.No2 = No2
        
    def Fun(self):
        print("inside Instance method name as Fun")
        print(self.No1)
        print(self.No2)
        
    def Gun(self):
        print("inside Instance Method name as Gun")
        print(self.No1)
        print(self.No2)
        
obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
    
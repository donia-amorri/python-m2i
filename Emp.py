class Emp: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
      
    def info(self): 
        print("Hello, % s. You are % s old." % (self.name, self.age)) 
  
Emps = [Emp("John", 43), 
    Emp("Hilbert", 16), 
    Emp("Alice", 30)] 
  
for emp in Emps: 
    emp.info()
#exemple orienté objet
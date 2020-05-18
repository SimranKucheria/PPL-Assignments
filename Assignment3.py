class rectangle:
    def __init__(self):
        self.name="abc"
        self.length=0
        self.breadth=0
        self.areas=0.0

    def inpt(self):
        self.name=input("Enter type of shape")
        self.length=input("Enter length")
        self.breadth=input("Enter breadth")
        self.areas=int(self.length) * int(self.breadth)
  
    def area(self):
      print ("The shape",self.name,"occupies ",self.areas,"m^2")

class square:
    def __init__(self):
        self.name="abc"
        self.side=0
        self.areas=0.0

    def inpt(self):
        self.name=input("Enter type of shape")
        self.side=input("Enter side")
        self.areas=int(self.side) * int(self.side)
  
    def area(self):
      print ("The shape",self.name,"occupies ",self.areas,"m^2")

class triangle:
    def __init__(self):
        self.name="abc"
        self.height=0
        self.base=0
        self.areas=0.0

    def inpt(self):
        self.name=input("Enter type of shape")
        self.heigth=input("Enter height")
        self.base=input("Enter base")
        self.areas=int(self.height) * int(self.base)*0.5
  
    def area(self):
      print ("The shape",self.name,"occupies ",self.areas,"m^2")

class circle:
    def __init__(self):
        self.name="abc"
        self.radius=0
        self.areas=0.0

    def inpt(self):
        self.name=input("Enter type of shape")
        self.radius=input("Enter radius")
        self.areas=int(self.radius) *int(self.radius)*3.14
  
    def area(self):
      print ("The shape",self.name,"occupies ",self.areas,"m^2")

class cat:
    def __init__(self):
        self.name="abc"
        self.legs=0
        self.trunk="abc"

    def inpt(self):
        self.name=input("Enter name")
        self.legs=input("Enter number of legs")
        self.trunk=input("Does animal have a trunk? Reply in has a or no")
    def info(self):
      print ("The cat named",self.name,"has",self.legs,"legs and",self.trunk,"trunk")

class elephant:
    def __init__(self):
        self.name="abc"
        self.legs=0
        self.trunk="abc"

    def inpt(self):
        self.name=input("Enter name")
        self.legs=input("Enter number of legs")
        self.trunk=input("Does animal have a trunk? Reply in has a or no")
    def info(self):
      print ("The elephant named",self.name,"has",self.legs,"legs and",self.trunk,"trunk")

class dog:
    def __init__(self):
        self.name="abc"
        self.legs=0
        self.trunk="abc"

    def inpt(self):
        self.name=input("Enter name")
        self.legs=input("Enter number of legs")
        self.trunk=input("Does animal have a trunk? Reply in has a or no")
    def info(self):
      print ("The dog named",self.name,"has",self.legs,"legs and",self.trunk,"trunk")

class snake:
    def __init__(self):
        self.name="abc"
        self.legs=0
        self.trunk="abc"

    def inpt(self):
        self.name=input("Enter name")
        self.legs=input("Enter number of legs")
        self.trunk=input("Does animal have a trunk? Reply in has a or no")
    def info(self):
      print ("The snake named",self.name,"has",self.legs,"legs and",self.trunk,"trunk")

class eagle:
    def __init__(self):
        self.name="abc"
        self.legs=0
        self.beak="abc"

    def inpt(self):
        self.name=input("Enter name")
        self.legs=input("Enter number of legs")
        self.beak=input("Does animal have a beak? Reply in has a or no")
    def info(self):
      print ("The eagle",self.name,"has",self.legs,"legs and",self.beak,"beak")

s1=cat()
s1.inpt()
s1.info()

s2=circle()
s2.inpt()
s2.area()





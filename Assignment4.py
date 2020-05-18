class shape(object):
    def __init__(self,x,y):
        self.height=int(x)
        self.breadth=int(y)

class Square(shape):
    def __init__(self,x,y):
        shape.__init__(self,x,y)
    def calc(self):
        print("Area is", shape.height * shape.height)
class Triangle(shape):
    def __init__(self,x,y):
        shape.__init__(self,x,y)
    def calc(self):
        print("Area is", self.height * self.breadth * 0.5)
class Rectangle(shape):
    def __init__(self,x,y):
        shape.__init__(self,x,y)
    def calc(self):
        print("Area is", self.height * self.breadth)

class animal(object):
    def __init__(self,x,y):
        self.name=x
        self.legs=int(y) 
      
class cat(animal):
    def __init__(self,x,y):
        animal.__init__(self,x,y)
  
    def info(self):
      print ("The cat named",self.name,"has",self.legs,"legs")

class dog(animal):
    def __init__(self,x,y):
        animal.__init__(self,x,y)

    def info(self):
      print ("The dog named",self.name,"has",self.legs,"legs")

class elephant(animal):
    def __init__(self,x,y):
        animal.__init__(self,x,y)

    def info(self):
      print ("The elephant named",self.name,"has",self.legs,"legs")


class snake(animal):
    def __init__(self,x,y):
        animal.__init__(self,x,y)

    def info(self):
      print ("The snake named",self.name,"has",self.legs,"legs")

class eagle(animal):
    def __init__(self,x,y):
        animal.__init__(self,x,y)
    def info(self):
      print ("The eagle named",self.name,"has",self.legs,"legs")


x=input("Enter height")
y=input("Enter breadth")
s1=Rectangle(x,y)
s1.calc()
x=input("Enter name of eagle")
y=input("Enter number of legs")
s2=eagle(x,y)
s2.info()






 







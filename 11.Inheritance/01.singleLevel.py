class Parent:
    name = 'Parent'

    def getName1(self):
        print(f"name:{self.name}")


class Child(Parent):
    
    def __init__(self, companyName):
     self.companyName = companyName;
    def getName(self):
      print(f"{self.companyName}")
        


object = Child(True)
object.getName()

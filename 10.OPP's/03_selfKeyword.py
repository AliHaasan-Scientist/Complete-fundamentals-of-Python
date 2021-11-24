# The self parameter is a reference to the current instance of the class
class Employee:
    companyName = "Nasa"
# This is Method of a class:

    def getData(self):
        print(
            f"Your name is {self.name} and you are working in {self.companyName}")


# ali is an objec0
ali = Employee()
ali.name = "Ali Hasan"
ali.getData()
# is same as using Employee.getData(ali);
#  hussan object
hussan = Employee()
hussan.name = "Muhammad Hussan"
hussan.getData()

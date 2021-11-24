class Scientist:
    companyName = "NeuaraLink"
    salary = "10000$"
    location = "America"  # class attribute.
# chang the value of class attribute.
    # def updateSalary(self,sel):
    #     self.__class__.salary = sel
# Alternative
    @classmethod
    def updateSalary(cls,sel):
         cls.salary = sel

ali = Scientist()

ali.updateSalary("200000$")
print(ali.salary)

print(Scientist.salary)

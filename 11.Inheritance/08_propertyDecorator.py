class Employee:
    companyName = "Nasa"
    salary = 5000
    salaryBonus = 500
    #totalSalary = salary+salaryBonus

    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus


e1 = Employee()
print(e1.totalSalary)
e1.totalSalary = 5600
   
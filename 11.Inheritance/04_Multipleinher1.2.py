class Employee:
    company = 'Microsoft ("_")'
    ecode = 120


class Freelance:
    company = 'Fiver'
    level = 0

    def updateLevel(self):
        self.level = self.level+1


class Progrmmer(Employee, Freelance):
    name = "Anonymouse"


e1 = Progrmmer()
e1.updateLevel()
e1.updateLevel()
e1.updateLevel()
print(e1.level)
print(e1.company)

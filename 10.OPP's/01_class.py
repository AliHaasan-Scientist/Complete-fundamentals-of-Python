class Employee:
    companyName: "Nasa"

    def getData(self, name, id):
        self.name = name
        self.id = id


ali = Employee()
ali.getData("Ali Hasan", 1)
print(ali.id)
print(ali.name)

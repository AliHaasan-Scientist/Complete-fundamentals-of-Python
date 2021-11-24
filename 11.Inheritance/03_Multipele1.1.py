class Product:
    company = " HP Accesories"

    def __init__(self, productName):
        self.productName = productName

    def show(self):
        print(f"product:{self.productName}")


hp = Product("Hp Compaq 6005")
hp.show()
# Derived Class


class Dell(Product):
   pass


dellP = Dell("Dell dual core")
dellP.show()



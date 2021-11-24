class Calculator:
    name = "simple Calculator"

    def square(self, value):
        return print(f"Square is {value**2}")

    def cube(self, value):
        return print(f"cube is {value**3}")
    def SquareRoot(self, value):
        return print(f"Squareroot is {value**.5}")


calclu1 = Calculator()
calclu1.square(3)
calclu1.cube(3)
calclu1.SquareRoot(1)
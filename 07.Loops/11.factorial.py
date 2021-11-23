fac = int(input("Enter a number"))

for i in range(1, fac):
    fac *= i
    i = i+1
print(f"{fac}!")

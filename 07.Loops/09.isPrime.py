num = int(input("Enter a number"))
for i in range(2, num):
    prime = True
    if (num % i == 0):
        prime = False
if prime:
    print("Is Prime")
else:
    print("Not a prime number")

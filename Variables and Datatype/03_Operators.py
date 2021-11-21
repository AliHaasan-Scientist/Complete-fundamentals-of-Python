#Operators in python
# Arithmatic Operator +,-,*,/
# add two integars
a = 20;
b = 10;
sum = a+b
subtration = a-b
product = a*b;
division = a/b;
print("sum is:", sum, "Diffrence is: ", subtration,
      "Multiplication is:", product, "Division is: ", division);
# Assignment Operator , =,+=,-=,/=,*=
a = 10;
b = 20;
temp = a;
a = b;
b = temp;
print(a, b);
#
a = 2;
a += 2;
print(a);
b -= 2;
print(b);
# Comperson Operator; And ,Or , NOT
a = 3;
b = 3;
c = 2;
equal = a == b;
print(equal);
lessthan = c < a;
print(lessthan)
greatethan = a > c;
print(greatethan)
# Logical Operators
andOperator = equal and lessthan;
print(andOperator)
orOpreator = equal and greatethan;
print(orOpreator);
null =equal or None;
print(null);
letter='''
Name:|name|
Date:|date|
dear principle,
i have applied in Bs Program.
:
:
:
:
:
Address:|address|

'''
name=input("Enter name:")
date=input("Enter Date:")
address=input("Enter Address:")


letter=letter.replace("|name|", name);
letter=letter.replace("|date|", date);
letter=letter.replace("|address|", address);
print(letter)


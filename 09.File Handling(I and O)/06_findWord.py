with open('09.File Input & Output\poem.txt', 'r') as f:
    a = f.read()
    print(a)
    if('twinkle' in a):
        find = True
    else:
        find = False
if find:
    print(" word is find")
else:
    print("word is not find")

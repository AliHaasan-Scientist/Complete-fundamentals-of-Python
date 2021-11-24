with open('09.File Input & Output\sample.txt', 'r') as f:
    a = f.read()
    with open('09.File Input & Output\sample.txt', 'w') as f:
        a = f.write("new text")
    print(a)

def greatNum(n1, n2, n3):
    if(n1 > n2):
        if(n1 > n3):
            n = n1
        else:
            n = n2
    if(n2 > n3):
        if(n2 > n1):
         n = n2
    else:
         n = n3
    return n


print(greatNum(400, 120, 100))

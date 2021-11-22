dicitonary = {
    "pankha": "Fan",
    "rotii": "bread",
    "bijli": "Electricity",
}
print("Find the meaning:", dicitonary.keys())
values = input("Input the word for meaning\n")
print("Your meaning is :", dicitonary.get(values))

# Dicitonary Methods
myDict = {
    "name": "Ali Hasan",
    "rollNum": 123,
    "cellNum": "03088741683",
    "age": 19,
    "class": "BS IT",
    "friendList": ["Ahmad", "Waqas", "Abdullah", "Hussan"],
"nestedDic":{
    "Univeristy":"BZU",
    "field":"Sciences",

}
}
#keys method
print(tuple(myDict.keys()))
#values method
print(myDict.values());
print(myDict.items());
#update method
updatedDic={
    "id":1
}
myDict.update(updatedDic);
print(myDict);
print(myDict.get("name"));
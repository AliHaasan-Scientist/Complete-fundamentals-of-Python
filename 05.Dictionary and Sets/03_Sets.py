myset = {1, 1, 2, 3, 4, 5}
print(myset)
# make an empty
emptySet = set()
print(emptySet)
# add items in Eset
emptySet.add(2)
print(emptySet)
# can we add list in set acctualy not i.e
# emptySet.add([1,2,4])
emptySet.add((1, 2, 4))
print(emptySet)
# can we dictonary in set Ans not becuse dic is mutable
# emptySet.add({"name":"ali"})
print(len(emptySet))
emptySet.remove(2)
print(emptySet)
print(emptySet.pop())
#uniou in sets
myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = myset.intersection({2, 10, 23, 12, 5})
b = myset.union({2, 10, 23, 12, 5})
print("This is intersection", a)
print("This is union of elements", b)

a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9, 10}

result = a.difference(b)
print(result)


result = a.intersection(b)
print(result)

result = a.union(b)
print(result)

result = a.symmetric_difference(b)
print(result)

result = a.symmetric_difference_update(b)
print(a)



print(a.isdisjoint(b))
print(a.issubset(b))
print(b.issubset(a))
print(a.issuperset(b))
print(b.issuperset(a))

data = {"White", "Black", "Yellow", "Green", "Red", "Blue"}
print(data)
data.remove("Yellow")
print(data)
data.pop()
print(data)

data.update(["Pink", "Jasmine"])
print(data)

data.add("Orange")
print(data)

data.discard("Jasmine")
print(data)
data.discard("Peach")

data.clear()
print(data)

a = set({1,2,3,4,5,6})
print(a)

names = {"John", "Sam", "Jason", "Mary"}
print(names)
names.add("Simon")
print(names)
names.update({"James", "David"})
print(names)
names.remove("James")
print(names)
names.discard("Jordon")
print(names)
names.clear()
print(names)


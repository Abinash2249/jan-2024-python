a = ()
b = tuple()
vowels = ("a", "e", "u", "i", "o", "u")
print(vowels[:2])
print(vowels.index("u",4,6))
print(vowels.index("u"))

print(vowels[2:4])


x = (1, 2, 3)
y = (4, 5, 6)

print(x+y)
print(x*2)

print(max(1,2,3,4,5))
print(min(4,5,6,7,1))
print(sum({1,2,3}))

data = sorted([1,3,2,8,6], reverse=True)
print(list(data))


student1 = {"name": "Jason", "address": "Baneshwor"}
name = student1["name"]
print(name)

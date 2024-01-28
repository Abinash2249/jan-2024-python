# WAP to print even numbers in the range of 0 to 50

print(list(range(0,51,2)))

num = 51
num2 = range(num)

for i in range(0,51):
    if i % 2 == 0:
        print(i)


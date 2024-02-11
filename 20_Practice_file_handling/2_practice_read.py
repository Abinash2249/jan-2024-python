

fp = open("message.txt", "r")
content = fp.read()
fp.close()
print(content)



fp = open("message.txt", "r")

try:
    content = fp.read()
except:
    print("Something went wrong.")
else:
    print(content)
finally:
    fp.close()



with open("message.txt", "r") as fp:
    content = fp.read()

print(content)

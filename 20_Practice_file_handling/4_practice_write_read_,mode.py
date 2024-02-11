

with open("message.txt", "w+") as fp:
    fp.write("Hello, this is write read mode in Python")
    content = fp.read()

print("Successful")

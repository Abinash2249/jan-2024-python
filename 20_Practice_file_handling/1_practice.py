


fp = open("message.txt", "w")
fp.write("Hello, I am learning file handling.")
fp.close()
print("Successful")



fp = open("message.txt", "w")

try:
    fp.write("Hello, I am learning file handling in python.")
except:
    print("Failed")
else:
    print("Successful")
finally:
    fp.close()
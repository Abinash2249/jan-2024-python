
with open("message.txt", "r+") as fp:
    content = fp.read()
    new_content = content[1:7]
    fp.seek(0)
    fp.write(new_content)

print("Successful")

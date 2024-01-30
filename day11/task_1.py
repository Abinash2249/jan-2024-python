# WAP to delete all the occurrences of a specified character in a given string
# S = “All the occurrences of a specified character in a given string”
# Input = “a”
# Output = “ll occurrences of  specified chracter in  given string”

S = "All the occurrences of a specified character in a given string"
result = ""
char = input("Enter a letter: ")
for each in S:
    if each.lower() == char.lower():
        continue
    result += each      # string concatenation
print(result)       # ll the occurrences of  specified chrcter in  given string



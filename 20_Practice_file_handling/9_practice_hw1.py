
# Write the above list in a binary file "student.dat"



import pickle

students = ["Jon", "Jane", "Hary", "Alex"]

with open("student.dat", "wb") as fp:
    pickle.dump(students, fp)

print("Successful")



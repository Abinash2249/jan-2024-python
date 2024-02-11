# Read the binary file and create a dictionary with information of student and their respective exam marks
# Finally write the info again to the binary file "marks.dat"


import pickle

with open("student.dat", "rb") as fp:
    student_list = pickle.load(fp)
print(student_list)

student_marks_dict = {
    "Jon": 89,
    "Jane": 93,
    "Hary": 78,
    "Alex": 75
}


with open("student.dat", "wb") as fp:
    pickle.dump(student_marks_dict, fp)

with open("student.dat", "rb") as fp:
    result = pickle.load(fp)
print(result)



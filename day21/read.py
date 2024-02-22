from day21 import create
import json
FILENAME = "students.json"


def read_student():
    student_id = input("Enter student id: ")
    with open(FILENAME, "r") as fp:
        students = json.loads(fp.read())
        filtered_student = list(filter(lambda student: student["id"] == student_id, students))
        if filtered_student:
            print(filtered_student[0])
        else:
            print("Invalid student id.")
    want_to_continue = input("Do you want to continue? (y/n): ")
    return True if want_to_continue.lower() == "y" else False

    # def read_student():
    #     student_id = input("Enter student id: ")
    #     with open(FILENAME, "r") as fp:
    #     for student in students:
    #         if student["id"] == student_id:
    #             print(f"The information for the id {student['id']} is {student}")
    #             break
    #     else:
    #         print("Student of the id you provided does not exist.")
    # want_to_continue = input("Do you want to continue? (y/n): ")
    # return True if want_to_continue.lower() == "y" else False
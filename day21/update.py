import json

FILENAME = 'students.json'
from day21 import create


def update_student():
    id = input("Enter the id of the student, whose information you want to update: ")
    which_info = input("which information do you wish to change: ")
    new_info = input(f"Enter the new {which_info} to be added: ")
    which_info = which_info.lower()
    new_info = new_info.lower()
    with open(FILENAME, "r+") as fp:
        students = json.loads(fp.read())
        filtered_student = list(filter(lambda student: student["id"] == id, students))
        if filtered_student:
            filtered_student[0][which_info] = new_info
        else:
            print("Invalid id")
            want_to_continue = input("Do you want to continue? (y/n): ")
            return True if want_to_continue.lower() == "y" else False
        # for student in students:
        #     if student["id"] == id:
        #         student[which_info] = new_info
        #         break
        # else:
        #     print("Invalid student id.")
        fp.seek(0)
        fp.write(json.dumps(students, indent=2))
    print("Student updated.")
    want_to_continue = input("Do you want to continue? (y/n): ")
    return True if want_to_continue.lower() == "y" else False
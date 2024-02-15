import json
from day21 import create

FILENAME = "students.json"
def delete_student():
    id = input('Enter the student id, that you want to delete: ')
    with open(FILENAME, "r") as fp:
        students = json.loads(fp.read())
        for student in students:
            if student["id"] == id:
                students.remove(student)
                break
        else:
            print("Invalid student id.")
            want_to_continue = input("Do you want to continue? (y/n): ")
            return True if want_to_continue.lower() == "y" else False
    with open(FILENAME, "w") as fp:
        fp.write(json.dumps(students))

    print("Student deleted successfully !!")
    want_to_continue = input("Do you want to continue? (y/n): ")
    return True if want_to_continue.lower() == "y" else False


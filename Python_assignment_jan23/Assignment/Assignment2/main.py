
from Assignment.Assignment2.read import read
from Assignment.Assignment2.insert import insert
from Assignment.Assignment2.update import update
from Assignment.Assignment2.delete import delete

def crud_student():
    selection = input("Enter your choice (i/r/u/d/e): ")
    selection = selection.lower()

    def exit_message():
        print("Thank you. See you again !!")

    if selection == "i":
        cont = insert()
        crud_student() if cont else exit_message()
    elif selection == "r":
        cont = read()
        crud_student() if cont else exit_message()
    elif selection == "u":
        cont = update()
        crud_student() if cont else exit_message()
    elif selection == "d":
        cont = delete()
        crud_student() if cont else exit_message()
    else:
        exit_message()

if __name__ == "__main__":
    crud_student()


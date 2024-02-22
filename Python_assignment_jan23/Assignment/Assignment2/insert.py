from estd_connection import estd_connection

def insert():

    cursor = estd_connection()

    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student's age: "))
    address = input("Enter student's address: ")

    sql = f"""
    INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS) VALUES ('{id}', '{name}', '{age}', '{address}')
    """

    cursor.execute(sql)
    print("Student added successfully !!")
    want_to_continue = input("Do you want to continue? (y/n): ")
    return True if want_to_continue.lower() == "y" else False


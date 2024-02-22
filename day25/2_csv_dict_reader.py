

import csv

def estd_connection():
    import psycopg2     # psycopg2
    conn = psycopg2.connect(
        database = "studenttestdb",
        user = "postgres",
        password = "4321",
        host = "127.0.0.1",
        port= 5432
    )
    conn.autocommit = True
    print("Connection established successfully !!")
    cursor = conn.cursor()
    return cursor


cursor = estd_connection()
filename = "students.csv"

with open(filename, "r") as cr:
    students = csv.DictReader(cr)
    # # print(students)
    # print(list(students))
    for student in students:
        name = student["name"]
        id = student["id"]
        age = student["age"]
        address = student["address"]
        sql = f"""
        INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS) VALUES ('{id}', '{name}', '{age}', '{address}')
        """
        cursor.execute(sql)
        
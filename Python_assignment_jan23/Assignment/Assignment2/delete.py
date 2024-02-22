from estd_connection import estd_connection

def delete():
    cursor = estd_connection()
    id = input("Enter student id: ")

    sql = f"""
    DELETE FROM STUDENT WHERE ID='{id}'
    """

    cursor.execute(sql)
    print("Student Deleted Successfully")
    want_to_continue = input("Do you want to continue? (y/n): ")
    return True if want_to_continue.lower() == "y" else False

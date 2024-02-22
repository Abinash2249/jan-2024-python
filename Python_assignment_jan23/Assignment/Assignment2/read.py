from estd_connection import estd_connection

def read():
    cursor = estd_connection()
    id = input("Enter student ID: ")

    sql = f"""
    SELECT * FROM STUDENT WHERE ID = '{id}'
    """

    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    want_to_continue = input("Do you want to continue? (y/n): ")
    return True if want_to_continue.lower() == "y" else False


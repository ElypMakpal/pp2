import psycopg2
import csv
from tabulate import tabulate


conn = psycopg2.connect(
    host="localhost",
    dbname="lab 10",
    user="postgres",
    password="Aktau1106",
    port=5432
)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
)
""")
conn.commit()



def insert_data():
    method = input('Type "csv" or "con" to insert from CSV file or console: ').lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    elif method == "csv":
        path = input("Enter CSV file path: ")
        try:
            with open(path, 'r') as f:
                reader = csv.reader(f)
                next(reader)  
                for row in reader:
                    if len(row) == 3:
                        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", row)
        except Exception as e:
            print("Error reading CSV:", e)
    conn.commit()

def update_data():
    column = input("Column to update (name/surname/phone): ").lower()
    old_val = input(f"Current {column}: ")
    new_val = input(f"New {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_val, old_val))
    conn.commit()

def delete_data():
    phone = input("Phone number to delete: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

def query_data():
    column = input("Search by column (name/surname/phone): ").lower()
    value = input(f"Value of {column}: ")
    cur.execute(f"SELECT * FROM phonebook WHERE {column} = %s", (value,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='grid'))

def display_data():
    cur.execute("SELECT * FROM phonebook ORDER BY user_id")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))



while True:
    print("""
    List of the commands:
    1. Type "i" or "I" in order to INSERT data to the table.
    2. Type "u" or "U" in order to UPDATE data in the table.
    3. Type "q" or "Q" in order to make specific QUERY in the table.
    4. Type "d" or "D" in order to DELETE data from the table.
    5. Type "s" or "S" in order to see the values in the table.
    6. Type "f" or "F" in order to close the program.
    """)

    cmd = input(">>> ").lower()
    if cmd == "i":
        insert_data()
    elif cmd == "u":
        update_data()
    elif cmd == "q":
        query_data()
    elif cmd == "d":
        delete_data()
    elif cmd == "s":
        display_data()
    elif cmd == "f":
        break
    else:
        print("Unknown command. Please try again.")


cur.close()
conn.close()

import sqlite3
import time

# Admin data base
conn=sqlite3.connect("admin.db")
c=conn.cursor()

def add_admin():
    username=input("Enter the username to be added: ")
    password=input("Enter the password corresponding to the enterd username: ")
    with conn:
        c.execute(
            """
            INSERT INTO credentials VALUES (:username,:password)
            """,{'username':username,'password':password}
        )
    print(username,"added successfully to the admin list")

add_admin()
time.sleep(2)
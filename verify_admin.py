import sqlite3
import time

# Admin data base
conn=sqlite3.connect("admin.db")
c=conn.cursor()

global verified
def verify_admin():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    with conn:
        c.execute(
            """
            SELECT username,password FROM credentials
            """
            )
        if((username,password) in c.fetchall()):
            print("You are logged in as an admin")
            return True
        else:
            print("Sorry, you have entered wrong credentials")
            time.sleep(2)
            return False

# if __name__=="__main__":
#     verified=verify_admin()
#     time.sleep(2)
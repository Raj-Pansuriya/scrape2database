import sqlite3
import time

# Admin data base
conn=sqlite3.connect("admin.db")
c=conn.cursor()

def remove_admin():
    username=input("Enter the username to be removed: ")
    choice=input("Are you sure you wnat to remove "+username+" from admin list? [y/N]: ")
    if(choice in ('y','Y')):
        with conn:
            try:
                c.execute(
                    """
                    DELETE FROM credentials WHERE username=:username
                    """,{'username':username}
                )
            except:
                print("The given username doesn't exist in the database...")
            else:
                print(username,"removed successfully from the admin list")

remove_admin()
time.sleep(2)
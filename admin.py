import sqlite3

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
            return True
        return False

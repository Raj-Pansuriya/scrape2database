import sqlite3
class User:
    def __init__(self,name):
        self.conn=sqlite3.connect("test.db")
        self.c=self.conn.cursor()
        self.name=name

    def display_all(self,table):
        if(table=="module_list"):
            self.c.execute(
                """
                SELECT "index",module FROM {}
                """.format(table)
            )
            for entry in self.c.fetchall():
                return "{:>3} | {}".format(entry[0],entry[1])
        else:
            try:
                self.c.execute(
                    """
                    SELECT "index",function_name FROM {}
                    """.format(table)
                )
                for entry in self.c.fetchall():
                    return "{:>3} | {}".format(entry[0],entry[1])
            except:
                return "The entered table is invalid"

    def get_by_name(self,name,table):
        if(table=="module_list"):
            self.c.execute(
                """
                SELECT module,source_code FROM {} WHERE module={}
                """.format(table,name)
            )
            return "{}    |    {}".format(self.c.fetchone()[0],self.c.fetchone()[1])
        else:
            try:
                self.c.execute(
                    """
                    SELECT function_name,function_usage FROM {} WHERE function_name={}
                    """.format(table,name)
                )
            except:
                return "No such function found in the database"

    def get_by_index(self,index,table):
        if(table=="module_list"):
            try:
                self.c.execute(
                    """
                    SELECT module,source_code FROM {} WHERE "index"={}
                    """.format(table,index)
                )
                return "{}"
            except:
                return "Please input a valid index"
        else:
            try:
                self.c.execute(
                    """
                    SELECT function_name,function_usage FROM {} WHERE "index"={}
                    """.format(table,index)
                )
            except:
                return "Please input a valid index"



class Admin(User):
    def __init__(self,name,password):
        self.conn=sqlite3.connect("test.db")
        self.c=self.conn.cursor()
        self.name=name

    def update(self,query):
        with self.conn:
            self.c.execute(query)

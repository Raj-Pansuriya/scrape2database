import sqlite3


conn=sqlite3.connect("test.db")
c=(conn).cursor()

def display_all(table):
    if(table=="module_list"):
        c.execute(
        """
            SELECT "index",module FROM {}
            """.format(table)
        )
        return c.fetchall()
    else:
        try:
            c.execute(
                """
                SELECT "index",function_name FROM {}
                """.format(table)
            )
            return c.fetchall()
        except:
            pass

def get_by_name(name,table):
    if(table=="module_list"):
        c.execute(
            """
            SELECT module,source_code FROM {} WHERE module={}
            """.format(table,name)
        )
        return c.fetchall()
    else:
        try:
            c.execute(
                """
                SELECT function_name,function_usage FROM {} WHERE function_name={}
                """.format(table,name)
            )
            return c.fetchall()
        except:
            return "No such function found in the database"

def get_by_index(index,table):
    if(table=="module_list"):
        try:
            c.execute(
                """
                SELECT module,source_code FROM {} WHERE "index"={}
                """.format(table,index)
            )
        except:
            return "Please input a valid index"
        else:
            return c.fetchall()
    else:
        try:
            c.execute(
                """
                SELECT function_name,function_usage FROM {} WHERE "index"={}
                """.format(table,index)
            )
        except:
            return "Please input a valid index"
        else:
            return c.fetchall()

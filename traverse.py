import sqlite3
import textwrap


conn=sqlite3.connect("test.db")
c=(conn).cursor()

def display_all(table):
    if(table=="module_list"):
        c.execute(
        """
            SELECT module FROM {}
            """.format(table)
        )
        return [str(i[0]) for i in c.fetchall()]
    else:
        try:
            c.execute(
                """
                SELECT function_name FROM {}
                """.format(table)
            )
            return [i[0] for i in c.fetchall()]
        except:
            pass

def get_by_name(name,table):
    if(table=="module_list"):
        c.execute(
            """
            SELECT source_code FROM module_list WHERE module=:module
            """,{'module':name}
        )
        return c.fetchall()[0][0]
    else:
        try:
            c.execute(
                f"""
                SELECT function_usage FROM {table} WHERE function_name =:function_name
                """,{'function_name':name}
            )
            return textwrap.fill(c.fetchall()[0][0],70)
        except:
            return "No such function found in the database"

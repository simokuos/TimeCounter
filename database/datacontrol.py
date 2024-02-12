import sqlite3
from .database_config import *

class datacontrol:

    connection = sqlite3.connect("{}{}".format(DATABASE['file_path'],DATABASE['name']))
    cursor = connection.cursor()

    def initTables():
        with datacontrol.connection:
            datacontrol.cursor.execute(
                "CREATE TABLE IF NOT EXISTS {} ({} INTEGER PRIMARY KEY,{}  TEXT,{} TEXT,{} TEXT)".format(DATABASE['table_name'], *DATABASE['columns'])
            )


    def initTaskList():
        with datacontrol.connection:
            result = datacontrol.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(DATABASE['table_name']))
            result = result.fetchall()
            if not result == []:
                result = datacontrol.cursor.execute(
                    "SELECT DISTINCT {} FROM {}".format(DATABASE['columns'][1], DATABASE['table_name'])
                )
                result = result.fetchall()
                if not result == []:
                    newlist = []
                    for x in result:
                        newlist.append(x[0])
                    return newlist
                return result
            return []

    def saveToDatabase(project, date, seconds):
        if not project == '':
            if not project[0] in ('+', ' '):
                with datacontrol.connection:
                    datacontrol.cursor.execute(
                        "INSERT INTO {} ({},{},{}) VALUES (?, ?, ? )".format(DATABASE['table_name'], *DATABASE['columns'][1:4]),
                        (project, str(date), str(seconds))
                    )
                return True
        return False


    def checkDatabase():
        with datacontrol.connection:
            # result = datacontrol.cursor.description
            # for r in result:
                # print(r)
            result = datacontrol.cursor.execute("Select * From sqlite_master")
            result = result.fetchall()
            print(result)

            result = datacontrol.cursor.execute("Select * From {0}".format( DATABASE['table_name']))
            result = result.fetchall()
            print("result :", result )
            for r in result:
                print(r)


if __name__ == "__main__":
    print("testing")
    datacontrol.initTables()
    datacontrol.checkDatabase()
    datacontrol.initTaskList()

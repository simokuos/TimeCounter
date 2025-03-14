import sqlite3

class Model:
    def __init__(self):
        self.connection = sqlite3.connect('database/database.db')
        self.cursor = self.connection.cursor()
        with self.connection:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS workhours (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, used_seconds TEXT );' )

    def add_workhours(self, project, seconds):
        query=("INSERT INTO workhours (name, date, used_seconds) "
              f"VALUES ('{project}', date('now'), '{seconds}' );")

        with self.connection: #to commit changes
            self.cursor.execute(query)

    def get_recent_unique_projects(self):
        query = ("SELECT DISTINCT name "
                 "FROM workhours "
                 "WHERE date > date('now', '-6 months');"
                )

        return [row[0] for row in self.cursor.execute(query)] #values out of tubles

if __name__ == "__main__":
    print('Module: database/model, testing ')
    model = Model()
    # model.add_workhours("test", "1000")
    # model.add_workhours("test2", "2000")
    print(model.get_recent_unique_projects())

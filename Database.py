import sqlite3
class Database:
    def __init__(self, dbname):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()

    def create_table(self, tablename, columns):
        types = ",".join(["%s %s" % column for column in columns])
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(tablename, types))

    def insert(self, tablename, values):
        marks = ",".join(["?" for i in values])
        try:
            self.cursor.execute("INSERT INTO {} VALUES ({})".format(tablename, marks), values)
        except sqlite3.IntegrityError:
            raise
        else:
            print("INSERT INTO {} VALUES ({})".format(tablename, *values))

    def commit(self):
        self.connection.commit()

import sqlite3
from sqlite3 import Error


class Database(object):

    def __init__(self):
        self.connection = sqlite3.connect(r'database.db')
        self.cursor = self.connection.cursor()
        self.table_name = "Example_table"
        self.cursor.execute(
            f"create table if not exists {self.table_name} (column_1 int, column_2 text, column_3 real)")

    def insert_data(self):
        column_1 = int(input('Enter int: '))
        column_2 = input('Enter string: ')
        column_3 = float(input('Enter float: '))

        self.cursor.execute(
            f'insert into {self.table_name} (column_1, column_2, column_3) values(?,?,?)', (column_1, column_2, column_3))

        self.connection.commit()
        print('Data saved')

    def read_data(self):
        self.cursor.execute(f'select * from {self.table_name}')
        for row in self.cursor.fetchall():
            print(row)


if __name__ == "__main__":
    database = Database()
    database.insert_data()
    database.read_data()
    database.cursor.close()
    database.connection.close()

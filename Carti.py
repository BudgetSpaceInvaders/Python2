import sqlite3


class Books:
    def __init__(self):
        self.conn = sqlite3.connect('exemplu2.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER AUTO_INCREMENT PRIMARY KEY,
                                ISBN TEXT,
                                Title TEXT,
                                ApparitionDay TEXT,
                                Writer TEXT
                            )''')
        self.conn.commit()

    def adauga(self, ISBN, Title, ApparitionDay, Writer):
        self.cursor.execute(
            f"INSERT INTO books (ISBN, Title, ApparitionDay, Writer) VALUES ('{ISBN}', '{Title}', '{ApparitionDay}', '{Writer}')")
        self.conn.commit()

    def show(self):
        self.cursor.execute("SELECT * FROM books")
        print(self.cursor.fetchall())

    def sterge(self, id):
        self.cursor.execute(f"DELETE FROM books WHERE id = {id}")
        self.conn.commit()

    def update(self, id, ISBN, Title, ApparitionDay, Writer):
        self.cursor.execute(
            f"UPDATE books SET ISBN = {ISBN}, Title = '{Title}', ApparitionDay = {ApparitionDay}, Writer = {Writer} WHERE id = {id}")
        self.conn.commit()

    def drop(self):
        self.cursor.execute("DROP TABLE books")
        self.conn.commit()


book = Books()
book.adauga("9786067063028", "Aventurile lui Tom Sawyer", "2016", "Mark Twain")
book.adauga("HRR973-7923-43-X", "Aventurile lui Huckleberry Finn", "2004", "Mark Twain")
book.show()
book.drop()

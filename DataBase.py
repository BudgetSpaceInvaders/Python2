import sqlite3

class Persoane:
    def __init__(self):
        self.conn = sqlite3.connect('exemplu.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS persoane (
                                id INTEGER PRIMARY KEY,
                                nume TEXT,
                                varsta INTEGER
                            )''')
        self.conn.commit()

    def adauga(self, nume, varsta):
        self.cursor.execute(f"INSERT INTO persoane (nume, varsta) VALUES ('{nume}', {varsta})")
        self.conn.commit()
    def show(self):
        self.cursor.execute("SELECT * FROM persoane")
        print(self.cursor.fetchall())
    def sterge(self, id):
        self.cursor.execute(f"DELETE FROM persoane WHERE id = {id}")
        self.conn.commit()
    def update(self, id, nume, varsta):
        self.cursor.execute(f"UPDATE persoane SET nume = '{nume}', varsta = {varsta} WHERE id = {id}")
        self.conn.commit()

# Exemplu de utilizare
persoane = Persoane()
persoane.adauga("Ion", 32)
persoane.adauga("Maria", 28)
persoane.update(1, "Vasile", 33)
persoane.show()
persoane.sterge(2)
persoane.show()


import sqlite3

# Conectați-vă la baza de date sau creați-o dacă nu există
conn = sqlite3.connect("biblioteca.db")

# Obțineți un cursor pentru a executa comenzi SQL
cursor = conn.cursor()

# Definiți schema tabelului pentru cărți
create_table_query = """
CREATE TABLE IF NOT EXISTS carti (
    id INTEGER PRIMARY KEY,
    titlu TEXT,
    autor TEXT,
    an_publicare INTEGER,
    pret DOUBLE
)
"""

# Executați comanda SQL pentru a crea tabelul
cursor.execute(create_table_query)

insert_query1 = """
INSERT INTO carti (titlu, autor, an_publicare, pret)
VALUES ('Mândrie și prejudecată', 'Jane Austen', 1813, 150)
"""
cursor.execute(insert_query1)

# Exemplu 2
insert_query2 = """
INSERT INTO carti (titlu, autor, an_publicare, pret)
VALUES ('1984', 'George Orwell', 1949, 45)
"""
cursor.execute(insert_query2)

# Închideți cursorul și aplicați modificările în baza de date
conn.commit()

# Închideți conexiunea la baza de date
conn.close()

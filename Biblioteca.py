class Book:
    def __init__(self, titlu, autor, ISBN, nrexemplare):
        self.titlu = titlu
        self.autor = autor
        self.ISBN = ISBN
        self.nrexemplare = nrexemplare

    def estevalid(self):
        if self.nrexemplare > 0:
            return True
        else:
            return False

    def imprumut(self):
        if self.estevalid():
            self.nrexemplare -= 1
            print('Ati imprumutat cartea "' + self.titlu + '" de', self.autor)
            print("Au ramas", self.nrexemplare, "exemplare")
        else:
            print("Stoc insuficient")

    def intoarcere(self):
        self.nrexemplare += 1
        print('Ati intors cartea "' + self.titlu + '" de', self.autor)
        print("Acum sunt", self.nrexemplare, "exemplare ramase")


Book1 = Book("Singur pe Lume", "Hector Malot", "973-7923-19-7", 91)
Book1.estevalid()
Book1.imprumut()
Book1.intoarcere()
Book1.imprumut()

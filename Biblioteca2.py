class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def show(self):
        return self.title, self.author, self.year


class Library:
    def __init__(self):
        self.books = []

    def adder(self, book):
        self.books.append(book)

    def remove(self, query):
        result = self.finder(query)
        if len(result) > 0:
            for book in result:
                self.books.remove(book)
            print("The book was deleted succesfully.")
        else:
            print("There wasn't any book found.")

    def show(self):
        for book in self.books:
            print(f"Title: {book.getTitle()}, Author: {book.getAuthor()}, Year: {book.getYear()}")

    def finder(self, prompt):
        result = []
        for x in self.books:
            if prompt.lower() in x.getTitle().lower() or prompt.lower() in x.getAuthor().lower():
                result.append(x)
        return result


library = Library()
book1 = Book("The adventures of Tom Sawyer", "Mark Twain", 2017)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
book3 = Book("The Chronicles of Narnia", "C.S. Lewis", 1950)
book4 = Book("1984", "George Orwell", 1949)
print(book1.getTitle())
print(book1.getAuthor())
print(book1.getYear())
library.adder(book1)
library.adder(book2)
library.adder(book3)
library.adder(book4)
library.show()
resulting = library.finder("Mark Twain")
for book in resulting:
    print(f"Title: {book.getTitle()}, Author: {book.getAuthor()}, Year: {book.getYear()}")
library.remove("Mark Twain")
library.show()

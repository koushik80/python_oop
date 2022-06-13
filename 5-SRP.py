# Single Responsibility Principle (SRP)

class LibraryBooks:

    def __init__(self):
        self.books = {}

    def add_book(self, name, price):
        self.books[name] = price

    def remove_book(self, name):
        del self.books[name]
    
    def print_books(self):
        print(self.books)

    # KULLAKIN LUOKALLA TULISI OLLA VAIN 1 TEHTÄVÄ
    # Jos seuraavat metodit lisäisi, rikkoisi SRP-sääntöä    

    # def sell_book(self,name):
        # pass

    # def print_total_income(self):
        # pass


# Järkevämpää on tehdä oma luokka, jotta ei riko jo olemassa olevaa,
# toimivaa luokkaa. Näin uusia ominaisuuksia tulisi lisätä ohjelmaan.
# Huom. ylläolevan luokan instanssi viedään parametrina
class LibrarySalesOperations:
    def __init__(self, library_books): # library
        #self.library = library
        self.books = library_books
        self.total_income = 0
        self.sold_books = []

    def sell_book(self,name):
        self.total_income += self.books[name] # self.library.books[name]  
        self.sold_books.append(name)
    
    def print_total_income(self):
        print(self.total_income)

lib = LibraryBooks()
lib.add_book('book1', 50)

op = LibrarySalesOperations(lib.books) # lib
op.sell_book('book1')
op.print_total_income()
print(op.sold_books)

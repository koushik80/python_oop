""" Luo luokka BookStore, luo luokkaan konstruktori, joka ei saa parametreja
 (eli olio luodaan ilman parametreja).
 Aseta konstruktorissa olion books tyhjäksi dictionaryksi.

 Luo metodit add_book(name, price), remove_book(name) ja print_books().

 Laita add_book-metodiin:
 self.books[name] = price

 ja
 remove_book-metodiin:
 del self.books[name]

 Luo luokasta olio, ja lisää kirjoja, printtaa kirjat, poista kirja, printtaa taas.
 Eli testaa toiminnallisuutta
"""

class BookStore:
    def __init__(self):
        self.books = {}

    def add_book(self, name, price):
        self.books[name] = price

    def remove_book(self, name):
        #del self.books[name].pop()
        self.bookspop(name)

    def print_books(self):
        print(self.books)
        
  
    
bs = BookStore()
#bs.print_books()
bs.add_book('anaconda', '50')
bs.print_books()
#bs.remove_book('panda', '60')
#bs.print_books()
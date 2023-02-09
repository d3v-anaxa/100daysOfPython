# Library Management System

from os import system


class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = len(self.books)

    def showDetails(self):
        print("List of books : ", self.books)
        print("Total number of books : ", self.no_of_books)

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
        # self.showDetails()

    def remove_book(self, book):
        self.books.remove(book)
        self.no_of_books = len(self.books)


menu = '''
1. add book
2. find and remove book
3. show details
4. stop()
Enter choice : '''

NewLibrary = Library()

while True:
    system("sleep 3 &&  clear")
    match int(input(menu)):
        case 1:
            book_name = str(input("Enter book name : "))
            NewLibrary.add_book(book_name)
        case 2:
            book_name = str(input("Enter book name : "))
            try:
                NewLibrary.remove_book(book_name)
            except Exception as e:
                print("Not Available")
        case 3:
            NewLibrary.showDetails()
        case 4:
            exit(0)
        case _:
            break

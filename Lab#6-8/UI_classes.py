from tests import *
from service import *

class Books_UI:
    def __init__ (self):
        self._bookService = ServiceBooks()

    @staticmethod
    def print_menu ():
        menu = '''
1. Add book
2. List books
3. Remove book
4. Update book
x. Exit
        '''
        print(menu)

    def add_book_UI (self):
        '''
        Reads and adds a book to the book list
        '''
        bookId = input("Give book ID: ").strip(" ")
        title = input("Give title: ").strip(" ")
        author = input("Give author: ").strip(" ")
        book = Book(bookId, title, author)

        try:
            self._bookService.add_book(book)
            print("\nThe book was added succesfully\n")
        except duplicateID:
            print("\nThe book already exists\n")
        except badId:
            print("\nThe id is not a natural number")
        
    def list_books_UI (self):
        books = self._bookService.list_books()
        if len(books) == 0:
            print("\nThere are no books\n")
        else:
            for i in books:
                print(i)

    def remove_book_UI (self):
        '''
        Removes a book after a given id
        '''
        ID = input("Give the book ID: ")

        try:
            self._bookService.remove_bookID(ID)
            print("\nThe book was removed succesfully\n")
        except IdDoesNotExist:
            print("\nThe required book does not exist\n")
        
    def update_book_UI (self):
        '''
        Updates the author or the title of a given book
        '''
        ID = input("Give ID: ")
        choice = '''
1. Update author
2. Update title
        '''
        print(choice)
        choice = input("> ")
        if choice == "1":
            author = input("Give new author: ")
            try:
                self._bookService.update_book_author(ID, author)
                print("\nThe book was updated succesfully\n")
            except IdDoesNotExist:
                print("\nThe required book doesn't exist\n")
        
        elif choice == "2":
            title = input("Give title: ")
            try:
                self._bookService.update_book_title(ID, title)
                print("\nThe book was updated succesfully\n")
            except IdDoesNotExist:
                print("\nThe required book does not exist\n")
        else:
            print("\nInvalid command\n")

    def start_book_ui (self):
        commands = {
            "1" : self.add_book_UI,
            "2" : self.list_books_UI,
            "3" : self.remove_book_UI,
            "4" : self.update_book_UI
        }

        while True:
            self.print_menu()
            choice = input("> ")
            print("")
            choice = choice.strip(" ")
            if choice in commands:
                commands[choice]()
                self._bookService.sort_book_list()
            elif choice == "x":
                return
            else:
                print("Invalid command")
            
#booksUi = Books_UI()
#booksUi.start()

class Clients_UI ():
    def __init__ (self):
        self._clientService = ServiceBooks()
    
    def add_client_ui (self):
        '''
        Function reads a client and adds it to the list
        '''
        pass

    def start_client_ui (self):
        commands = {
            
        }

        while True:
            self.print_menu()
            choice = input("> ")
            print("")
            choice = choice.strip(" ")
            if choice in commands:
                commands[choice]()
            elif choice == "x":
                return
            else:
                print("Invalid command")


    

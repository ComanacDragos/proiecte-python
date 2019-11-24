from service import *

class UI:
    def __init__ (self, booksService, clientsService, rentalsService):
        self.booksService = booksService
        self.clientsService = clientsService
        self.rentalsService = rentalsService

#-----------------------Books----------------------------------------------------------------#



    @staticmethod
    def print_books_menu ():
        menu = '''
1. Add book
2. List books
3. Remove book
4. Update book
x. Go back to main menu
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
            self.booksService.add_book(book)
            print("\nThe book was added succesfully\n")
        except duplicateID:
            print("\nThe book already exists\n")
        except badId:
            print("\nThe id is not a natural number\n")
        except emptyString:
            print("\nThe author or the title is void\n")
        
    def list_books_UI (self):
        books = self.booksService.list_books()
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
            self.booksService.remove_bookID(ID)
            self.rentalsService.remove_rentals(self.rentalsService.bookId_rentals(ID))
            print("\nThe book was removed succesfully\n")
        except IdDoesNotExist:
            print("\nThe required book does not exist\n")
        except badId:
            print("\nThe id not a natural number")

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
                self.booksService.update_book_author(ID, author)
                print("\nThe book was updated succesfully\n")
            except IdDoesNotExist:
                print("\nThe required book doesn't exist\n")
            except emptyString:
                print("\nThe new name of the author is void\n")
            except badId:
                print("\nThe id is not a natural number\n")
        
        elif choice == "2":
            title = input("Give title: ")
            try:
                self.booksService.update_book_title(ID, title)
                print("\nThe book was updated succesfully\n")
            except IdDoesNotExist:
                print("\nThe required book does not exist\n")
            except emptyString:
                print("\nThe new value of the title is void\n")
            except badId:
                print("\nThe id is not a natural number\n")
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
            self.print_books_menu()
            choice = input("> ")
            print("")
            choice = choice.strip(" ")
            if choice in commands:
                commands[choice]()
                if choice in ["1", "3"]:
                    self.booksService.sort_book_list()
            elif choice == "x":
                return
            else:
                print("Invalid command")
       


#---------------------------Clients-----------------------------------#


    @staticmethod
    def print_clients_menu():
        menu = '''
1. Add client
2. List clients
3. Remove client
4. Update client
x. Go back to main menu
'''
        print (menu)
    def add_client_ui (self):
        '''
        Function reads a client and adds it to the list
        '''
        ID = input("Give ID: ").strip(" ")
        name = input("Give name: ").strip(" ")
        client = Client(ID, name)
        try:
            self.clientsService.add_client(client)
            print("\nThe client was added succesfully\n")
        except badId:
            print("\nThe id is not a natural number\n")
        except duplicateID:
            print("\nA client with this id already exists\n")

    def list_clients_ui (self):
        '''
        Function lists all clients
        '''
        clients = self.clientsService.list_clients()
        if len(clients) == 0:
            print("\nThere are no clients\n")
        else:
            for i in clients:
                print(i)
            

    def remove_client_ui (self):
        '''
        Removes a client from the list of clients
        '''
        ID = input("Give the id: ").strip(" ")
        try:
            self.clientsService.remove_client(ID)
            self.rentalsService.remove_rentals(self.rentalsService.clientId_rentals(ID))
            print("\nThe client was removed succesfully")
        except IdDoesNotExist:
            print("\nThe required id does not exist\n")
        except badId:
            print("\nThe id is not a natural number\n")

    def update_client_ui (self):
        '''
        Updates a client's name
        '''
        ID = input("Give id: ").strip(" ")
        name = input("Give name: ").strip(" ")
        try: 
            self.clientsService.update_client_name(ID, name)
            print("\nThe client was updated succesfully\n")
        except badId:
            print("\nThe id is not a natural number\n")
        except IdDoesNotExist:
            print("\nThe required client does not exist")
    

    def start_client_ui (self):
        commands = {
            "1" : self.add_client_ui,
            "2" : self.list_clients_ui,
            "3" : self.remove_client_ui,
            "4" : self.update_client_ui
        }

        while True:
            self.print_clients_menu()
            choice = input("> ")
            print("")
            choice = choice.strip(" ")
            if choice in commands:
                commands[choice]()
                if choice in ["1", "3"]:
                    self.clientsService.sort_client_list()
            elif choice == "x":
                return
            else:
                print("Invalid command")


#------------------------------Rentals-------------------------------#


    @staticmethod
    def print_rental_menu ():
        menu = '''
1. List rentals
2. Rent a book
3. Return a book
x. Go back to main menu
        '''
        print(menu)

    def list_rentals (self):
        cont = 0
        if len(self.rentalsService.rentalsRepo) == 0:
            print("\nThere are no rentals\n")
            return 
        for i in self.rentalsService.rentalsRepo:
            cont = cont + 1 
            print(str(cont) + ". " + str(i))
    
    def ui_add_rental (self):
        '''
        Reads the values of a rental then adds it to the list
        '''
        print("")
        rentalId = input("Give rental ID: ").strip(" ")
        bookId = input("Give book ID: ").strip(" ")
        clientId = input("Give client ID: ").strip(" ")
        rentedDate = input("Give rented date(day.month.year): ").strip(" ")
        d = rentedDate.split(".")
        print("")

        try:
            date(int(d[2]), int(d[1]), int(d[0]))
        except:
            print("\nBad date\n")
            return

        rentedDate = date(int(d[2]), int(d[1]), int(d[0]))

        rental = Rental(rentalId, bookId, clientId, rentedDate)

        try:
            self.rentalsService.add_rental(rental)
            print("\nThe rental was added succesfully\n")
        except badId:
            print("\nOne of the id's is not a natural number\n")
        except duplicateID:
            print("\nThere already exists a rental with this rental ID\n")
        except rentedBook:
            print("\nThe required book is rented\n")
        except bookDoesNotExist:
            print("\nThe required book doesn't exist\n")
        except clientDoesNotExist:
            print("\nThe  required client does not exist\n")
        except badDate:
            print("\nThe book was rented in that period\n")

    def ui_return_book (self):
        '''
        Returns a book
        '''
        print("")
        rentalId = input("Give rental ID: ").strip(" ")
        returnedDate = input("Give return date(day.month.year): ").strip(" ")
        print("")
        d = returnedDate.split(".")
        try:
            returnedDate = date(int(d[2]), int(d[1]), int(d[0]))
        except:
            print("\nBad date\n")
        else:
            try:
                self.rentalsService.return_book(rentalId, returnedDate)
                print("\nThe book was returned succesfully\n")
            except badDates:
                print("\nThe return date is smaller than the rent date\n")
            except returnedBook:
                print("\nThe book is already returned")
            except rentalDoesNotExist:
                print("\nThe required rental does not exist\n")
            except badId:
                print("\nThe rental id is not a natural number")
            except badReturnDate:
                print("\nThe book was borrowed in that period\n")

    def start_rental_ui (self):
        commands = {
            "1" : self.list_rentals,
            "2" : self.ui_add_rental,
            "3" : self.ui_return_book,
        }
    
        while True:
            self.print_rental_menu()
            choice = input("> ").strip(" ")
            print("")
            if choice in commands:
                commands[choice]()
                if choice == "2":
                    self.rentalsService.sort_rentals()
            elif choice == "x":
                return
            else:
                print("Invalid command")

    @staticmethod
    def search_book_menu ():
        menu = '''
1. Search for Id
2. Search author
3. Search title
x. Go back to main menu
        '''
        print(menu)

    def search_book_ui (self):
        '''
        Reads a word and searches for books that contain that word in either one of their fields
        '''       
        self.search_book_menu()
        choice = input(">").strip(" ")

        if choice == "1":
            word = input("\nGive id to search for: ").strip("")
            books = self.booksService.search_book_Id(word)
        elif choice == "2":
            word = input("\nGive author to search for: ").strip("")
            books = self.booksService.search_book_author(word)
        elif choice == "3":
            word = input("\nGive title to search for: ").strip("")
            books = self.booksService.search_book_title(word)
        elif choice == "x":
            return
        else:
            print("\nInvalid command\n")
            return
        
        if len(books) == 0:
            print("\nThere are no books matching this description\n")
            return
        cont = 0
        for i in books:
            cont += 1
            print(str(cont) + ". " + str(i))

    @staticmethod
    def search_client_menu ():
        menu = '''
1. Search for Id
2. Search for name
3. Go back to main menu
        '''
        print(menu)
    
    def search_client_ui (self):
        '''
        Reads a word and searches for clients that contain that word in either one of their fields
        '''
        self.search_client_menu()
        choice = input(">").strip(" ")
        
        if choice == "1":
            word = input("\nGive id to search for: ").strip("")
            clients = self.clientsService.search_client_id(word)
        elif choice == "2":
            word = input("\nGive name to search for: ").strip("")
            clients = self.clientsService.search_client_name(word)
        elif choice == "3":
            return
        else:
            print("\nInvalid command\n")
            return
        
        if len(clients) == 0:
            print("\nThere are no clients matching that description\n") 
            return
        
        cont = 0
        for i in clients:
            cont += 1
            print(str(cont) + ". " + str(i))
        
    def most_rented_books_ui (self):
        bookIds = self.rentalsService.most_rented_books()

        if len(bookIds) == 0:
            print("\nThere are no books\n")
            return

        books = self.booksService.list_books_id(bookIds)
        books = self.booksService.list_books(books)

        for i in books:
            print(i)
        
    @staticmethod
    def statistics_menu ():
        menu = '''
1. Most rented books
2. Most active clients
3. Most rented author
x. Go back to main menu
        '''
        print(menu)
    
    def statistics_ui (self):
        self.statistics_menu()
        choice = input(">").strip(" ")

        commands = {
            "1" : self.most_rented_books_ui
        }

        if choice in commands:
            commands[choice]()
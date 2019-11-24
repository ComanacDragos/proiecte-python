from newRepository import *
from datetime import date


class BooksService:
    def __init__ (self, booksRepo):
        self.booksRepo = booksRepo
    
    def add_book (self, book):
        '''
        Adds a book to the book list
        Input:
            book - object of class Book
        Exceptions:
            duplicateBook - duplicate book id
        '''
        if len(str(book.author)) == 0 or len(str(book.title)) == 0:
            raise emptyString
        self.booksRepo.store(book)

    def list_books (self, listOfBooks = None):
        '''
        Returns the list of some books in a specific format
        Input:
            listOfBooks - a list of books (with the default list being all the books)
        Output:
            books - the required books in a specific format
        '''
        if listOfBooks == None:
            listOfBooks = self.booksRepo
        books = []
        count = 0
        for i in listOfBooks:
            count += 1
            books.append(str(count) + ". " + str(i))
        return books

    def list_books_id (self, idList):
        '''
        Returns a list of book objects having ids from idList
        '''
        books = []
        for i in idList:
            index = self.booksRepo.find(i)
            book = self.booksRepo[index]
            books.append(book)
        for i in self.booksRepo:
            if i.Id not in idList:
                books.append(i)
        return books
        

    def remove_bookID (self, ID):
        '''
        Removes a book with a given id
        Input:
            ID - the id of the book to be removed
        Exception:
            bookIdDoesNotExist - required book doesn't exist
        '''
        self.booksRepo.delete(ID)

    def update_book_author (self, ID, author):
        '''
        Updates the author of a given book 
        Input:
            ID - the id of the book to be removed
            author - the new author
        Exception:
            bookIdDoesNotExist - required book doesn't exist
        '''

        self.booksRepo.valid_ID(ID)

        if len(str(author)) == 0:
            raise emptyString
        
        for i in self.booksRepo:
            if i.Id == ID:
                i.author = author
                return
        raise IdDoesNotExist("Required book doesn't exist")

    def update_book_title (self, ID, title):
        '''
        Updates the title of a given book 
        Input:
            ID - the id of the book to be removed
            title - the new title
        Exception:
            bookIdDoesNotExist - required book doesn't exist
        '''
        self.booksRepo.valid_ID(ID)

        if len(str(title)) == 0:
            raise emptyString

        for i in self.booksRepo:
            if i.Id == ID:
                i.title = title
                return
        raise IdDoesNotExist("Required book doesn't exist")

    def sort_book_list (self):
        '''
        Sorts the list with respect to the book ids
        '''
        self.booksRepo.sort()

    def book_exists (self, ID):
        '''
        Checks if there is a book with given ID
        Input:
            ID - the required book id
        '''
        for i in self.booksRepo:
            if i.Id == ID:
                return True
        return False
    
    def search_book_Id (self, Id):
        '''
        Returns a list of all books that have the string Id book Id
        '''
        books = []
        for i in self.booksRepo:
            if Id.upper() in i.Id.upper():
                books.append(i)
        return books

    def search_book_author (self, author):
        '''
        Returns a list of all books that have the string author book author
        '''
        books = []
        for i in self.booksRepo:
            if author.upper() in i.author.upper():
                books.append(i)
        return books

    def search_book_title (self, title):
        '''
        Returns a list of all books that have the string title book title
        '''
        books = []
        for i in self.booksRepo:
            if title.upper() in i.title.upper():
                books.append(i)
        return books

    def most_rented_author (self, idDict):
        '''
         This provides the list of book authored, sorted in descending order of the number of rentals their books have
        '''
        authors = {}
        for i in idDict:
            index = self.booksRepo.find(i)
            book = self.booksRepo[index]

            if book.author not in authors:
                authors[book.author] = idDict[i]
            else:
                authors[book.author] += idDict[i]
        
        for i in self.booksRepo:
            if i.Id not in idDict:
                if i.author not in authors:
                    authors[i.author] = 0

        return authors

class ClientsService:
    def __init__ (self, clientsRepo):
        self.clientsRepo = clientsRepo

    
    def add_client (self, client):
        '''
        Adds a client to the client list 
        Input:
            client - object of type Client
        '''
        self.clientsRepo.store(client)

    
    def list_clients (self, clientList = None):
        '''
        Returns the list of some clients in a specific format
        Input:
            clientList - the list of some clients in a specific format (if no client list is given all clients are considered)
        Output:
            clients - the required clients in a specific format
        '''
        if clientList == None:
            clientList = self.clientsRepo
        clients = []
        count = 0
        for i in clientList:
            count += 1
            clients.append(str(count) + ". " + str(i))
        return clients

    def list_clients_Id (self, clientIds):
        '''
        Returns a list of client object type, given a list of their ids
        '''    
        clients = []
        for i in clientIds:
            index = self.clientsRepo.find(i)
            client = self.clientsRepo[index]
            clients.append(client)
        for i in self.clientsRepo:
            if i.Id not in clientIds:
                clients.append(i)
        
        return clients

    def remove_client (self,  ID):
        '''
        Removes a client with a given ID
        Input:
            ID - the id of the client to be removed
        '''
        self.clientsRepo.delete(ID)

    def update_client_name (self, ID, name):
        '''
        Updates the name of a client 
        Input:
            ID - the id of the client to be updated
            name - the new name
        '''
        self.clientsRepo.valid_ID(ID)
        for i in self.clientsRepo:
            if int(i.Id) == int(ID):
                i.name = name
                return
        raise IdDoesNotExist

    def sort_client_list (self):
        '''
        Sorts the client list with respect to client id
        '''
        self.clientsRepo.sort()

    
    def client_exists (self, ID):
        '''
        Checks if there is an client with given ID
        Input:
            ID - the required client id
        '''
        for i in self.clientsRepo:
            if i.Id == ID:
                return True
        return False

    def search_client_id (self, Id):
        '''
        Search for a client using partial string matching for id
        '''
        clients = []
        for i in self.clientsRepo:
            if Id.upper() in i.Id.upper():
                clients.append(i)
        return clients
    
    def search_client_name (self, name):
        '''
        Search for a client using partial string matching for name
        '''
        clients = []
        for i in self.clientsRepo:
            if name.upper() in i.name.upper():
                clients.append(i)
        return clients



class RentalsService:
    def __init__ (self, rentalsRepo, booksService, clientsService):
        self.rentalsRepo = rentalsRepo
        self.booksService = booksService
        self. clientsService = clientsService
   
        

    def add_rental (self, rental):
        '''
        Adds a rental to the list of rentals
        Input:
            rental - object of type rental
        '''

        self.rentalsRepo.valid_ID(rental.Id)
        self.rentalsRepo.valid_ID(rental.bookId)
        self.rentalsRepo.valid_ID(rental.clientId)

        for i in self.rentalsRepo:
            if i.Id == rental.Id:
                raise duplicateID
            if i.bookId == rental.bookId:
                if i.returnedDate == None:
                    raise rentedBook
                elif i.returnedDate != None:
                    if rental.rentedDate <= i.returnedDate and rental.rentedDate >= i.rentedDate :
                        raise badDate
        
        if self.booksService.book_exists(rental.bookId) == False:
            raise bookDoesNotExist

        if self.clientsService.client_exists(rental.clientId) == False:
            raise clientDoesNotExist

        self.rentalsRepo.store(rental)

    @staticmethod
    def intersected_dates (x1, y1, x2, y2):
        '''
        Checks if the periods of time intersect 
        [x1, y1] - first time interval
        [x2, y2] - second time interval
        Where x1,y1,x2,y2 are dates and y2 may be None
        Output:
            True if they intersect
            False otherwise
        '''
        if y2 == None:
            if x2 > x1 and x2 < y1:
                return False
            return True
        else:
            
            if x1 > y1 or x2 > y2:
                return False
            if y1 < x2 or x1 > y2:
                return True
            return False
            

    def return_book (self, ID, date):
        '''
        Set the return date for a given rental
        Input:
            ID - rental ID
            date - the return date
        '''
        self.rentalsRepo.valid_ID(ID)
        for i in self.rentalsRepo:
            if i.Id == ID:
                if i.returnedDate == None:
                    if i.rentedDate > date:
                        raise badDates
                    else:
                        for j in self.rentalsRepo:
                            if i.bookId == j.bookId and self.intersected_dates(i.rentedDate, date, j.rentedDate, j.returnedDate) ==False:
                                raise badReturnDate
                        i.returnedDate = date
                        return
                else:
                    raise returnedBook
        raise rentalDoesNotExist

    def sort_rentals (self):
        '''
        Sorts the list of rentals with respect to rental id
        '''
        self.rentalsRepo.sort()
 
    def bookId_rentals (self, ID):
        '''
        Returns a list of rentals with a given book ID
        '''
        rentals = []
        for i in self.rentalsRepo:
            if i.bookId == ID:
                rentals.append(i)
        return rentals

    def clientId_rentals (self, ID):
        '''
        Returns a list of rentals with a given book ID
        '''
        rentals = []
        for i in self.rentalsRepo:
            if i.clientId == ID:
                rentals.append(i)
        return rentals

    def remove_rentals (self, rentals):
        '''
        Removes multiple rentals from a list of rentals
        '''
        for i in rentals:
            self.rentalsRepo.delete(i.Id)
    
    
    def add_rentals (self, rentals):
        '''
        Removes multiple rentals from a list of rentals
        '''
        for i in rentals:
            self.rentalsRepo.store(i)


    def most_rented_books (self):
        books = {}
        for i in self.rentalsRepo:
            if i.bookId not in books:
                books[i.bookId] = 1
            else:
                books[i.bookId] += 1
        
    
        return books

    def most_active_client (self):
        clients = {}
        for i in self.rentalsRepo:
            if i.clientId not in clients:
                if i.returnedDate != None:
                    clients[i.clientId] = (i.returnedDate - i.rentedDate).days
            else:
                if i.returnedDate != None:
                    clients[i.clientId] += (i.returnedDate - i.rentedDate).days
        
        clients = sorted(clients, key=clients.__getitem__, reverse = 1)

        return clients


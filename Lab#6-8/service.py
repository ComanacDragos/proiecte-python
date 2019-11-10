from domain import *
from exceptions import *
from random_words import *
import random
import copy

class ServiceBooks:
    def __init__ (self):
        self._bookList = []
        for i in range(100, 110):
            l = random.choice(books)
            self._bookList.append(Book(str(i), l[0], l[1]))        

    def valid_ID (self, ID):
        '''
        Cheks if the id is correct or not
        '''
        try:
            nr = float(ID)
        except:
            raise badId
        else:
            if nr < 0 or int(nr) != nr:
                raise badId
                

    def add_book (self, book):
        '''
        Adds a book to the book list
        Input:
            book - object of class Book
        Exceptions:
            duplicateBook - duplicate book id
        '''
        self.valid_ID(book.bookId)
        '''
        try:
            book.bookId = int(book.bookId)
        except:
            raise badId
        else:
            if int(book.bookId) < 0 or int(book.bookId) != book.bookId:
                raise badId
        '''
        for i in self._bookList:
            if i == book:
                raise duplicateID("Duplicate book id!")
        self._bookList.append(book)

    def list_books (self, listOfBooks = None):
        '''
        Returns the list of some books in a specific format
        Input:
            listOfBooks - a list of books (with the default list being all the books)
        Output:
            books - the required books in a specific format
        '''
        if listOfBooks == None:
            listOfBooks = self._bookList
        books = []
        count = 0
        for i in listOfBooks:
            count += 1
            books.append(str(count) + ". " + str(i))
        return books

    def remove_bookID (self, ID):
        '''
        Removes a book with a given id
        Input:
            ID - the id of the book to be removed
        Exception:
            bookIdDoesNotExist - required book doesn't exist
        '''
        self.valid_ID(ID)    

        for i in self._bookList:
            if int(i.bookId) == int(ID):
                self._bookList.remove(i)
                return
        raise IdDoesNotExist("Required book doesn't exist!")

    def update_book_author (self, ID, author):
        '''
        Updates the author of a given book 
        Input:
            ID - the id of the book to be removed
            author - the new author
        Exception:
            bookIdDoesNotExist - required book doesn't exist
        '''
        self.valid_ID(ID)
        for i in self._bookList:
            if i.bookId == ID:
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
        for i in self._bookList:
            if i.bookId == ID:
                i.title = title
                return
        raise IdDoesNotExist("Required book doesn't exist")

    def sort_book_list (self):
        '''
        Sorts the list with respect to the book ids
        '''
        self._bookList.sort()

class ServiceClients:
    def __init__(self):
        self._clientList = []
        self._clientList.append(Client(100, "Bob"))

    def valid_ID (self, ID):
        '''
        Cheks if the id is correct or not
        '''
        try:
            nr = float(ID)
        except:
            raise badId
        else:
            if nr < 0 or int(nr) != nr:
                raise badId

    def add_client (self, client):
        '''
        Adds a client to the client list 
        Input:
            client - object of type Client
        '''
        self.valid_ID(client.clientId)

        for i in self._clientList:
            if client == i:
                raise duplicateID
        self._clientList.append(client)
    
    def list_clients (self, clientList = None):
        '''
        Returns the list of some clients in a specific format
        Input:
            clientList - the list of some clients in a specific format (if no client list is given all clients are considered)
        Output:
            clients - the required clients in a specific format
        '''
        if clientList == None:
            clientList = self._clientList
        clients = []
        count = 0
        for i in clientList:
            count += 1
            clients.append(str(count) + ". " + str(i))
        return clients
    
    def remove_client (self,  ID):
        '''
        Removes a client with a given ID
        Input:
            ID - the id of the client to be removed
        '''
        self.valid_ID(ID) 

        for i in self._clientList:
            if int(i.clientId) == int(ID):
                self._clientList.remove(i)
                return
        raise IdDoesNotExist

    def update_client_name (self, ID, name):
        '''
        Updates the name of a client 
        Input:
            ID - the id of the client to be updated
            name - the new name
        '''
        self.valid_ID(ID)
        for i in self._clientList:
            if int(i.clientId) == int(ID):
                i.name = name
                return
        raise IdDoesNotExist
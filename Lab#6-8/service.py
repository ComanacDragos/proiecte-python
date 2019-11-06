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
        

    def add_book (self, book):
        '''
        Adds a book to the book list
        Input:
            book - object of class Book
        Exceptions:
            duplicateBook - duplicate book id
        '''
        try:
            book.bookId = int(book.bookId)
        except:
            raise badId
        else:
            if int(book.bookId) < 0 or int(book.bookId) != book.bookId:
                raise badId
        
        for i in self._bookList:
            if i == book:
                raise duplicateID("Duplicate book id!")
        self._bookList.append(book)

    def list_books (self):
        '''
        Returns the list of books in a specific format
        Output:
            books - the list of books in that format
        '''
        books = []
        count = 0
        for i in self._bookList:
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

    def add_client (self, client):
        '''
        Adds a client to the client list 
        Input:
            client - object of type Client
        '''
        try:
            client.clientId = int(client.clientId)
        except:
            raise badId
        else:
            ID = client.clientId
            if ID < 0 or ID != int(ID):
                raise badId
        for i in self._clientList:
            if client == i:
                raise duplicateID
        self._clientList.append(client)


def test_add_client():
    service = ServiceClients()
    service.add_client(Client("1", "bobo"))
    assert str(service._clientList[-1].clientId) == "1" and service._clientList[-1].name == "bobo"
    try:
        service.add_client(Client("-23","bobo"))
        assert False
    except badId:
        assert True

    try:
        service.add_client(Client("1","bobo"))
        assert False
    except duplicateID:
        assert True
test_add_client()
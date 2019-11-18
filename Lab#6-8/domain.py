class Book:
    def __init__ (self, _ID, _Title, _Author):
        self.bookId = _ID
        self.title = _Title
        self.author = _Author

    @property
    def bookId (self):
        return self._ID

    @bookId.setter
    def bookId (self, value):
        self._ID = value

    @property
    def title (self):
        return self._Title
    
    @title.setter
    def title (self, value):
        self._Title = value

    @property
    def author (self):
        return self._Author
    
    @author.setter
    def author (self, value):
        self._Author = value

    def __eq__ (self, book):
        return int(self.bookId) == int(book.bookId)

    def __str__ (self):
        return "The book id is " + str(self.bookId) + ", the author is " + str(self.author) + " and the title is " + str(self.title)

    def __lt__ (self, book):
        return int(self.bookId) < int(book.bookId)


class Client:
    def __init__ (self, _ID, _Name):
        self.clientId = _ID
        self.name = _Name

    @property
    def clientId (self):
        return self._ID
    
    @clientId.setter
    def clientId (self, value):
        self._ID = value

    @property
    def name (self):
        return self._Name
    
    @name.setter
    def name (self, value):
        self._Name = value

    def __str__ (self):
        return "For " + str(self.name)+ " the client id is " + str(self.clientId) 
    
    def __eq__ (self, client):
        return int(self.clientId) == int(client.clientId)
    
    def __lt__ (self, client):
        return int(self.clientId) < int(client.clientId)

class Rental:
    def __init__ (self, _ID, _BookId, _ClientId, _RentedDate, _ReturnedDate = None):
        self.rentalId = _ID
        self.bookId = _BookId
        self.clientId = _ClientId
        self.rentedDate = _RentedDate
        self.returnedDate = _ReturnedDate

    @property
    def rentalId (self):
        return self._ID 
    
    @rentalId.setter
    def rentalId (self, value):
        self._ID = value

    @property
    def bookId (self):
        return self._BookId 
    
    @bookId.setter
    def bookId (self, value):
        self._BookId = value

    @property
    def clientId (self):
        return self._ClientId 
    
    @clientId.setter
    def clientId (self, value):
        self._ClientId = value

    @property
    def returnedDate (self):
        return self._ReturnedDate 
    
    @returnedDate.setter
    def returnedDate (self, value):
        self._ReturnedDate = value

    @property
    def rentedDate (self):
        return self._RentedDate 
    
    @rentedDate.setter
    def rentedDate (self, value):
        self._RentedDate = value

    def __str__ (self):
        if self.returnedDate == None:
           return "For the rental Id " + str(self.rentalId) + ", the book Id " + str(self.bookId) + " and the client id " +  str(self.clientId) + " the rented date is " +  str(self.rentedDate.strftime("%d, %b %Y")) 
        else:
            return "For the rental Id " + str(self.rentalId) + ", the book Id " + str(self.bookId) + " and the client id " +  str(self.clientId) + " the rented date is " +  str(self.rentedDate.strftime("%d, %b %Y")) + " and the returned date is " + str(self.returnedDate.strftime("%d, %b %Y"))

    def __lt__ (self, rental):
        return int(self.rentalId) < int(rental.rentalId)
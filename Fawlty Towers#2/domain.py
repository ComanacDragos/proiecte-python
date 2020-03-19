from datetime import date

class Room:
    def __init__(self, id, type):
        self.is_natural(id)
        self.is_natural(type)
        self.ID = int(id)
        if int(type) not in [1,2,4]:
           raise BadRoomType("Bad room type")
        self.type = int(type)

    @property
    def id (self):
        return self.ID

    @staticmethod
    def is_natural (n):
        try:
            n = float(n)
        except:
            raise NotNaturalNumber("Not natural number")
        else:
            if n <= 0 or n != int(n):
                raise NotNaturalNumber("Not natural number")

    def __str__(self):
        return "The id is: " + str(self.id) + " and the type is: " +  str(self.type)

class Reservation:
    def __init__(self, id, roomNumber, family, numberGuests, arrival, departure):

        self.is_natural(id)
        self.is_natural(roomNumber)
        self.is_natural(numberGuests)

        if len(family) == 0:
            raise EmptyFamily("Empty family")

        self._id = id
        self._roomNumber = int(roomNumber)
        self._family = family
        self._numberGuests = int(numberGuests)
        self._arrival = self.valid_date(arrival)
        self._departure = self.valid_date(departure)

        if self._numberGuests  < 1 or self._numberGuests>4:
            raise BadGuests("Bad nr of guests")

        if self._arrival > self._departure:
            raise BadDate("Arrival after departure")

    @staticmethod
    def is_natural(n):
        try:
            n = float(n)
        except:
            raise NotNaturalNumber("Not natural number")
        else:
            if n <= 0 or n != int(n):
                raise NotNaturalNumber("Not natural number")

    @staticmethod
    def valid_date(d):
        newd = d.split(".")
        if len(newd) != 2:
            raise BadDate("Bad date")

        try:
            newd = date(year=2018, month=int(newd[1]), day=int(newd[0]))
        except:
            raise BadDate("Bad date")
        else:
            return newd

    def __str__(self):
        return str(self._id) + " " + str(self._roomNumber) +" "+ str(self._family) +" "+ str(self._numberGuests) +" "+ self._arrival.strftime("%d.%m") +" "+ self._departure.strftime("%d.%m")

    @property
    def id (self):
        return self._id

    @property
    def room (self):
        return self._roomNumber

    @property
    def arrival (self):
        return self._arrival

    @property
    def departure (self):
        return self._departure

class NotNaturalNumber (Exception):
    pass

class BadRoomType(Exception):
    pass

class EmptyFamily(Exception):
    pass

class BadDate(Exception):
    pass

class BadGuests (Exception):
    pass
class NoRooms(Exception):
    pass
class IdNotFound(Exception):
    pass
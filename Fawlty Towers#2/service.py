from repository import *
import random

class Service:
    def __init__(self, roomRepo, reservationsRepo):
        self._roomRepo = roomRepo
        self._reservationsRepo = reservationsRepo

        self._ids = []
        for i in self._reservationsRepo:
            self._ids.append(i.id)

    def list_rooms (self):
        s = ""
        for i in self._roomRepo:
            s += str(i)
            s += "\n"
        return s

    def list_reservations(self):
        s = ""
        for i in self._reservationsRepo:
            s += str(i)
            s += "\n"
        return s

    def generate_id(self):
        while True:
            id = ""
            for i in range(4):
                digit = random.choice(range(0,10))
                id += str(digit)

            if id not in self._ids:
                self._ids.append(id)
                return id

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

    def intersected_dates(self, x1, y1, x2, y2):
        if y1 < x2 or y2 < x1:
            return False
        return True


    def available_rooms_in_interval (self, d1, d2):
        rooms = range(1,11)
        rooms = list(rooms)

        arrival = self.valid_date(d1)
        departure = self.valid_date(d2)
        if arrival > departure:
            raise BadDate("Arrival larger than departure")

        for i in self._reservationsRepo:
            if self.intersected_dates(arrival, departure, i.arrival, i.departure) == True:
                rooms.remove(i.room)
        return rooms

    def available_room_of_type (self, type, d1, d2):
        availableRooms = self.available_rooms_in_interval(d1, d2)
        self.is_natural(type)

        for i in self._roomRepo:
            if i.id in availableRooms and i.type == int(type):
                return i.id

        return None

    def create_reservation (self, family, roomType, numberGuests, arrival, departure):
        room = self.available_room_of_type(roomType, arrival, departure)
        if room == None:
            raise NoRooms("There are no available rooms")
        id = self.generate_id()
        reservation = Reservation(id, room, family, numberGuests, arrival, departure)
        self._reservationsRepo.store(reservation)

    def delete_reservation(self, id):
        self.is_natural(id)
        self._reservationsRepo.delete(id)

    def available_rooms_and_room_types (self, d1, d2):
        rooms = self.available_rooms_in_interval(d1, d2)
        s = ""
        for i in self._roomRepo:
            if i.id in rooms:
                s+= str(i)
                s += "\n"
        return s

    @staticmethod
    def key (arr):
        return arr[0]

    def get_last_day(self, d):
        day = d.day
        i = 0
        while True:
            try:
                d = date(d.year, d.month, day+i)
            except:
                return i
            i += 1

    def get_first_day(self, d):
        day = d.day
        i = 0
        while True:
            try:
                d = date(d.year, d.month, day-i)
            except:
                return i
            i += 1

    def monthly_report(self):
        months = []
        for i in range(12):
            months.append([0,i])

        for i in self._reservationsRepo:
            if i.arrival.month == i.departure.month:
                days = i.departure - i.arrival
                months[i.arrival.month][0] += days.days
            else:
                months[i.arrival.month][0] += self.get_last_day(i.arrival)
                months[i.departure.month][0] += self.get_first_day(i.departure)

        months.sort(reverse=True, key=self.key)
        return months

    def week_report (self):
        days = []
        for i in range(7):
            days.append(0)

        for i in range(7):
            for res in self._reservationsRepo:
                arrival = res.arrival.weekday()
                departure = res.departure.weekday()
                print()
                print(res)
                print(arrival, departure)
                print()
                if arrival <= departure:
                    if i >= arrival and i <= departure:
                        days[i] += 1
                else:
                    if i >= arrival or i <= departure:
                        days[i] += 1
        return days



# joi ->luni : 3 4 5 6 7 0


d1 = date(2019,2, 3)
d2 = date(year=2019, month=2, day = 2)
d = d1-d2

print(d.days, type(d.days))


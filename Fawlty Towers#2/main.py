from UI import *

class Main:
    def __init__(self):
        self.roomRepo = Repository("rooms.txt", Room)
        self.reservationRepo = Repository("reservations.txt", Reservation)

        self.service = Service(self.roomRepo, self.reservationRepo)
        self.UI = UI(self.service)

        self.UI.start()

Main()
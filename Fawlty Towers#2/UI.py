from service import *

class UI:
    def __init__(self, Service):
        self._service = Service

    def UI_list_rooms(self):
        print(self._service.list_rooms())

    def UI_list_reservations(self):
        print(self._service.list_reservations())

    def UI_create_reservation(self):
        family = input("Give name: ").strip()
        roomType = input("Give room type: ").strip()
        numberGuests = input("Give number of guests: ").strip()
        arrival = input("Give arrival: ").strip()
        departure = input("Give departure: ").strip()

        try:
            self._service.create_reservation(family, roomType, numberGuests, arrival, departure)
            print("The reservation was succesfull")
        except Exception as err:
            print(err)
        """
       except BadGuests as err:
            print(err)
        except BadDate as err:
            print(err)
        except BadRoomType as err:
            print(err)
        except NoRooms as err:
            print(err)
        except NotNaturalNumber as err:
            print(err)
        except EmptyFamily as err:
            print(err)"""



    def UI_delete_reservation (self):
        id = input("Give id: ").strip()
        try:
            self._service.delete_reservation(id)
            print("The reservation was deleted succesfully")
        except IdNotFound as err:
            print (err)
        except NotNaturalNumber as err:
            print(err)

    def UI_available_rooms (self):
        arrival = input("Give first date: ").strip()
        departure = input("Give second date: ").strip()
        try:
            rooms = self._service.available_rooms_and_room_types(arrival,departure)
            if len(rooms) == 0:
                print("there are no such rooms")
            else:
                print(rooms)
        except BadDate as err:
            print(err)

    def UI_monthly_report(self):
        report  = self._service.monthly_report()
        for i in report:
            print("For month:" + str(i[1]) + " the number of reserved days is: " + str(i[0]))

    def UI_week_report (self):
        report = self._service.week_report()
        print(report)
        for i in range(7):
            print("For day: " + str(i) + " the number of reserved days is: " + str(report[i]))

    @staticmethod
    def print_menu ():
        menu = """
1. List rooms
2. List reservations
3. Create reservation
4. Delete reservation
5. Available rooms
6. Monthly report
7. Day of week report
x. Exit

        """
        print(menu)

    def start (self):
        commands = {
            "1" : self.UI_list_rooms,
            "2" : self.UI_list_reservations,
            "3" : self.UI_create_reservation,
            "4" : self.UI_delete_reservation,
            "5" : self.UI_available_rooms,
            "6" : self.UI_monthly_report,
            "7" : self.UI_week_report
        }
        while True:
            self.print_menu()
            choice = input(">").strip()
            if choice in commands:
                commands[choice]()
            elif choice == "x":
                return
            else:
                print("Invalid command")
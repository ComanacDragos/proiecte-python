import unittest
from service import *

class MyTestCase(unittest.TestCase):
    def test_domain(self):
        r = Room(1,4)
        reservation = Reservation(1234, 1, "Pop", 4, "19.02", "20.02")

        with self.assertRaises(BadRoomType):
            r = Room(1,5)

        with self.assertRaises(NotNaturalNumber):
            r = Room("ads",5)

        with self.assertRaises(NotNaturalNumber):
            r = Room(1,"asd")

        with self.assertRaises(NotNaturalNumber):
            r = Room(1.4,5)

        with self.assertRaises(EmptyFamily):
            reservation = Reservation(1234, 1, "", 4, "19.02", "20.02")

        with self.assertRaises(BadDate):
            reservation = Reservation(1234, 1, "asd", 4, "21.02", "20.02")


        with self.assertRaises(BadDate):
            reservation = Reservation(1234, 1, "asd", 4, "19.02", "2002")
        with self.assertRaises(BadDate):
            reservation = Reservation(1234, 1, "asd", 4, "22", "20.02")

        with self.assertRaises(BadDate):
            reservation = Reservation(1234, 1, "asd", 4, "31.02", "20.02")

        with self.assertRaises(NotNaturalNumber):
            reservation = Reservation(1234, "asd", "asd", 4, "21.02", "20.02")


        with self.assertRaises(NotNaturalNumber):
            reservation = Reservation(1234, "asd", "3", "asd", "21.02", "20.02")


        with self.assertRaises(NotNaturalNumber):
            reservation = Reservation(-3, "asd", "4", 4, "21.02", "20.02")

        with self.assertRaises(BadGuests):
            reservation = Reservation(1234, 1, "Pop", 5, "19.02", "20.02")

    def test_service(self):
        roomRepo = Repository("asd", Room, [Room(1,4),Room(2,2), Room(3, 1)])
        reservationRepo = Repository("asd", Reservation, [Reservation("0111", 1, "pop", 4, "19.02", "21.02")])
        service = Service(roomRepo, reservationRepo)

        availableRooms = service.available_rooms_in_interval("18.02", "20.02")
        self.assertEqual(availableRooms, [2,3,4,5,6,7,8,9,10])

        id = service.available_room_of_type(2, "18.02", "20.02")

        self.assertEqual(id,2)

        service.create_reservation("pop", 2, 4, "19.02", "20.02")
        self.assertEqual(len(reservationRepo), 2)

        service.delete_reservation("0111")
        self.assertEqual(len(reservationRepo), 1)

if __name__ == '__main__':
    unittest.main()

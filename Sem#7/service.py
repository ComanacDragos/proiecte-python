from domain import Client
class TestClientAgain (unittest.TestCase):
    def test_client (self):
        # sum interesting
        # python 3.8 introduced walrus operator -> :=
        # if (n:= len(mylist)):

        c = Client(1, "Pop Andreea", 19 )
        assert c.id == 1
        assert c.name == "Pop Andreea"
        assert c.age == 19

        try:
            c.age = 17
            assert False # should not run
        except ValueError:
            assert True # we are okay
        except Exception:
            assert False # a dif exception was raised


    def test_client_again (self):
        c = Client(1, "Pop Mihnea", 20 )
        try:
            c.age = 20
            assert False # should not run
        except ValueError:
            assert True # we are okay
        except Exception:
            assert False # a dif exception was raised

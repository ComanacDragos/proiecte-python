from service import *
class Tests:

    def __init__ (self):
        self.repo = Repository()

    @staticmethod
    def test_add_book ():
        service = Repository()
        service.add_book(Book(1,2,3))
        assert service._bookList[-1].bookId == 1 and service._bookList[-1].title == 2 and service._bookList[-1].author == 3
        try:
            service.add_book(Book(1,4,5))
            assert False
        except duplicateID:
            assert True
        else:
            assert False

        try:
            service.add_book(Book(-1,4,5))
            assert False
        except badId:
            assert True
        else:
            assert False

    @staticmethod
    def test_remove_book ():
        service =Repository()
        n = len(service._bookList)
        service.add_book(Book("1","2","3"))
        service.remove_bookID("1")
        assert len(service._bookList) == n
        try:
            service.remove_bookID("3")
            assert False
        except IdDoesNotExist:
            assert True
        else:
            assert False

    @staticmethod
    def test_update_book ():
        service = Repository()
        service.add_book(Book(1,2,3))
        service.update_book_author(1,"new")
        service.update_book_title(1,"new2")
        assert service._bookList[-1].author == "new"
        assert service._bookList[-1].title == "new2"

        try:
            service.update_book_author(2, "asd")
            assert False
        except IdDoesNotExist:
            assert True
        
        try:
            service.update_book_title(2, "asd")
            assert False
        except IdDoesNotExist:
            assert True
        
    @staticmethod
    def test_remove_client():
        service = Repository()
        service.add_client(Client("1", "bobo"))
        n = len(service._clientList)
        service.remove_client("1")
        assert len(service._clientList) == n-1
        assert service._clientList[-1].clientId != "1"
        try:
            service.remove_client(Client("2", "bobo"))
            assert False
        except:
            assert True

    @staticmethod
    def test_add_client():
        service = Repository()
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

    def test_update_client (self):
        
        self.repo.add_client(Client("1", "bobo"))
        self.repo.update_client_name("1", "newBobo")
        assert self.repo._clientList[-1].name == "newBobo"

        try:
            self.repo.update_client_name("asd", "newBobo")
            assert False
        except badId:
            assert True
        
        try:
            self.repo.update_client_name("2", "newBobo")
            assert False
        except IdDoesNotExist:
            assert True
    

    def run_tests (self):
        self.test_add_book()
        self.test_remove_book()
        self.test_update_book()
        self.test_add_client()
        self.test_remove_client()
        self.test_update_client()

test = Tests()
test.run_tests()
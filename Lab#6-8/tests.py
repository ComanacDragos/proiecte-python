from service import *
class Tests:

    @staticmethod
    def test_add_book ():
        service = ServiceBooks()
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
        service = ServiceBooks()
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
        service = ServiceBooks()
        service.add_book(Book(1,2,3))
        service.update_book_author(1,"new")
        service.update_book_title(1,"new2")
        assert service._bookList[-1].author == "new"
        assert service._bookList[-1].title == "new2"

        try:
            service.update_book_author(0, "asd")
            assert False
        except IdDoesNotExist:
            assert True
        
        try:
            service.update_book_title(0, "asd")
            assert False
        except IdDoesNotExist:
            assert True

    def run_tests (self):
        self.test_add_book()
        self.test_remove_book()
        self.test_update_book()

test = Tests()
test.run_tests()
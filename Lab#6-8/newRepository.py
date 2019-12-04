from exceptions import *
from domain import *


class Repository:
    def __init__ (self, objectList):
        self.objectList = objectList
    
    def valid_ID (self, ID):
        '''
        Cheks if the id is correct or not
        '''
        try:
            nr = float(ID)
        except:
            raise badId
        else:
            if nr <= 0 or int(nr) != nr:
                raise badId

    @property
    def get_list (self):
        return self.objectList

    def store (self, object):
        self.valid_ID(object.Id)
        for i in self.get_list:
            if i.Id == object.Id:
                raise duplicateID ("duplicate id")
        self.get_list.append(object)

    def find (self, id):
        for i in range(0, len(self.get_list)):
            if self.get_list[i].Id == id:
                return i
        raise IdDoesNotExist

    def delete (self, id):
        self.valid_ID(id)
        index = self.find(id)
        if index == None:
            raise IdDoesNotExist("No such object")
            
        self.get_list.pop(self.find(id))
    
    def __getitem__ (self, value):
        return self.get_list[value]
     

    def __len__ (self):
        return len(self.get_list)

    def sort (self):
        self.get_list.sort()

class FileRepository (Repository):
    def __init__ (self, filename, Class):
        super().__init__([])
        self._filename = filename
        self._Class = Class
        self._loadFile()

    def _loadFile (self):
        file = open(self._filename, "r")
        lines = file.readlines()
        for i in lines:
            i = i.strip()
            line = i.split(",")
            newObject = self._Class(*line)
            self.store(newObject)
        file.close()

    def _storeFile (self):
        file = open(self._filename, "w")
        for i in self.get_list():
            pass

book = Book("100","asd", "bsdf")
list = vars(book).items()
#for i in vars(book).items():
    #str += i[1]

str = "abc"
print(str)

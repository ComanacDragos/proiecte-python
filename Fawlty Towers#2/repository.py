from domain import *

class Repository:
    def __init__(self, filename, Class, data = None):
        if data != None:
            self.data = data
            return
        else:
            self.data = []
        self._filename = filename
        self._Class = Class
        self.load_file()

    def load_file (self):
        f = open(self._filename, "r")
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(",")
            self.data.append(self._Class(*line))

    def store (self, obj):
        self.data.append(obj)

    def delete (self, id):
        for i in self.data:
            if i.id == id:
                self.data.remove(i)
                return
        raise IdNotFound("The requiesd reservation does not exists")

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)




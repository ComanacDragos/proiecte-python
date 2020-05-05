from UI import *
class Main:
    def __init__(self):
        self.board = Board()
        self.service = Service(self.board)
        self.UI = UI(self.service)
        self.UI.start()

Main()


from UI import *
class Main:
    def __init__(self):
        self.service = Service()
        self.UI = UI(self.service)
        self.UI.start()

Main()




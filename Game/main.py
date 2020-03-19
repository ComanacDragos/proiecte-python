from UI import *

class Main:
    def __init__(self):
        self.board = Board()
        self.load_game()

        self.ai = AI(self.board)
        self.service = Service(self.board, self.ai)

        self.UI = UI(self.service)

        self.UI.start()

    def load_game(self):
        while True:
            choice = input("Do you want to load a game?(1/0): ")
            if choice == "1":
                filename = input("Give name: ")
                try:
                    self.board.load_board(filename)
                    return
                except:
                    print("Game not found")
            elif choice == "0":
                return
            else:
                print("invalid command")



Main()
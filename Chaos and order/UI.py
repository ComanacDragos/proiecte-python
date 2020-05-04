from service import *
class UI:
    def __init__(self, service):
        self.service = service

    def read_move(self):
        move = input(">").strip()
        if move == "save":
            filename = input("Save as: ")
            self.service.save(filename)
            return
        else:
            move = move.split(" ")

        """
        row = input("Give row number: ").strip()
        col = input("Give col number: ").strip()
        symbol = input("Give symbol: ").strip()
        """

        try:
            if len(move) != 3:
                raise BadMove("Bad command")
            self.service.human_move(*move)
            self.service.computerMove()
        except BadSymbol as err:
            print("\n" + str(err) + "\n")
        except BadColNumber as err:
            print("\n" + str(err) + "\n")
        except BadRowNumber as err:
            print("\n" + str(err) + "\n")
        except BadMove as err:
            print("\n" + str(err) + "\n")


    def start(self):
        while True:
            print(self.service.get_board())
            try:
                self.read_move()
            except ComputerWins as err:
                print(self.service.get_board())
                print(err)
                return
            except HumanWins as err:
                print(self.service.get_board())
                print(err)
                return
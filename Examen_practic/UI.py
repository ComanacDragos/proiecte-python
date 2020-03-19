from service import *
class UI:
    def __init__(self, service):
        self._service = service

    def UI_print_board(self):
        print(self._service.list_board())

    def UI_cheat(self):
        print(self._service.cheat())

    def UI_warp(self, coord):
        try:
            self._service.warp(coord)

        except BadMove as err:
            print(err)

    def UI_fire (self, coord):
        try:
            self._service.fire(coord)
        except BadMove as err:
            print(err)

    def start(self):
        self.UI_print_board()
        while True:
            command = input(">").strip()
            com = command.split(" ")

            if com[0] == "cheat":
                self.UI_cheat()
            elif com[0] == "warp":
                try:
                    self.UI_warp(com[1:])
                except GameOver as err:
                    print(err)
                    return

                self.UI_print_board()
            elif com[0] == "fire":
                try:
                    self.UI_fire(com[1:])
                except Won as err:
                    print(err)
                    return
                self.UI_print_board()
            else:
                print("invalid command")
                self.UI_print_board()



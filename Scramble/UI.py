from service import *

class UI:
    def __init__(self, service):
        self._service = service

    def UI_print_word(self):
        print(self._service.get_word())

    def read_command(self):
        command = input(">")
        return command.strip().split(" ")

    def UI_swap(self, params):
        try:
            self._service.swap(params)
        except BadCommand as err:
            print(err)

    def UI_undo (self, params):
        try:
            self._service.undo(params)
        except BadCommand as err:
            print(err)
        except DuringUndo as err:
            print(err)



    def start(self):
        while True:
            self.UI_print_word()
            command = self.read_command()
            if command[0] == "swap":
                try:
                    self.UI_swap(command[1:])
                except GameWon as err:
                    print(err)
                    self.UI_print_word()
                    return
                except GameOver as err:
                    print(err)
                    self.UI_print_word()
                    return
            if command[0] == "undo":
                self.UI_undo(command[1:])
           # else:
            #    print("Invalid command")


"""
command = input(">")
command.strip().split(" ")
print(command)"""
"""
command = input(">")
command = command.split("-")
for i in command:
    print(i)
    i = i.split(" ")
    print(i)

print(command)

l = [1,2,3,4]
print(l)
for i in range(len(l)):
    l[i] += 1
print(l)"""

from functions import *
from domain import *


def give_help (params):
    '''
    Function provides details about the commands
    '''
    if len(params) != 0:
        error_messages(9)
        return
    print ("")
    print ("For adding an expense insert the following command:")
    print("     add <apartment> <type> <amount>")
    print("")
    print("For removing one or multiple expenses insert the following commands:")
    print("     remove <apartment>")
    print("     remove <start apartment> to <end apartment>")
    print("     remove <type>")
    print("")
    print("For replacing the amount of an expense with another amount insert the following command:")
    print("     replace <apartment> <type> with <amount>")
    print("")
    print("For listing expenses insert the following commands:")
    print("     list")
    print("     list <apartment>")
    print("     list [ < | = | > ] <amount>")
    print("")
    print("For exiting the program insert the following command:")
    print("     exit")
    print("Where:")
    print("     <apartment> is the apartment id")
    print("     <type> is the expense type")
    print("     <amount> is the cost of the expense")
    print("")

def start ():
    expenses = init_expenses()
    print("")
    print("Insert <help> for information about the commands ")
    print("")
    commands = {
        "add" : add_expense,
        "remove" : remove_expense,
        "replace" : replace_amount,
        "list" : list_expenses,
        "sum" : sum
        }
    while True:
        cmdList = read_command()
        cmd = cmdList[0]
        params = cmdList[1]
        if cmd in commands:
            commands[cmd](expenses,params)
        elif cmd == "help":
            give_help(params)
        elif cmd == "exit":
            return
        else:
            print("Invalid command")
            
        
start()

from functions import *

def print_simple_array (array):
    '''
    Function prints an array in the <1. el> format
    Input:
        array - a list
    '''
    count = 1
    for i in array:
        print (str(count) + ". " + str(i))
        count = count+1

def print_two_arrays (array1, array2):
    '''
    Function prints in a specific format 2 lists
    Input parameters:
        array1 - the list of either apartment ids or expense types
        array2 - the list of amounts
    '''
    count = 0
    for i,j in zip(array1, array2):
        print("For " + str(i) + " the amount is " + str(j))

def display_expenses (expenses):
    '''
    Function prints the expenses in the <In apartment (apId) for the expense type (expenseType) the amount is (amount)> format
    Input:
        expenses - the list of expenses
    '''
    count = 1
    print("")
    for i in expenses:
        apId = get_apartmentId(i)
        expenseType = get_expenseType(i)
        amount = get_amount(i)
        print(str(count) + ". " + "In apartment " + str(apId) + " for the expense type " + expenseType + " the amount is " + str(amount))
        count = count+1
    print("")

def error_messages (error):
    '''
    Function prints error messages for a given error number
    '''
    errorList = {
        "1" : "Wrong apartment id",
        "2" : "Wrong expense type",
        "3" : "Wrong amount",
        "4" : "<to> is missing",
        "5" : "<with> is missing",
        "6" : "The left operand is bigger than the right operand",
        "7" : "There is no apartment with given id",
        "8" : "There is no apartment with given expense",
        "9" : "Wrong number of operands",
        "10": "One of < | = | > is missing ",
        #"11": "This kind of expense already exists for this apartment"
        "12" : "<apartment> or <type> is missing"
    }
    print("")
    print(errorList[str(error)])
    print("")

def give_help (params):
    '''
    Function provides details about the commands
    '''
    if len(params) != 0:
        error_messages(9)
        return
    help = """
For adding an expense insert the following command:
        add <apartment> <type> <amount>

For removing one or multiple expenses insert the following commands:
        remove <apartment>
        remove <start apartment> to <end apartment>
        remove <type>

For replacing the amount of an expense with another amount insert the following command:
        replace <apartment> <type> with <amount>

For listing expenses insert the following commands:
        list
        list <apartment>
        list [ < | = | > ] <amount>

For exiting the program insert the following command:
        exit

    For adding an expense insert the following command:
        add <apartment> <type> <amount>

For removing one or multiple expenses insert the following commands:
        remove <apartment>
        remove <start apartment> to <end apartment>
        remove <type>

For replacing the amount of an expense with another amount insert the following command: 
        replace <apartment> <type> with <amount>

For listing expenses insert the following commands:
        list
        list <apartment>
        list [ < | = | > ] <amount>

For exiting the program insert the following command:
        exit

For the sum of the amount of all expenses of a given type insert the following command
        sum <type>

For the maximum amount per each expense type for a given apartment insert the following command:
        max <apartment>

Where:
        <apartment> is the apartment id
        <type> is the expense type
        <amount> is the cost of the expense
"""
    print(help)
    
def read_command ():
    '''
    Function reads a command and splits it into the command keyword and the values of the command
    Output:
        command - command keyword
        params - the values of the command
    '''
    cmd = input("Give command: ")
    idx = cmd.find(" ")
    if idx == -1:
        return (cmd,[])
    command = cmd[:idx]
    params = cmd[idx+1:]
    params = params.split(" ")
    for i in range(len(params)):
        params[i] = params[i].strip()
    return [command,params]

def list_expenses (expenses, params):
    '''
    Function prints the required list or an error if the command is wrong
    Input:
        expenses - the list of the expenses
        params - the values of the command
    Output:
        The required list or an error message if the command is wrong
    '''

    if valid_list(params) != 0 :
        error_messages(valid_list(params))
    elif len(expenses) == 0:
        print("")
        print("There are no expenses in any apartments")
        print("")
    else:
        print ("")
        ok = 0
        if len(params) == 0:
            display_expenses(expenses)
        elif len(params) == 1:
            id = params[0]
            for i in expenses:
                if int(get_apartmentId(i)) == int(id):
                    print ("For " + str(get_expenseType(i)) + " the amount is " + str(get_amount(i)))
                    ok = 1
            if ok == 0:
                error_messages(7)

        elif len(params) == 2:
            amount = int(params[1])
            apList = empty()
            if params[0] == "<":
                for i in expenses:
                    id = int(get_apartmentId(i))
                    if sum_expenses(expenses, id) < amount:
                        append_to_array(apList,id)
                        ok = 1
                if ok == 1:
                    print ("The apartments with total expenses less than " + str(amount) + " are:")

            if params[0] == "=":
                for i in expenses:
                    id = get_apartmentId(i)
                    if sum_expenses(expenses, id) == amount:
                        append_to_array(apList,id)
                        ok = 1
                if ok == 1:
                    print ("The apartments with total expenses equal to " + str(amount) + " are:")

            if params[0] == ">":
                for i in expenses:
                    id = get_apartmentId(i)
                    if sum_expenses(expenses, id) > amount:
                        append_to_array(apList,id)
                        ok = 1
                if ok == 1:
                     print ("The apartments with total expenses more than " + str(amount) + " are:")
            
            
            if ok == 0:
                print("There are no such apartments")
            else:
                apList = list (dict.fromkeys(apList))
                apList.sort()
                print_simple_array(apList)
        print("")

def add_expense (expenses, params):
    '''
    Adds an expense to the expense list
    Input parameters :
        - expenses - the list of expenses
        - params - values of the expense
    Output:
        If the command is wrong it prints a message
    '''
    valid = valid_expense(expenses, params)
    if valid != 0:
        error_messages(valid)
    else:
        expense = create_expense(int(params[0]), params[1], int(params[2]))
        append_to_array(expenses, expense)
        print("")
        print("The expense was added succesfully")   
        print("")

def remove_expense (expenses, params):
    '''
    Removes a expense or multiple expenses from the list of expenses
    Input parameters:
        expenses - list of expenses
        params - values that need to be removed
    Output:
        If the command is wrong a message is printed
    '''
    ok = 0
    valid = valid_removal(params)
    if valid != 0:
        error_messages(valid)
    else:

        if params[0] in expenses_types():
            expenseType = params[0]
            i = 0
            n = len(expenses)
            while i < n:
                if expenseType == get_expenseType(expenses[i]):
                    remove_el(expenses,expenses[i])
                    n = n-1
                    ok = 1
                else:
                    i = i+1
                
        else:
            first = int(params[0])
            if len(params) == 3:
                last = int(params[2])
            else:
                last = first
            i = 0
            n = len(expenses)
            while i < n:
                id = get_apartmentId(expenses[i])
                if id >= first and id <= last:
                    remove_el(expenses,expenses[i])
                    n = n-1
                    ok = 1
                else:
                    i = i+1
        if ok == 0:
            print("")
            print("The requested expenses do not exist")
            print("")
        else:
            print("")
            print("The expenses were removed succesfully")
            print("")

def replace_amount (expenses, params):
    '''
    Replaces the amount of an expense for a given apartment
    Input :
        params - the values of the command
    '''
    valid = valid_replace(params)
    if valid != 0:
        error_messages(valid)
    else:
        ok = 0
        for i in expenses:
            id = get_apartmentId(i)
            expType = get_expenseType(i)
            if int(params[0]) == int(id) and params[1] == expType:
                set_amount(i, params[3])
                ok = 1
                break
        if ok == 0:
            print ("The requested expense does not exist")
        else:
            print("")
            print("The amount was replaced succesfully")
            print("")

def sum (expenses,params):
    '''
    Function writes the total amount for the expenses having a given type
    Input:
        expenses - the list of expenses
        params - the operands of the command
    '''
    valid = valid_sum(params)
    if valid != 0:
        error_messages(valid)
    else:
        expenseType = params[0]
        s = sum_expenses_types(expenses, expenseType)
        if s == 0:
            print("")
            print("There are no apartments with given expense")
            print("")
        else:
            print("")
            print("The total amount for this expense type is: " + str(s))
            print("")

def max (expenses, params):
    '''
    Write the maximum amount per each expense type for a given apartment
    Input parameters:
        expenses - the list of expesnes
        params - the apartment id
    '''
    valid = valid_max(params)
    if valid != 0:
        error_messages(valid)
    else:
        print("")
        apId = int(params[0])
        exp_types = expense_types_for_ap(expenses, apId)
        if len(exp_types) == 0:
            print("There are no expenses for this apartment")
        else:
            for i in exp_types:
                mx = max_amount(expenses, apId, i)
                print("For "+ i + " the maximum amount is " + str(mx))
        print("")
                
def sort (expenses, params):
    '''
    Function prints the list of apartments sorted ascending by total amount of expenses or the total amount of expenses for each type, sorted ascending by amount of
    money
    Input parameters:
        expenses - the list of expenses
        params - apartment / type
    '''
    valid = valid_sort(params)
    if valid != 0:
        error_messages(valid)
    elif len(expenses) == 0:
         print("\nThere are no expenses in any apartment \n")
    else:
        
        print("")
        sort = params[0]
        if sort == "apartment":
            apList = sort_apartment(expenses)
            print_two_arrays(apList[0], apList[1])
        else:
            expensesList = sort_types(expenses)
            print_two_arrays(expensesList[0], expensesList[1])
        print("")

     



def start ():
    expenses = init_expenses()
    print("\nInsert <help> for information about the commands \n")
    commands = {
        "add" : add_expense,
        "remove" : remove_expense,
        "replace" : replace_amount,
        "list" : list_expenses,
        "sum" : sum,
        "max" : max,
        "sort": sort
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
            print("\nInvalid command\n")
            
start()


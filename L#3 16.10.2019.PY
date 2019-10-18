def create_expense (apartmentId,expenseType,amount):
    dict = {
        "apartmentId" : apartmentId,
        "expenseType" : expenseType,
        "amount" : amount
    }
    return dict

def test_create_expense ():
    e = create_expense(1,"water",40)
    assert get_apartmentId(e) != 1
    assert get_expenseType(e) != "water"
    assert get_amount(e) != 40
test_create_expense


def get_apartmentId (apartment):
    return apartment["apartmentId"]

def get_expenseType (apartment):
    return apartment["expenseType"]

def get_amount (apartment):
    return apartment["amount"]

def set_apartmentId (apartment, newId):
    apartment["apartmentId"] = newId

def set_expenseType (apartment,newExpenseType):
    apartment["expenseType"] = newExpenseType

def set_amount (apartment,newAmount):
    apartment["amount"] = newAmount

def empty ():
    return []

def append_to_array (array,value):
    array.append(value)

def remove_el (array,value):
    array.remove(value)

def expenses_types():
    return  ["water", "heating", "electricity", "gas", "other"]

# LIST feature

def valid_list (params):
    if len(params) == 1:
        try:
            id = int(params[0])
        except:
            return 0
        else:
            if id <= 0:
                return 0
    elif len(params) == 2:
        if params[0] not in ["<", "=", ">"]:
            return 0
        try:
            amount = int (params[1])
        except:
            return 0
        else:
            if amount <= 0 :
                return 0
    else:
        if len(params) > 2:
            return 0    
    return 1

def display_expenses (expenses,params):
    count = 1
    print("")
    for i in expenses:
        apId = get_apartmentId(i)
        expenseType = get_expenseType(i)
        amount = get_amount(i)
        print(str(count) + ". " + "In apartment " + str(apId) + " for the expense type " + expenseType + " the amount is " + str(amount))
        count = count+1
    print("")

def test_valid_list ():
    assert valid_list ([15]) == 1
    assert valid_list (["<", 10]) == 1
    assert valid_list (["15"]) == 1
    assert valid_list ([-15]) == 0
    assert valid_list (["-15"]) == 0
    assert valid_list ([">", -10]) == 0
    assert valid_list (["="]) == 0
    assert valid_list (["=",1,2,3]) == 0
    assert valid_list (["="]) == 0


def read_command ():
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


# ADD expense feature

def valid_expense (expenses, params):
    '''
    Checks if an expense has a valid format
    input params:
        params - the expense
    output :
        1 - valid data
        0 - invalid data
    '''
    try:
        apartmentId = int(params[0])
        expenseType = params[1]
        amount = int(params[2])
    except:
        return 0
    else:
        if apartmentId <= 0 or amount <= 0:
            return 0
        if expenseType not in expenses_types():
            return 0
        for i in expenses:
            if apartmentId == get_apartmentId(i) and expenseType ==  get_expenseType(i):
                return 0
    return 1
   
def add_expense (expenses, params):
    '''
    Adds an expense to the expense list
    Input parameters :
        - expenses - the list of expenses
        - params - values of the expense
    '''
    if len(params) != 3 or valid_expense(expenses, params) == 0:
        print("Invalid data")
    else:
        expense = create_expense(int(params[0]), params[1], int(params[2]))
        append_to_array(expenses, expense)     

def test_valid_expense ():
    '''
    Tests if the valid_expense function gives correct outputs
    '''    
    exp = empty ()
    assert valid_expense(exp,[1,"water", 3]) == 1
    assert valid_expense(exp,[-1, "water", 3]) == 0
    assert valid_expense(exp,[1,"awt",3]) == 0
    assert valid_expense (exp,[1, "heating", "asf"]) == 0
    assert valid_expense (exp,[]) == 0
    assert valid_expense (exp,[1, "heating"]) == 0
    assert valid_expense (exp,[1, "heating", -4]) == 0
    assert valid_expense (exp,[1, "heatg", 3]) == 0
    assert valid_expense (exp,[1, "heatg", 3, 4]) == 0

test_valid_expense()


# REMOVE expenses feature

def valid_removal (params):
    '''
    Checks if an removal command has a valid format
    input params:
        params - the values of the removal command
    output :
        1 - valid data
        0 - invalid data
    '''
    if len(params) == 1:
        if params[0] in expenses_types():
            return 1
        try:
            ap = int(params[0])
        except:
            return 0
        else:
            if ap <= 0:
                return 0
    elif len(params) == 3:
        try:
            first = int(params[0])
            last = int(params[2])
        except:
            return 0
        else:
            if first <= 0 or last <= 0 or first > last:
                return 0
            if params[1] != "to":
                return 0
    else:
        return 0
            
    return 1

def remove_expense (expenses, params):
    '''
    Removes a expense or multiple expenses from the list of expenses
    Input parameters:
        expenses - list of expenses
        params - values that need to be removed
    '''
    ok = 0
    if valid_removal(params) == 0:
        print("Invalid data")
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
            print("The requested expenses do not exist")
            
def test_valid_removal ():
    assert valid_removal([10]) == 1
    assert valid_removal([1,"to",10]) == 1
    assert valid_removal([1,"too",10]) == 0
    assert valid_removal(["gaas"]) == 0
    assert valid_removal([-1,"to",3]) == 0
    assert valid_removal([1,2]) == 0
    assert valid_removal([]) == 0
    assert valid_removal([3,"to","ASD"]) == 0
    assert valid_removal([3,"to",-3]) == 0
    assert valid_removal(["asd","to",3]) == 0
    assert valid_removal([4,"to",3]) == 0
    assert valid_removal(["asd",3,"asd"]) == 0
    assert valid_removal(["gaas"]) == 0
    assert valid_removal(["gas"]) == 1
    assert valid_removal(["gas",2]) == 0
test_valid_removal()



# REPLACE feature

def valid_replace (params):
    '''
    Checks if an replace command has valid parameters 
    Input - params - the list of parameters
    Output :
        1 - valid data 
        0 - invalid data
    '''
    if len(params) != 4:
        return 0
    if params [2] != "with":
        return 0
    if params[1] not in expenses_types():
        return 0
    try:
        apId = int(params[0])
        newAmount = int(params[3])
    except:
        return 0
    else:
        if apId <= 0 or newAmount <= 0:
            return 0
    return 1

def replace_amount (expenses, params):
    '''
    Replaces the amount of an expense for a given apartment
    Input :
        params - the values of the command
    '''
    if valid_replace(params) == 0:
        print("Invalid data")
    else:
        ok = 0
        for i in expenses:
            id = get_apartmentId(i)
            expType = get_expenseType(i)
            if int(params[0]) == int(id) and params[1] == expType:
                set_amount(i, params[3])
                ok = 1
        if ok == 0:
            print ("The requested expense does not exist")

def test_valid_replace ():
    assert valid_replace(["12","gas","with","20"]) == 1
    assert valid_replace(["12","gas","with","20","32"]) == 0
    assert valid_replace(["12","ga","with","200"]) == 0
    assert valid_replace(["12","gas","o","200"]) == 0
    assert valid_replace(["12","gas","with","-200"]) == 0
    assert valid_replace(["-12","gas","with","200"]) == 0
    assert valid_replace(["12","gas","with","fgh"]) == 0
    assert valid_replace(["hjk","gas","with","200"]) == 0
    assert valid_replace(["12","gas","with"]) == 0
test_valid_replace()

def init_expenses ():
    '''
    Initializes a list of expenses
    '''
    expenses = empty()
    add_expense(expenses,[100,"water",40])
    add_expense(expenses,[101,"electricity",60])
    add_expense(expenses,[102,"other",20])
    add_expense(expenses,[100,"heating",45])
    add_expense(expenses,[101,"gas",100])
    return expenses

def start ():
    expenses = init_expenses()
    commands = {"add" : add_expense, "remove" : remove_expense, "replace" : replace_amount, "list" : display_expenses}
    while True:
        cmdList = read_command()
        cmd = cmdList[0]
        params = cmdList[1]
        if cmd in commands:
            commands[cmd](expenses,params)
        elif cmd == "exit":
            return
        else:
            print("Invalid command")
            
        
start()

from domain import *

#LIST feature

def valid_list (params):
    '''
    Checks if the list command has a valid format
    Input :
        params: command values
    Output:
        0 - valid data
        1 - wrong apartment id
        3 - wrong amount
        9 - wrong number of operands
        10 - < | = | > is missing
    '''
    if len(params) == 1:
        try:
            id = int(params[0])
        except:
            return 1
        else:
            if id <= 0:
                return 1
    elif len(params) == 2:
        if params[0] not in ["<", "=", ">"]:
            return 10
        try:
            amount = int (params[1])
        except:
            return 3
        else:
            if amount <= 0 :
                return 3
    else:
        if len(params) > 2:
            return 9    
    return 0

def test_valid_list ():
    assert valid_list ([15]) == 0
    assert valid_list (["<", 10]) == 0
    assert valid_list (["15"]) == 0
    assert valid_list ([-15]) == 1
    assert valid_list (["-15"]) == 1
    assert valid_list ([">", -10]) == 3
    assert valid_list (["="]) == 1
    assert valid_list (["=",1,2,3]) == 9
    assert valid_list (["asd"]) == 1
    assert valid_list([]) == 0
    assert valid_list(["1231","1231323"]) == 10
test_valid_list()

def sum_expenses (expenses, apId):
    sum = 0
    for i in expenses:
        if get_apartmentId(i) == apId:
            sum = sum + get_amount(i)
    return sum

def test_sum_expenses ():
    exp = []
    append_to_array(exp,create_expense(1,"gas",2))    
    append_to_array(exp,create_expense(1,"other",2))
    append_to_array(exp,create_expense(1,"electricity",2))
    append_to_array(exp,create_expense(1,"water",2))
    assert sum_expenses(exp,1) == 8 

# ADD expense feature

def valid_expense (expenses, params):
    '''
    Checks if an expense has a valid format
    input params:
        params - the expense
    output :
        0 - valid data
        1 - wrong apartment id
        2 - wrong expense type
        3 - wrong amount
        9 - wrong number of operands
        11 - this kind of expense already exists
    '''
    if len(params) != 3 :
        return 9
    try:
        apartmentId = int(params[0])
    except:
        return 1
    else:
        if apartmentId <= 0:
            return 1
    try:
        expenseType = params[1]
    except:
            return 2
    else:
        if expenseType not in expenses_types():
            return 2
        for i in expenses:
            if apartmentId == get_apartmentId(i) and expenseType ==  get_expenseType(i):
                return 11
    try:
        amount = int(params[2])
    except:
        return 3
    else:
        if amount <= 0:
            return 3
    return 0

def test_valid_expense ():
    '''
    Tests if the valid_expense function gives correct outputs
    '''    
    exp = empty ()
    assert valid_expense(exp,[1,"water", 3]) == 0
    assert valid_expense(exp,[-1, "water", 3]) == 1
    assert valid_expense(exp,[1,"awt",3]) == 2
    assert valid_expense (exp,[1, "heating", "asf"]) == 3
    assert valid_expense (exp,[]) == 9
    assert valid_expense (exp,[1, "heating"]) == 9
    assert valid_expense (exp,[1, "heating", -4]) == 3
    assert valid_expense (exp,[1, "heatg", 3]) == 2
    assert valid_expense (exp,[1, "heatg", 3, 4]) == 9
test_valid_expense()

# REMOVE expenses feature

def valid_removal (params):
    '''
    Checks if an removal command has a valid format
    input params:
        params - the values of the removal command
    output :
        0 - valid data
        natural number - invalid data
    '''
    if len(params) == 1:
        if params[0] in expenses_types():
            return 0
        try:
            ap = int(params[0])
        except: 
            return 1
        else:
            if ap <= 0:
                return 1
    elif len(params) == 3:
        try:
            first = int(params[0])
            last = int(params[2])
        except:
            return 1
        else:
            if first <= 0 or last <= 0:
                return 1
            if first > last:
                return 6
            if params [1] !="to":
                return 4
    else:
        return 9
    return 0

def test_valid_removal ():
    assert valid_removal([10]) == 0
    assert valid_removal([1,"to",10]) == 0
    assert valid_removal([1,"too",10]) == 4
    assert valid_removal(["gaas"]) == 1
    assert valid_removal([-1,"to",3]) == 1
    assert valid_removal([1,2]) == 9
    assert valid_removal([]) == 9
    assert valid_removal([3,"to","ASD"]) == 1
    assert valid_removal([3,"to",-3]) == 1
    assert valid_removal(["asd","to",3]) == 1
    assert valid_removal([4,"to",3]) == 6
    assert valid_removal(["asd",3,"asd"]) == 1
    assert valid_removal(["gaas"]) == 1
    assert valid_removal(["gas"]) == 0
    assert valid_removal(["gas",2]) == 9
test_valid_removal()

# REPLACE feature

def valid_replace (params):
    '''
    Checks if an replace command has valid parameters 
    Input - params - the list of parameters
    Output :
        1 - valid data 
        natural number - invalid data
    '''
    if len(params) != 4:
        return 9
    try:
        apId = int (params[0])
    except:
        return 1
    else: 
        if apId <= 0:
            return 1
    if params[1] not in expenses_types():
        return 2
    try:
        newAmount = int(params[3])
    except:
        return 3
    else:
        if newAmount <= 0:
            return 3
    if params [2] != "with":
        return 5
    return 0

def test_valid_replace ():
    assert valid_replace(["12","gas","with","20"]) == 0
    assert valid_replace(["12","gas","with","20","32"]) == 9
    assert valid_replace(["12","ga","with","200"]) == 2
    assert valid_replace(["12","gas","o","200"]) == 5
    assert valid_replace(["12","gas","with","-200"]) == 3
    assert valid_replace(["-12","gas","with","200"]) == 1
    assert valid_replace(["12","gas","with","fgh"]) == 3
    assert valid_replace(["hjk","gas","with","200"]) == 1
    assert valid_replace(["12","gas","with"]) == 9
test_valid_replace()

# SUM feature

def valid_sum (params):
    '''
    Checks if the sum command has valid parameters
    Input:
        params - the operands of the command
    Output:
        0 - valid data
        natural number - invalid data
    '''
    if len(params) != 1:
        return 9
    if params[0] not in expenses_types():
        return 2
    return 0

def test_valid_sum ():
    assert valid_sum(["gas"]) == 0
    assert valid_sum([1]) == 2
    assert valid_sum(["1"]) == 2
    assert valid_sum([]) == 9
    assert valid_sum([""]) == 2
    assert valid_sum([1,2]) == 9
test_valid_sum()



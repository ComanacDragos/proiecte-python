class duplicateID (Exception):
    '''
    Duplicate bookId exception
    '''
    pass

class IdDoesNotExist (Exception):
    '''
    Required id does not exist
    '''
    pass

class badId (Exception):
    '''
    The book id is not a natural number
    '''
    pass
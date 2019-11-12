from domain import *

'''
0. writing domain classes
1. unit testing the proper way
2. a new layer? repository

Assignment 01 - 05

    ui -> service -> domain
        -> domain
    
    ui 
        - user interface for entire program
    service 
        - functions that solve the problem
    repository
        - manage lisft of domain entitites
    domain
        - entitites from problem domain


    ui  -> service  -> repository -> domain
                    -> domain
        -> domain
'''



'''
 write a client repository class:
    - it keeps a list of clients (private)
    - funtion to add a new client (raise exception if client with same id already in repo)
    - function returns all clients
'''
import copy

class clientRepository:
    def __init__ (self):
        self._data =  []
    
    def store (self, client):
        pass

    def delete (self, clientID):
        pass

    def find (self, clientID):
        pass

    def getAll (self):
        #maybe copy here for safety
        # returns a reference to the live list
        return self._data

        return self._data[:]
        #even safer
        return copy.deepcopy(self._data) 
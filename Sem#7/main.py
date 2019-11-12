from repository import *

clientRepo = clientRepository()

#service needds a repository that stores entitites
clientService = ClientService(clientRepo)


#UI will talk to a client service

ui = UI(clientService)
ui.start()
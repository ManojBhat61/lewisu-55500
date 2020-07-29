#for python 2.7
#from SimpleXMLRPCServer import SimpleXMLRPCServer
#from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

#using python 3.7
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create airline server
server = SimpleXMLRPCServer(('localhost', 55501), allow_none=True)
server.register_introspection_functions()

import pandas as pd

#Create initial list of Airline availability
# number, Airline, From, To, bookedYN
#
Airlines = pd.DataFrame([
    ['1','AA','Chicago','LA', 'N'], 
    ['2','AA','Chicago','San Francisco', 'N'], 
    ['3','UA','Chicago','New York', 'N'], 
    ['4','UA','Chicago','Newark', 'N'],
    ['5','Delta','Chicago','Salt Lake City', 'N']],
	
    columns = ['AirlineID','AirlineName','FromCity','ToCity','BookedYesOrNo'])

Reservations = pd.DataFrame([ ['','','']], columns = ['ResID','AirlineID','Name'])
resCount = 0
	
#Start with printing the initial list of availability
#print ''
#print 'Current List of airline tickets'
#print ''
#print Airlines

class AirlineFunctions:
    # get list of tickets
    def GetList(self):
        print (' In the AirlineServer GetList function'	    )
        print (Airlines)
        print (' ========================')
        return Airlines.to_string()


    # get list of reservations
    def GetReservationList(self):
        print (' In the AirlineServer GetReservationList function'	  )
        print (Reservations)
        print (' ========================')
        return Reservations.to_string()

		#Create a reservation
    def AddReservation(self, ID, Name):
       global Reservations       
       global resCount
       print (' In the AirlineServer AddReservation function'	    )
       resCount = resCount + 1
       Add = pd.DataFrame([[resCount, ID, Name]],columns = ['ResID','AirlineID','Name'])
       Reservations = Reservations.append(Add, ignore_index=True)
       print ('')
       print ('Updated Airline Reservation List')
       print ('')
       print (Reservations)
       print (' ========================')
       return True

    #Create a function to remove one reservation
    def RemoveReservation(self, Index):
        global Reservations
        print (' In the AirlineServer RemoveReservation function'	  )
        Reservations = Reservations.drop(Reservations.index[Index])
        print ('')
        print ('Updated Airline Reservation List')
        print ('')
        print (Reservations)
        print (' ========================')
        return True

    
resCount = 0
server.register_instance(AirlineFunctions())

print (' Airline Server is ready to accept calls....')

# Run the server's main loop
server.serve_forever()


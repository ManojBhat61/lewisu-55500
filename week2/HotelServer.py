from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)    
#    rpc_paths = ('/hotel',)

# Create hotel server
server = SimpleXMLRPCServer(('localhost', 55502), allow_none=True)
server.register_introspection_functions()

import pandas as pd

#Create initial list of hotel availability
# number, hotel, From, To, bookedYN
#
hotels = pd.DataFrame([
    ['1','Holiday Inn','LA', '1/1/2018', '3/1/2018', 'N'], 
    ['2','Holiday Inn','San Franciso', '1/1/2018', '3/1/2018', 'N'], 
    ['3','Holiday Inn','New York', '1/1/2018', '3/1/2018', 'N'], 
    ['4','Holiday Inn','Newark', '1/1/2018', '3/1/2018', 'N'], 
    ['5','Holiday Inn','Chicago', '1/1/2018', '3/1/2018', 'N']], 
    columns = ['hotelID','hotelName','City', 'From','To','BookedYesOrNo'])

Reservations = pd.DataFrame([ ['','','','','']], columns = ['ResID','hotelID','Name', 'FromDate', 'ToDate'])
resCount = 0
	
class hotelFunctions:
    # get list of hotels
    def GetList(self):
        print(' In the HotelServer GetList function')	    
        print(hotels)
        print(' ========================')
        return hotels.to_string()


    # get list of reservations
    def GetReservationList(self):
        print(' In the HotelServer GetReservationList function')	    
        print(Reservations)
        print(' ========================')
        return Reservations.to_string()

		#Create a reservation
    def AddReservation(self, ID, Name, FromDt, ToDt):
       global Reservations       
       global resCount
       print(' In the HotelServer AddReservation function')	    
       resCount = resCount + 1
       Add = pd.DataFrame([[resCount, ID, Name, FromDt, ToDt]],columns = ['ResID','hotelID','Name','FromDate','ToDate'])
       Reservations = Reservations.append(Add, ignore_index=True)
       print('')
       print('Updated hotel Reservation List')
       print('')
       print(Reservations)
       print(' ========================')
       return True

    #Create a function to remove a reservation
    def RemoveReservation(self, Index):
        global Reservations
        print(' In the HotelServer RemoveReservation function')	  
        Reservations = Reservations.drop(Reservations.index[Index])
        print('')
        print('Updated hotel Reservation List')
        print('')
        print(Reservations)
        print(' ========================')
        return True

    
resCount = 0
server.register_instance(hotelFunctions())

print(' hotel Server is ready to accept calls....')

# Run the server's main loop
server.serve_forever()


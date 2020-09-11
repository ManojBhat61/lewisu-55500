#for python 2.7
#from SimpleXMLRPCServer import SimpleXMLRPCServer
#from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# for Python 3.x
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create Car server
server = SimpleXMLRPCServer(('localhost', 55503), allow_none=True)
server.register_introspection_functions()

import pandas as pd

#Create initial list of Car availability
# number, Car, Location, Rate, bookedYN
#
Cars = pd.DataFrame([
    ['1','Avis','Chicago','$100', 'N'], 
    ['2','Hertz','Chicago','$50', 'N'], 
    ['3','Budget','Chicago','$200', 'N'], 
    ['4','Avis','Chicago','$20', 'N'],
    ['5','Avis','Chicago','$30', 'N']],
    columns = ['CarID','Company','Location','Rate','BookedYesOrNo'])

Reservations = pd.DataFrame([ ['','','']], columns = ['ResID','CarID','Name'])
resCount = 0
	
#Start with printing the initial list of availability
#print ''
#print 'Current List of rental Cars '
#print ''
#print Cars

class CarFunctions:
    # get list 
    def GetList(self):
        print (' In the CarServer GetList function')
        print (Cars)
        print (' ========================')
        return Cars.to_string()


    # get list of reservations
    def GetReservationList(self):
        print(' In the CarServer GetReservationList function')
        print (Reservations)
        print (' ========================')
        return Reservations.to_string()

		#Create a reservation
    def AddReservation(self, ID, Name):
       global Reservations       
       global resCount
       print (' In the CarServer AddReservation function')
       resCount = resCount + 1
       Add = pd.DataFrame([[resCount, ID, Name]],columns = ['ResID','CarID','Name'])
       Reservations = Reservations.append(Add, ignore_index=True)
       print ('')
       print ('Updated Car Reservation List')
       print ('')
       print (Reservations)
       print (' ========================')
       return True

    #Create a function to remove one reservation
    def RemoveReservation(self, Index):
        global Reservations
        print (' In the CarServer RemoveReservation function')
        Reservations = Reservations.drop(Reservations.index[Index])
        print ('')
        print ('Updated Car Reservation List')
        print ('')
        print (Reservations)
        print (' ========================')
        return True

    
resCount = 0
server.register_instance(CarFunctions())

print (' Car Server is ready to accept calls....')

# Run the server's main loop
server.serve_forever()


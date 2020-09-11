#for python 2.7
#from SimpleXMLRPCServer import SimpleXMLRPCServer
#from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

#using python 3.7
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

import pandas as pd
import pymongo    # <<<<< changes >>>>>>
import sys

from pymongo import MongoClient    # <<<<< changes >>>>>>

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create airline server
server = SimpleXMLRPCServer(("192.168.xx.yy", 55501), allow_none=True)   #update IP address 
server.register_introspection_functions()


resCount = 0
	
class AirlineFunctions:
    # get list of Airlines
    def GetList(self):
        print (" In the GetList function")
        try:		
           # connect to the MongoDB server
           client = MongoClient('192.168.x.y', 27017, username='xxx', password='yyy')     # <<<<< changes >>>>>>

           # get the database	
           db = client.Vacation       # <<<<<=============
        
           # get the collection
           collection = db.Airlines      # <<<<<=============
		
           # retrieve all records		
           cursor =  collection.find()   # <<<<<=============
        
		   #convert to DataFrame
           airlines = pd.DataFrame(list(cursor))     # <<<<<=============
        

           print ('========================')
           return airlines.to_string()
        except:
           print ('Could not connect to MongoDB: ' )
           sys.exit()		   


    #Create a reservation
    def AddReservation(self, ID, Name):
       global resCount
       print (" In the AddReservation function"	    )
       resCount = resCount + 1
	   
       #update the airline record
       try:		
         client = MongoClient('192.168.x.y', 27017, username='xxx', password='yyy')     # <<<<< changes >>>>>>
		 
         # get the database	
         db = client.Vacation

         # get the collection
         collection = db.Airlines
		
         # update the airline row by setting the flag to Y
         cursor =  collection.update({'FLIGHT':ID}, {"$set" : {"bookedYN" : "Y"}})     # <<<<<=============

         #create a new reservation object and add to the table	   
         newres = {"ResID" : resCount, "AirlineID" : ID, "Name" : Name }
         db.reservations.insert(newres)
		 
         print ("")
         print ("Airline Airlines updated. New reservation added. ")
         print ("")
         return 'Added reservation'
         print (' ========================')
       except Exception as e:
          print(('Something happened %s' % e))
          return ('Error in updating record : ' )

    #Create a function to remove one reservation
    def RemoveReservation(self, ID):
        
        print (" In the AddReservation function"	  )
        #update the airline record
        try:		
            client = MongoClient('192.168.x.y', 27017, username='xxx', password='yyy')     # <<<<< changes >>>>>>
        except:
          print ('Could not connect to MongoDB: ' )
          sys.exit()		   

        # get the database	
        db = client.Vacation
        # get the Airlines collection
        collection = db.Airlines
        rescoll = db.reservations

        # update the airline row by setting the flag to N
        cursor =  collection.update({'FLIGHT':ID}, {"$set" : {"bookedYN" : "N"}})

        #delete the reservation
        db.reservations.delete_one( {"AirlineID" : ID })
        
       
        print ("")
        print ("Updated Airline Reservation List")
        print ("")
        print (' ========================')
        return True

    
resCount = 0
server.register_instance(AirlineFunctions())

print (" Airline Server is ready to accept calls....")


#  to test the code without a client calling a function 
try:		
	# connect to the MongoDB server
    client = MongoClient('192.168.x.y', 27017, username='xxx', password='yyy')     # <<<<< changes >>>>>>

    # get the database	
    db = client.Vacation      
            
    # get the collection
    collection = db.Airlines  
    print (collection)

    print(('=== number of docs in the collection = ' +   str(collection.count())))
    # retrieve all records		
    cursor =  collection.find()   # <<<<<=============
	
    print (cursor)
    airlines = pd.DataFrame(list(cursor))    
    print (airlines)
	
except:
    print ('Could not connect to MongoDB: ' )
    sys.exit()		   


# Run the server's main loop
server.serve_forever()


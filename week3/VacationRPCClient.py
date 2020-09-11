import xmlrpc.client  #(python 3)
import sys

#  Testing airline server
try:
    airlineServer = xmlrpc.client.ServerProxy('http://localhost:55501')
    hotelServer   = xmlrpc.client.ServerProxy('http://localhost:55502')
    carServer     = xmlrpc.client.ServerProxy('http://localhost:55503')
except Exception as e:
    print(e)
    sys.exit(1)

print ('======================')
print(' *** Testing Airline Server ***')
print ('======================')
print ('calling Get list of reservations')
listOfAirlines = airlineServer.GetList()
print(listOfAirlines) 

# call function to add a reservation
print ('calling Airline AddReservation')
airlineServer.AddReservation(1, 'John Doe')
airlineServer.AddReservation(2, 'Jane Doe')
airlineServer.AddReservation(3, 'Jack Doe')

print ('calling delete Airline reservation')
# cancel a reservation
airlineServer.RemoveReservation(1)

#############################################################
print ('======================')
print(' *** Testing Hotel Server ***')
print ('======================')
print ('calling Get list of reservations')
listOfHotels  = hotelServer.GetList()
print(listOfHotels) 

# call function to add a reservation
print ('calling Hotel AddReservation')
hotelServer.AddReservation(1, 'John Doe', '1/1/2018', '3/1/2018')
hotelServer.AddReservation(2, 'Jane Doe', '1/1/2018', '3/1/2018')
hotelServer.AddReservation(3, 'Jack Doe', '1/1/2018', '3/1/2018')
print ('======================')


print ('calling delete Hotel reservation')
# cancel a reservation
hotelServer.RemoveReservation(1)

#############################################################
print ('======================')
print(' *** Testing Car Server ***')
print ('======================')
print ('calling Get list of reservations')
listOfCars  = carServer.GetList()
print(listOfCars) 

# call function to add a reservation
print ('calling Car AddReservation')
carServer.AddReservation(1, 'John Doe')
carServer.AddReservation(2, 'Jane Doe')
carServer.AddReservation(3, 'Jack Doe')
print ('======================')


print ('calling delete Car reservation')
# cancel a reservation
carServer.RemoveReservation(1)

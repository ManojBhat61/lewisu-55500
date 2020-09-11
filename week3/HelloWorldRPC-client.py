import xmlrpc.client  
#import xmlrpclib  #(python 2.7)

s = xmlrpc.client.ServerProxy('http://localhost:55500')
print(s.Greeting('World')) 
print(s.Greeting('John')) 


# Print list of available methods
# print(s.system.listMethods())

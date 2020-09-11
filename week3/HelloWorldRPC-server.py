
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 55500), requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def Greeting(str):
    return 'Hello ',str

 
server.register_function(Greeting, 'Greeting')

# Run the server's main loop
server.serve_forever()


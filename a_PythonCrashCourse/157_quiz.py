#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        # connections[connection_id] = connection_load
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load
        # print('\t{l}'.format(l=connection_load))


    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections.keys():
            del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#

server = Server()
server.add_connection("192.168.1.1")
print('your output is a random number between 1 and 10:')
print(server.load(),end='\n'*2)

server.close_connection("192.168.1.1")
print('your output should be 0:')
print(server.load(),end='\n'*2)

#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        # connections[connection_id] = server
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[connection_id] = server

        # Add the connection to the server
        server.add_connection(connection_id)

        # ensure_availability
        self.ensure_availability()


    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        if connection_id in self.connections.keys():
            # Find out the server for that connection-id
            server = self.connections[connection_id]

            # Close the connection on the server
            server.close_connection(connection_id)

            # Remove the connection from the load balancer
            del self.connections[connection_id]

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        result = 0
        for c, s in self.connections.items():
            load = s.connections[c]
            result += load
            #print('\t{l}'.format(l=load))
        # same as before using list comprehension
        result = sum(s.connections[c] for c, s in self.connections.items())
        return result/len(self.servers)

    def avg_load_2(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        result = 0
        for s in self.servers:
            #for load in s.connections.values():
                #result += load
            result += sum([load for load in s.connections.values()])
        return result/len(self.servers)

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        while (self.avg_load() > 50):
            l.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
l.add_connection("fdca:83d2::f20d222")

print('your output > 0:')
print(l.avg_load(),end='\n'*2)
print(l.avg_load_2(),end='\n'*2)

l.close_connection("fdca:83d2::f20d222")
print(l.avg_load(),end='\n'*2)


print('your output half of before:')
l.servers.append(Server())
print(l.avg_load(),end='\n'*2)

l = LoadBalancing()
for connection in range(20):
    l.add_connection(connection)
#print(l)
print('connections:{}'.format(len(l.connections)))
print('servers:{}'.format(len(l.servers)))
print('ave load:{}'.format(l.avg_load()))


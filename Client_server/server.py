# import socket
# import threading
#
#
# PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
# ADDR = (SERVER,PORT)
# print (SERVER)
# print (socket.gethostname())
# print(ADDR)

import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port

server = socket.gethostbyname(socket.gethostname())
# server = '10.42.1.194'
print (server)

server_address = (server, 12345)

# Bind the server to the address and port
server_socket.bind(server_address)

# Listen for incoming connections (maximum 5 clients in the queue)
server_socket.listen(5)
print("Server Moonton is listening on {}:{}".format(*server_address))

while True:
    # Wait for a connection from a czlient
    client_socket, client_address = server_socket.accept()
    print("Received connection from {}:{}".format(*client_address))

    # Handle the client request
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received data: {}".format(data.decode()))

    # Send a response back to the client
    response = ("Halo Codashop, id tersebut Tidak Ditemukan")
    client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()
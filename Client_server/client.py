import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port to connect to
server_address = ('192.168.100.28', 12345)

# Connect to the server
client_socket.connect(server_address)

# Send data to the server
message = "Halo Server Moonton, Saya mau minta id mobile legend 12345567"
client_socket.send(message.encode())

# Receive and print the server's response
data = client_socket.recv(1024)
print("Received from server: {}".format(data.decode()))

# Close the client socket
client_socket.close()

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.10"
port = 444

clientSocket.connect((host, port))

message = clientSocket.recv(1024)
clientSocket.close()

print(message.decode('ascii'))

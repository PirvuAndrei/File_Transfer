import socket

host = 'localhost'
port = 8081

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))

fileName = 'abc.txt'
sock.send(fileName.encode())

readFile = sock.recv(1024)

print(readFile.decode())

sock.close()
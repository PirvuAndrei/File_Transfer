import socket

host = 'localhost'
port = 8081


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((host,port))

sock.listen(1)

print("The Server is running and is listening to clients requests")

conn, adress = sock.accept()

message = "Hey there is something import for you"

conn.send(message.encode())

conn.close()
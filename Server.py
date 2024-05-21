import socket

host = 'localhost'
port = 8081


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((host,port))

sock.listen(1)

print("The Server is running and is listening to clients requests")

conn, adress = sock.accept()

try:
    fileName = conn.recv(1024)
    file = open(fileName, 'rb')
    readFile = file.read()
    conn.send(readFile)

    file.close()

except:

    conn.send("File Not Found on the Server".encode())

conn.close()
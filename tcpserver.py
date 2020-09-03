# tcpserver.py
import socket
welcomeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
welcomeSocket.bind(("localhost", 6789))
welcomeSocket.listen(5)
while True:
    print("The server is waiting")
    connectionSocket, address = welcomeSocket.accept()
    clientSentenceBytes = connectionSocket.recv(4096)
    clientSentence = clientSentenceBytes.decode("utf-8")
    connectionSocket.send(str.encode(clientSentence.upper()))
    connectionSocket.close()

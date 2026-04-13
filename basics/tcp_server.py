import socket
import threading

bind_ip = input("give ip:")
bind_port = int(input("port: "))

#Creating a listening socket -----> Receptionist alloting her a desk she can sit at only one desk
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding the server to listent
server.bind((bind_ip,bind_port))

server.listen(5)
print( "[*] Listening on %s:%d" % (bind_ip,bind_port))

def handle_client(client_socket):

	request = client_socket.recv(1024)

	print( "[*] Received: %s" % request)
	client_socket.send("ACK!")

	client_socket.close()

while True:

#this is receptionist after hearing a voice or attending a customer sends the customeer to another assistant or which is thread
	client,addr = server.accept()
	print( "[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))


	client_handler = threading.Thread(target=handle_client,args=(client,)) 
	client_handler.start() 

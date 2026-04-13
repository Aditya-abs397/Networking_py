import socket

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# sending data b is to tell python that its a byte not a string
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receiving data
response = client.recv(4096)

print(response.decode())


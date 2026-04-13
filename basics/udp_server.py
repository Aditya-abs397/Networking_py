import socket

bind_ip = input("Give IP: ")
bind_port = int(input("Port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((bind_ip, bind_port))

print(f"[*] Listening on {bind_ip}:{bind_port}")

while True:
    data, addr = server.recvfrom(4096)
    print(f"[*] Received from {addr[0]}:{addr[1]} -> {data.decode()}")
    msg = input("message :")
    server.sendto(msg.encode(), addr)

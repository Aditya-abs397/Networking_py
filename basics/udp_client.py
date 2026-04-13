import socket

target_address = input("Enter target's address: ")
target_port = int(input("Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(5.0)

try:
    msg = input("Enter message: ")
    client.sendto(msg.encode(), (target_address, target_port))

    data, addr = client.recvfrom(4096)
    print(f"Response from {addr}: {data.decode()}")

except socket.timeout:
    print("\n[!] Error: Timed out after 5 seconds.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()

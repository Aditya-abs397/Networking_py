import socket

target_host = input("Give IP address or website (e.g., www.google.com): ")
target_port = int(input("Enter Port (Use 80 for standard HTTP): "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(10)

try:
    client.connect((target_host, target_port))

    protocol = input("Send HTTP GET request? (y/n): ").strip().lower()
    
    if protocol == 'y':
        request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\nConnection: close\r\n\r\n"
        client.sendall(request.encode())

    response = b""
    while True:
        chunk = client.recv(4096)
        if not chunk:
            break
        response += chunk

    print("\n--- Response ---")
    print(response.decode(errors='ignore'))

except socket.timeout:
    print("Connection timed out.")
except socket.gaierror:
    print(f"Could not resolve host: {target_host}")
except ConnectionRefusedError:
    print(f"Connection refused on port {target_port}.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()
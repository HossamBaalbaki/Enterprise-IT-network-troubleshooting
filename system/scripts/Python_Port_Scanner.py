import socket

host = "192.168.10.1"
ports = [22, 80, 443, 3389]

print(f"Scanning {host}...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    sock.close()

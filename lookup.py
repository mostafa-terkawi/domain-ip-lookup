import socket

domain = input("Enter domain name (e.g. google.com): ")
ip = socket.gethostbyname(domain)

print(f"The IP address of {domain} is: {ip}")

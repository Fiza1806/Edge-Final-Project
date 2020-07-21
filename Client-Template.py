import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('unix-03.qatar.cmu.edu', 9030))
s.sendall ('Fiza Faris'.encode())
data = s.recv(1024)
data = data.decode()
print(repr(data))



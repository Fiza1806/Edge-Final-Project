import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9043))
s.listen()

s1, addr1 = s.accept()

s.sendall("Hello! Welcome to our game! Waiting for a partner to connect. Please, wait)".encode())

s1.sendall("What is your username?".encode())

data = s1.recv(1024)

data = data.decode()

name1=data

s2, addr2 = s.accept()

s2.sendall("Hello! Welcome to our game! You are going to play with "+ name1.encode())

s2.sendall("What is your username?".encode())

data1 = s2.recv(1024)


data2 = data1.decode()

name2=data2

s1.sendall("You are going to play with "+name2.encode())


print("Players:"+str(addr1)+" / "+name1+" and "+str(add2)+" / " + name2)

s1.close()
s2.close()


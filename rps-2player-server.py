import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9030))
s.listen()

s1, addr1 = s.accept()

s1.sendall("Hello! Welcome to our game!\n".encode())

s1.sendall("What is your username? Please enter:  ".encode())

data = s1.recv(1024)

data = data.decode()

name1=data

s2, addr2 = s.accept()

s2.sendall("Hello! Welcome to our game! You are going to play with ".encode()+ name1.encode())

s2.sendall("What is your username? Please enter:  ".encode())

data = s2.recv(1024)


data2 = data.decode()

name2=data2

s1.sendall("You are going to play with ".encode()+name2.encode())


print("Players:"+name1+" and "+name2)



#### then you start a game

s1.sendall("Rock/Paper/Scissors? Make sure you type it correctly".encode())

p1=s1.recv(1024)

p1=p1.decode()

s2.send("Rock/Paper/Scissors? Make sure you type it correctly".encode())

p2=s2.recv(1024)

p2=p2.decode()

if p1 == "Rock":
    p1 = 1
elif p1== "Paper":
    p1 = 2
elif p1 == "Scissors":
    p1 = 3



if p2 == "Rock":
    p2 = 1
elif p2 == "Paper":
    p2 = 2
elif p2 == "Scissors":
    p2 = 3

if p1 > p2:
    s1.send("You won!!".encode())
    s2.send("You lose!".encode())
elif p1 < p2:
    s2.send("You won!!".encode())
    s1.send("You lose!!".encode())
elif p1 == p2:
    s1.send("You draw!!".encode())
    s2.send("You draw!!".encode())

s1.close()
s2.close()
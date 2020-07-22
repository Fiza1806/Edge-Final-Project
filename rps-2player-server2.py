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



#### Let the game start!!!

s1.sendall("Rock/Paper/Scissors? Make sure you type it correctly! Your choice:   ".encode())

p1=s1.recv(1024)

p1=p1.decode()

list=["Rock","Scissors","Paper"]
if p1 in list:
    s1.sendall("Waiting for your opponent's choice \n".encode())
else:
    s1.sendall("Put valid input. Check your spelling, please!".encode())
    choice = s1.recv(1024)

    p1 = choice.decode()


s2.send("Rock/Paper/Scissors? Make sure you type it correctly! Your choice:   ".encode())

p2=s2.recv(1024)

p2=p2.decode()



if p2 in list:
    s2.sendall("Let's find the winner!\n")

else:
    s2.sendall("Put valid input. Check your spelling, please!".encode())
    choice1 = s2.recv(1024)

    p2 = choice1.decode()



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
    s1.send("You won!".encode()+p1.encode()+" will ALWAYS conquer ".encode()+p2.encode())
    s2.send("You lose!".encode()+p1.encode()+" will ALWAYS conquer ".encode()+p2.encode())
elif p1 < p2:
    s2.send("You won!!".encode()+p2.encode()+" will ALWAYS conquer ".encode()+p1.encode())
    s1.send("You lose!!".encode()+p2.encode()+" will ALWAYS conquer ".encode()+p1.encode())
elif p1 == p2:
    s1.send("You draw!!".encode())
    s2.send("You draw!!".encode())

s1.close()
s2.close()
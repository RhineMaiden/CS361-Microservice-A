import zmq #for ZeroMQ
import random #for random.choice
import time #for sleep

context = zmq.Context() #set up enviroment to be able to create sockets
socket = context.socket(zmq.REP) #specify type as reply socket
socket.bind("tcp://*:4666") #where the socket will listen

examplesList = [
    [b"Assembly", b"byte", b"8 bits"],
    [b"Intro to Security", b"Malware", b"Malicious software"],
    [b"Intro to Security", b"Nonce", b"Seed or randomization value"],
    [b"Theory of Computation", b"Bitstring", b"Binary string, string that consists of 0s and 1s"],
    [b"Theory of Computation", b"Alphabet", b"Finite set of characters"],
    [b"Theory of Computation", b"String", b"Ordered sequence of characters"],
    [b"Peoples of the World Pacific", b"The Three Regions of Oceania", b"Micronesia, Polynesia, Melanesia"],
    [b"Psychology", b"Delerium", b"A mental state characterized by confusion and disorganized thinking"],
    [b"Statistics", b"Hypothesis", b"A Testable, educated guess"],
    [b"Psychology", b"Discrimintation", b"Actions based off of steriotypes that negatively affect an out group"],
    [b"Psychology", b"Most common mental disorder in the US", b"Major Depressive Disorder"]
]

#create loop to wait for message from client
while True:
    #message from client
    message = socket.recv()        

    if len(message) > 0:
        #decode message
        print(f"\nMessage received: {message.decode()}\n")

        #client asked server to quit
        if message.decode() == "quit":
            break

        randomFact = random.choice(examplesList)

        #send reply to client
        socket.send_multipart(randomFact)
        print(f"Message sent: {randomFact}\n")

print(f"Goodbye!\n")
#clean exit
context.destroy()

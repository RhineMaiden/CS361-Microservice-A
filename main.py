import zmq #for ZeroMQ
import time #for sleep

context = zmq.Context() #set up environment to be able to create sockets
socket = context.socket(zmq.REQ) #specify type as request socket
socket.connect("tcp://localhost:4666") #connect to remote socket

#message to send
message = "example"

socket.send_string(message) #sendin the specified string
print(f"\n\nMessage sent: {message}\n") #print the sent message

message = socket.recv_multipart() #get the reply
print(f"Message received: {message}\n") #print the reply message

message = [msg.decode('utf-8') for msg in message]
print(f"Message decoded: {message}\n")

print(f"Course (message[0]): {message[0]}")
print(f"Term (message[1]): {message[1]}")
print(f"Definition (message[2]): {message[2]}\n")

#End server
message = "quit"
socket.send_string(message)
print(f"\nMessage sent: {message}\n")

How to REQUEST data

    Once your socket is created and connected to the correct port, send the sting "example" using the method send_string()
    
        socket.send_string("example") 

How to RECEIVE data

    The response will come back as an array of three byte strings. Use recv_multipart() to receive the array

        message = socket.recv_multipart()

    The array will contain byte strings. You can convert each index of the array into character strings with:

        message = [msg.decode('utf-8') for msg in message]

    After this, you access each string via the array index. There are three strings total. The first string is the course name, the second string is the term name, and the third string is the term definition. You can access each string respectively with:

        message[0] #course title
        message[1] #term name
        message[2] #term definition

End the Process

    You can also tell the microservice program to end by sending the string "quit". This does not generate any response. You can do this just before ending your main program to avoid having to manually end the process.

        socket.send_string("quit") 


UML sequence diagram


UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.
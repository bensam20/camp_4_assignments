import json
import socket

#Initializng the phon book dicrtionary
phoneBook = {"Abhi":"9757455821", "Sibi":"9758421652", "Subi":"8574692514", "Ben": "7025217574"}


def server_program():
    host = socket.gethostname() #getting the ip of host
    port = 5000
    #"127.0.01" or "localhost"
    #port can range from 1024 till 65535

    #create socket instance
    server_socket = socket.socket()

    #binding the host ip and port to our socket instance
    #pass the host and port as a tuple into bind method
    server_socket.bind((host,port))

    #start listening to the socket
    server_socket.listen(2)  #2 inside listen represents number of clients

    #accept an incoming connection
    #the accept() method will give back the conn obj and ip address of the incoming connection request
    conn, address = server_socket.accept()

    choice = '1'

    while(True):
        #infinite while loop to receive the data stream
        #receive the packets (with max size og 1024 bytes)
        #decode the received data
        data = conn.recv(1024).decode()

        choice = data

        
        if choice=='1':
            # for i in sorted(phoneBook.keys()):
            #     data = f"{i} : {phoneBook[i]}"
            #     conn.send(data.encode())
            phoneBookJson = json.dumps(phoneBook)
            conn.send(phoneBookJson.encode())
        elif choice=='2':
            keyreq = "Please enter name: "
            conn.send(keyreq.encode())
            key = conn.recv(1024).decode()
            valreq = "Please enter phone number: "
            conn.send(valreq.encode())
            val = conn.recv(1024).decode()
            phoneBook[key] = val
        elif choice=='3':
            keyreq = "Please enter name: "
            conn.send(keyreq.encode())
            key = conn.recv(1024).decode()
            del phoneBook[key]
        elif choice=='4':
            keyreq = "Please enter name: "
            conn.send(keyreq.encode())
            key = conn.recv(1024).decode()
            res = f"{key} : {phoneBook[key]}"
            conn.send(res.encode())
        elif choice=='5':
            numreq = "Please enter number: "
            conn.send(numreq.encode())
            num = conn.recv(1024).decode()
            for i in phoneBook:
                if phoneBook[i] == num:
                    res = f"{i} : {phoneBook[i]}"
                    conn.send(res.encode())
        else:
            res = "Wrong choice"
            conn.send(res.encode())

        # if no data recieved then terminate the while loop
        if not data:
            break
    
    conn.close() #close the connection once the while loop breaks

if __name__ == '__main__':
    server_program()


import sys
import socket


def clientInput(staples_string):
    """takes port number to connect to server"""
    return clientFunction(staples_string)


def clientFunction(staples_string) -> [bool, str]:
    """runs client function """

    write_variable = False 

    while write_variable is False:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        address = "127.0.0.1"

        client_socket.connect((address, 54345))

        print("Connected to the microservice via port 54345")
    
        if staples_string is None:
            staples_string = "None"

        print("Sending " + staples_string + " to microservice")

        client_socket.sendall(staples_string.encode())

        response = client_socket.recv(4096)

        print("Received message from Microservice.")

        if response.decode() == "ending":
            print("Server shutting down, closing client.")
            client_socket.close()
            sys.exit()
        
        client_socket.close()    

        print("Closing Connection Now")

        staples_string = response.decode()
        print(staples_string)

        with open("staples_file.txt", "w") as f:
            f.write(staples_string)
            write_variable = True

        
import socket

def scrub_server():
    """Microservice that connects to a scrubber.
    Uses Sockets to receive a time stamp and respond.
    Receives data and calls a helper function to create or
    append that data to an existing file, with the time stamp as file name
    Returns: None"""

    socket_obj = socket.socket()
    print("Successfully Created A Socket")

    port = 12345

    socket_obj.bind(("127.0.0.1", port))
    print(f"Binded Socket Successfully to: {port}")

    socket_obj.listen(5)
    print("Socket is Listening")

    # run infinitely
    while True:
        # Create + connect to client socket
        client_socket, address = socket_obj.accept()
        print(f"Now Connected to: {address}")

        try:
            # receive time stamp + decode
            time_stamp_data = client_socket.recv(1024)
            time_stamp_data = time_stamp_data.decode("utf-8")

            # respond with received msg
            print(f"Received: {time_stamp_data}")

            response = "A Time Stamp has been Received"
            client_socket.sendall(response.encode())

            # receive data to save to file + decode
            string_data = client_socket.recv(1024)
            string_data = string_data.decode("utf-8")

            # respond with received msg
            print(f"Received Data for: {time_stamp_data}")

            # save information to file or append to existing file
            save_file(time_stamp_data, string_data)

            # respond with file name
            response = time_stamp_data + ".txt"
            client_socket.sendall(response.encode())

        finally:
            client_socket.close()


def save_file(data_string, time_stamp):
    """Takes data in as a string and checks if a file with name "time_stamp" exists.
    If so, it appends the data_string to the bottom of the file. If not, then it
    creates that file and appends to that list.
    data_string: str
    time_stamp: str
    Returns: Str: file path"""

    # file path to check for
    file_path = "./data/time_stamp.txt"

    # open the txt file; if it doesn't exist create it
    txt_file = open(file_path, "a")

    # check if the string is over 72 characters.
    # if it is, split it at a space for readability 
    # then write it to the file
    if len(data_string) > 72:
        count = 0
        for char in data_string:
            count += 1
            if count < 50:
                txt_file.write(char)
            
            else:
                if char == " ":
                    txt_file.write("\n")
                    count = 0
                
                else:
                    txt_file.write(char)
                
    # if less than 72 characters, just write it directly
    else:
        txt_file.write(data_string)
    
    # write blank lines for the end of the file to set up the next set of data
    txt_file.write("\n")
    txt_file.write("\n")

    # close file
    txt_file.close()

    # Return the file path so we know it was successful
    return file_path
    

scrub_server()
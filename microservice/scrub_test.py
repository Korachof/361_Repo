import socket

def client_side():
    

    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_ip = "127.0.0.1"
        port = 54321

        client.connect((server_ip, port))

        print(f"Now connected to server under port: {port}")

        time_stamp_message_test = input("Type a 5 digit number: ")

        client.sendall(time_stamp_message_test.encode("utf-8")[:1024])
        
        response = client.recv(1024)

        response = response.decode("utf-8")

        print(f"Received: {response}")

        string_data_test = "this is a test to see if the data will be saved to a text file as intended. This is long to make sure it is saved in an easy to read format, feel me?"

        client.sendall(string_data_test.encode("utf-8")[:1024])

        confirmation = client.recv(1024)
        confirmation = confirmation.decode("utf-8")

client_side()
Welcome to the Readme for the CS 361 Scrubber Microservice!

This server creates a continuous connection via TCP listening clients, using a server and client side. 

It uses the localhose IP address and port 12345. This port can be easily changed if conflict with 
another program arises. 

This microservice receives a time stamp via a client-side program. Once it receives this time stamp, it will
send back an okay to the client to let the client side know a connection has been established. Once that has 
been established, the client side will send a long string of data to the microservice. The microservice will 
decode and read this data.

Once this has occurred, it will then check if a txt file exists within root/data with the title containing the
time stamp sent (example, if the time stamp is 010924 1627, it will name the file 010924 1627.txt). If the file
exists, it will append the new string content at the bottom, in an easily readable format. If the file does not
exist, it will create that file and write the contents of the string to it in an easily readable format. 

Server:

![image](https://github.com/Korachof/361_Repo/assets/114110894/90c4d313-6e2a-4bb8-be00-a42560411d77)

Client: 

![image](https://github.com/Korachof/361_Repo/assets/114110894/11f88430-46c2-4f4a-b6a4-16ba584066c1)

Server:

![image](https://github.com/Korachof/361_Repo/assets/114110894/6e316268-3848-4076-b05c-e2c7102e6a3c)

Output:

![image](https://github.com/Korachof/361_Repo/assets/114110894/f51428b6-ea0b-451a-809a-ec78e6c720fc)

![image](https://github.com/Korachof/361_Repo/assets/114110894/4283966c-67c6-4a31-bb0c-cf2c136f2f43)

Basic UML Sequence:

![Untitled](https://github.com/Korachof/361_Repo/assets/114110894/5ad7da11-1034-4cc7-93ad-414f59f7a2f0)

Included is a simple test client that allows the user to input a 5-digit number to similate the output 
for creating a text file and data. The data that is saved can be easily changed. 







""""
testing sending and receiving data
"""


import socket

my_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET corresponds to Ipv4 and SOCK_STREAM corresponds to TCP connection

#now bind that socket to a tuple (IP,Port), since this is the server go with local host for IP and any port
my_socket.bind((socket.gethostname(),1234))

"""socket= end point that receieves data"""

#This socket will wait for requests and have a queue of 5
my_socket.listen(5)
while True:
    #Accept any socket - client_socket is a socket object
    client_socket, address = my_socket.accept()
    print(f" Connection from {address} has been established")
    #send info back to client socket

    client_socket.send(bytes("Welcome to the server","utf-8"))
    ###WHAT IS BYTES AND WHAT IS A UTF-8 BYTE?????

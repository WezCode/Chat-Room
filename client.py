import socket

import socket

my_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET corresponds to Ipv4 and SOCK_STREAM corresponds to TCP connection

#Now connect to an IP of our choosing
my_socket.connect()
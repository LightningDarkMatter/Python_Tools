#!/bin/python3

#SOCKETS

import socket

# Create a socket object
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 7777        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is the address family ipv4, SOCK_STREAM is a port.
s.connect((HOST, PORT)) #connect to the server

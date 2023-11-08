import random
import socket
import threading
import time

from googletrans import Translator

HOST = "127.0.0.1"
PORT = 50123

langs = ['ar','hi','kn','ja','ru','gd']

# Create a socket
sock = socket.socket()

tran = Translator()

# Connect to the server
sock.connect((HOST, PORT))


def handle_connection(sock: socket):
    # Continuously read data from the client and print it out
    while True:
        data = sock.recv(4096)
        if not data:
            break
        print(data.decode())


bo = threading.Thread(target=handle_connection)
bo.start()



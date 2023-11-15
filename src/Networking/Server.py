import socket
import threading


class Client:
    socket: socket
    addr: str
    name: str
    stup: (str, int)

    def __init__(self, socket_tup):
        self.stup = socket_tup
        self.socket = socket_tup[0]
        self.addr = socket_tup[1]
        self.name = self.accept_message()
        print(f"{self.name}   {self.addr}")

    def accept_message(self):
        data = self.socket.recv(1024)
        if not data:
            return None
        return data.decode()

    def send_msg(self, inp: str):
        self.socket.sendall(inp.encode())

    def get_addr_tup(self):
        return self.stup

    def get_addr(self):
        return self.addr

    def get_name(self):
        return self.name


def send_all(clients: [Client], sender: Client, msg: str):
    if len(clients) == 0:
        return
    for c in clients:
        try:
            c.send_msg(f"$$MSG$$ |{sender.get_name()}: {msg}")
        except:
            return


def send_all_misc(clients: [Client]):
    if len(clients) == 0:
        return
    for c in clients:
        try:
            print(f'sent msg to {c.get_name()} : {c.get_addr()}')
            c.send_msg(f"$$UPDATE$$ |{';'.join([i.get_name() for i in clients])}")
        except:
            return


def is_connected(client: Client):
    try:
        client.send_msg("");
        return True
    except:
        return False


HOST = "127.0.0.1"
PORT = 50123

# Create a socket
sock = socket.socket()

# Bind the socket to the port
sock.bind((HOST, PORT))

# Listen for incoming connections
sock.listen()

clients: [Client] = []


def read_thrd(client: Client):
    # Continuously read data from the client and print it out
    while is_connected(client):
        try:
            data = client.accept_message()
        except:
            print(f"{client.get_name()} disc")
            send_all_misc(clients)
            continue
        if data is not None:
            print(f"{client.get_name()}: {data}")
            send_all(clients, client, data)
    print(f"{client.get_name()} disc : {[i.get_name() for i in clients]}")
    clients.remove(client)
    send_all_misc(clients)


while True:
    s, addr = sock.accept()
    print((s, addr))
    t_client = Client((s, addr))
    clients.append(t_client)
    send_all_misc(clients)
    threading.Thread(target=read_thrd, args=(t_client,)).start()

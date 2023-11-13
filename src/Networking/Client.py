import socket
import threading

from googletrans import Translator

from src.GUI.MemberList.MemberListFrame import MemberListFrame
from src.GUI.TextFrame.TextFrame import TextFrame


class NetworkingClient:
    def __init__(self, port: int, ip: int, name: str, member_list_frame: MemberListFrame, text_frame: TextFrame):
        self.IP = ip
        self.PORT = port
        self.NAME = name
        self.mlf = member_list_frame
        self.txtfrm = text_frame

        self.c_socket = socket.socket()
        self.c_socket.connect((self.IP, self.PORT))

        self.recvthrd = threading.Thread(target=self.receive_dat)
        self.recvthrd.start()

        self.send_dat(self.NAME)

    def receive_dat(self):
        while True:
            print("recvthrd")
            data = self.c_socket.recv(4096)
            if not data:
                break
            self.handle_dat(data.decode())
            print("Received message")
            print(data)

    def handle_dat(self, data):
        if "$$UPDATE$$" in data:
            members = data.split("|")[1].split(";")
            self.mlf.update_memlist(members)
            return

        if "$$MSG$$" in data:
            msg = data.split("|")[1]
            self.txtfrm.append_txt(msg)
            return

    def send_dat(self, msg: str):
        self.c_socket.sendall(msg.encode())

import socket
import threading

from googletrans import Translator

from src.GUI.MemberList.MemberListFrame import MemberListFrame
from src.GUI.TextFrame.TextFrame import TextFrame


class NetworkingClient:
    def __init__(self, port: str, ip: int, name: str, member_list_frame: MemberListFrame, text_frame: TextFrame):
        self.IP = ip
        self.PORT = port
        self.mlf = member_list_frame
        self.txtfrm = text_frame

        self.c_socket = socket.socket()
        self.c_socket.bind((self.IP, self.PORT))

        self.send_dat(name)

        self.recvthrd = threading.Thread(target=self.receive_dat)
        self.recvthrd.start()

    def receive_dat(self):
        while True:
            data = self.c_socket.recv(4096)
            if not data:
                break
            self.handle_dat(data)

    def handle_dat(self, data):
        if "$$UPDATE$$" in data:
            members = data.split("|")[1].split(";")
            self.mlf.update_memlist(members)
            return

        self.txtfrm.append_txt(data)

    def send_dat(self, msg: str):
        self.c_socket.sendall(msg)




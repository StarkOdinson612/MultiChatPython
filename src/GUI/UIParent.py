import customtkinter

from src.GUI.MemberList.MemberListFrame import MemberListFrame
from src.GUI.TextEntry.TextEntry import TextEntry
from src.GUI.TextFrame.TextFrame import TextFrame
from src.Networking.Client import NetworkingClient


class UIParent(customtkinter.CTkFrame):
    def __init__(self, master: any, port: int, ip: str, name: str, **kwargs):
        super().__init__(master, **kwargs)
        self.PORT = port
        self.IP = ip
        self.NAME = name

        self.grid_columnconfigure(index=(0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure(index=(0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.mlf = MemberListFrame(self)
        self.mlf.grid(row=0, rowspan=8, column=0, padx=5, pady=5, sticky="nsew")

        self.txtfrm = TextFrame(self)
        self.txtfrm.grid(row=0, column=1, padx=5, pady=5, columnspan=4, rowspan=7, sticky="nsew")

        self.network_cl = NetworkingClient(port=self.PORT,
                                           ip=self.IP,
                                           name=self.NAME,
                                           member_list_frame=self.mlf,
                                           text_frame=self.txtfrm)

        self.t_entry = TextEntry(master=self, n_client=self.network_cl)
        self.t_entry.grid(row=7,column=1, columnspan=4, stick="nsew", padx=5, pady=5)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Not Discord")
        self.geometry("900x450")
        self.minsize(200, 400)
        ip_dialog = customtkinter.CTkInputDialog(text="Enter the IP to connect to: ",
                                                 title="IP Address")
        self.IP = ip_dialog.get_input()

        port_dialog = customtkinter.CTkInputDialog(text="Enter the port: ",
                                                   title="Port")
        self.PORT = int(port_dialog.get_input())
        name_dialog = customtkinter.CTkInputDialog(text="Enter username: ",
                                                   title="Client Username")
        self.NAME = name_dialog.get_input()
        # self.IP = "localhost"
        # self.PORT = 50123
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.ui_parent = UIParent(master=self, port=self.PORT, ip=self.IP, name=self.NAME)
        self.ui_parent.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

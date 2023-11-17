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

        self.grid_columnconfigure(index=1, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        self.mlf = MemberListFrame(self)
        self.mlf.grid(row=0, column=0, rowspan=2, padx=5, pady=5, sticky="nsew")

        self.txtfrm = TextFrame(self)
        self.txtfrm.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.network_cl = NetworkingClient(port=self.PORT,
                                           ip=self.IP,
                                           name=self.NAME,
                                           member_list_frame=self.mlf,
                                           text_frame=self.txtfrm)

        self.t_entry = TextEntry(master=self, n_client=self.network_cl)
        self.t_entry.grid(row=1, column=1, stick="nsew", padx=5, pady=5)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Not Discord")
        self.geometry("1600x900")
        self.minsize(750, 400)
        # ip_dialog = customtkinter.CTkInputDialog(text="Enter the IP to connect to: ",
        #                                          title="IP Address")
        # self.IP = ip_dialog.get_input()
        #
        # port_dialog = customtkinter.CTkInputDialog(text="Enter the port: ",
        #                                            title="Port")
        # self.PORT = int(port_dialog.get_input())
        # name_dialog = customtkinter.CTkInputDialog(text="Enter username: ",
        #                                            title="Client Username")
        # self.NAME = name_dialog.get_input()

        user_inp = InputsApp(self)
        self.INP_U = user_inp.get_data()
        self.IP = self.INP_U[0]
        self.PORT = self.INP_U[1]
        self.NAME = self.INP_U[2]
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.ui_parent = UIParent(master=self, port=self.PORT, ip=self.IP, name=self.NAME)
        self.ui_parent.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def setInp(self, inp: (str, int, str)):
        self.INP_U = inp


class InputsApp(customtkinter.CTkToplevel):
    def __init__(self, master_a: App):
        super().__init__()

        self.title("Connection Window")
        self.geometry("450x300")
        self.minsize(200, 100)
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.master_a = master_a

        self.user_inp: (str, int, str) = None

        self.grid_rowconfigure(index=(0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        self.tframe = customtkinter.CTkFrame(master=self)
        self.tframe.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.tframe.grid_columnconfigure(index=0, weight=1)
        self.tframe.grid_rowconfigure(index=(0, 1, 2), weight=1)

        self.ip = customtkinter.CTkEntry(master=self.tframe,
                                         placeholder_text="Enter IP")
        self.ip.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.port = customtkinter.CTkEntry(master=self.tframe,
                                           placeholder_text="Enter Port")
        self.port.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.name = customtkinter.CTkEntry(master=self.tframe,
                                           placeholder_text="Enter Username")
        self.name.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.name.bind(sequence="<Return>", command=lambda _: self._button_submit())

        self.sub_but = customtkinter.CTkButton(self, text="Connect", command=self._button_submit)
        self.sub_but.grid(row=1, column=0)

        self.lift()
        self.attributes("-topmost", True)

    def _button_submit(self):
        print("sub")
        self.master_a.setInp((self.ip.get(), int(self.port.get()), self.name.get()))
        self.user_inp = (self.ip.get(), int(self.port.get()), self.name.get())
        print("bob")
        self.grab_release()
        self.destroy()

    def get_data(self) -> (str, int, str):
        self.master.wait_window(self)
        return self.user_inp

    def _on_closing(self):
        self.grab_release()
        self.destroy()

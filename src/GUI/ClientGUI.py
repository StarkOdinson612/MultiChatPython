import customtkinter


class MemberListFrame(customtkinter.CTkScrollableFrame):


class UIParent(customtkinter.CTkFrame):
    def __init__(self, master: any, port: str, ip: str, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(index=(0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(index=(0, 1), weight=1)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Not Discord")
        self.geometry("1600x900")
        self.minsize(800, 450)
        ip_dialog = customtkinter.CTkInputDialog(text="Enter the IP to connect to: ",
                                                 title="IP Address")
        self.IP = ip_dialog.get_input()

        port_dialog = customtkinter.CTkInputDialog(text="Enter the port: ",
                                                   title="Port")
        self.PORT = port_dialog.get_input()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.ui_parent = UIParent(master=self, port=self.PORT, ip=self.IP)
        self.ui_parent.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

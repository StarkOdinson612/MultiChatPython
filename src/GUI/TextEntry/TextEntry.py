import customtkinter

from src.Networking.Client import NetworkingClient


class TextEntry(customtkinter.CTkFrame):
    def __init__(self, master: any, n_client: NetworkingClient, **kwargs):
        super().__init__(master, **kwargs)
        self.n_client = n_client

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.entry_b = customtkinter.CTkEntry(master=self)
        self.entry_b.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.entry_b.bind(sequence="<Return>", command=lambda _: self.send_msg())

    def send_msg(self):
        text = self.entry_b.get()
        self.entry_b.delete(0, "end")
        self.n_client.send_dat(text)

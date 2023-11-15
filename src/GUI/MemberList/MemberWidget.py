import customtkinter


class MemberWidget(customtkinter.CTkFrame):
    def __init__(self, master, name, **kwargs):
        super().__init__(master, **kwargs)
        self.name = name

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.textbox = customtkinter.CTkLabel(master=self,
                                              text=name,
                                              corner_radius=10)
        self.textbox.grid(row=0, column=0, sticky="nsew")

    def get_name(self):
        return self.name
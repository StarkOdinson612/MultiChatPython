import customtkinter


class TextFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.text_box = customtkinter.CTkTextbox(self, wrap="none",state="disabled")
        self.text_box.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")

    def append_txt(self, text: str):
        self.text_box.configure(state="normal")
        self.text_box.insert("end", text + "\n")
        self.text_box.configure(state="disabled")

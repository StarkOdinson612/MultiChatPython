import customtkinter

from src.GUI.MemberList.MemberWidget import MemberWidget


class MemberListFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.members: [MemberWidget] = []
        self.grid_columnconfigure(0, weight=1)

    def update_memlist(self, memberstr: [str]):
        for i in self.members:
            i.destroy()

        for i in memberstr:
            temp = MemberWidget(self, name=i)
            temp.grid(row=len(self.members), column=0, padx=5, pady=5, sticky="ew")
            self.members.append(temp)
        print(self.members)

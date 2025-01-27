
import tkinter as tk

class UI(tk.Frame):

    def __init__(self, parent=None, title="Rental System", bg_color="white", size="920x620"):
        super().__init__(parent)

        
        self.parent = parent
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        x = (screen_width // 2) - (920 // 2)
        y = (screen_height // 2) - (620 // 2)
        self.parent.resizable(False,False)
        self.parent.title(title)
        self.parent.geometry(f"{size}+{x}+{y}")
        self.parent.minsize(400,400)
        self.parent.configure(bg=bg_color)
        self.parent.iconbitmap("View/img/favicon.ico")  
        self.init_ui()

    def init_ui(self):
        pass
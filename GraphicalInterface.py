import tkinter as tk
import ImageEditor

class Menu:
    def __init__(self, master):
        self.master = master
        self.EditButton = tk.Button(self.master, text='Edit', width=25, command=self.OpenEditor)
        self.ExitButton = tk.Button(self.master, text='Exit', width=25, command=self.CloseWindow)
        self.EditButton.pack()
        self.ExitButton.pack()


    def OpenEditor(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ImageEditor.Editor(self.newWindow)

    def CloseWindow(self):
        self.master.destroy()

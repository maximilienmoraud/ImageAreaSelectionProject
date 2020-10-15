import tkinter as tk
import ImageEditor


class Menu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.EditButton = tk.Button(self.frame, text='Edit', width=25, command=self.OpenEditor)
        self.ExitButton = tk.Button(self.frame, text='Exit', width=25, command=self.CloseWindow)
        self.EditButton.pack()
        self.ExitButton.pack()
        self.frame.pack()

    def OpenEditor(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ImageEditor.Editor(self.newWindow)

    def CloseWindow(self):
        self.master.destroy()

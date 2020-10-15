import tkinter as tk


class Editor:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.ExitButton = tk.Button(self.frame, text='Quit', width=25, command=self.CloseWindow)
        self.ExitButton.pack()
        self.frame.pack()

    def CloseWindow(self):
        self.master.destroy()

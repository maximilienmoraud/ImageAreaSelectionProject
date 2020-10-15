import tkinter as tk
from tkinter import *
from tkinter import filedialog
import numpy as np
from tkinter.messagebox import *

from PIL import ImageTk, Image

x = 0
y = 0
list = []


class Editor:
    def __init__(self, master):
        self.master = master

        self.Image()

        self.SelectionType = Listbox(self.master, height=3, width=6)
        self.SelectionType.insert(1, " Square")
        self.SelectionType.insert(2, "  Circle")
        self.SelectionType.insert(3, "  Other")
        self.SelectionType.pack()

        self.EditButton = tk.Button(self.master, text='Edit', width=25, command=test)
        self.EditButton.pack(side=LEFT)

        self.ExitButton = tk.Button(self.master, text='Quit', width=25, command=self.CloseWindow)
        self.ExitButton.pack(side=RIGHT)

    def CloseWindow(self):
        # Fonction qui permet de fermer la fenettre
        self.master.destroy()

    def Image(self):
        # Fonction qui permet d'afficher l'image
        img = ImageTk.PhotoImage(ResizeImage(Image.open("Images/PhotoChat.jpg"), self.master.winfo_screenwidth()))
        self.canvas = tk.Canvas(self.master, width=img.width(), height=img.height(), borderwidth=0,
                                highlightthickness=0)
        self.canvas.pack(expand=True)
        self.canvas.img = img
        self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
        self.canvas.bind('<Button-1>', GetMousePos)
        self.canvas.bind('<Motion>', self.Mouvement)

    def Mouvement(self, zz):
        self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, width=2, outline="black")


def ResizeImage(img, ScreenWidth):
    originalWidth, originalHeight = img.size
    return img.resize((int(ScreenWidth / 2), int(((ScreenWidth / 2) / originalWidth) * originalHeight)))


def GetMousePos(event):
    global x
    global y
    global list
    x = event.x
    y = event.y
    pos = x, y
    list.append(pos)


def test():
    print(list)

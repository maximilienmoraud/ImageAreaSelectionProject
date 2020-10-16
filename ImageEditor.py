import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

x = -1
y = -1
list = []


class Editor:
    def __init__(self, master):
        self.draw = 0
        self.coords = []
        self.type = ""
        self.scale = 0

        self.master = master

        self.Image()

        self.SelectionType = Listbox(self.master, height=3, width=6)
        self.SelectionType.insert(1, " Square")
        self.SelectionType.insert(2, "  Circle")
        self.SelectionType.insert(3, "  Other")
        self.SelectionType.pack(side=LEFT, padx=10)

        self.NameSelection = Entry(self.master)
        self.NameSelection.pack(side=LEFT, padx=10)

        self.SaveButton = tk.Button(self.master, text='Save', width=25, command=self.Export)
        self.SaveButton.pack(side=BOTTOM)

        self.ResetButton = tk.Button(self.master, text='Reset', width=25, command=self.ResetImage)
        self.ResetButton.pack(side=BOTTOM)

        self.ExitButton = tk.Button(self.master, text='Quit', width=25, command=self.CloseWindow)
        self.ExitButton.pack(side=BOTTOM)

    def CloseWindow(self):
        # Fonction qui permet de fermer la fenettre
        self.master.destroy()

    def Image(self):
        # Fonction qui permet d'afficher l'image
        imgfullsize = Image.open("Images/PhotoChat.jpg")
        OriginalWidth, OriginalHeight = imgfullsize.size
        img = ResizeImage(imgfullsize, self.master.winfo_screenwidth())
        ResizedWidth, ResizedHeight = img.size
        self.scale = OriginalWidth/ResizedWidth
        img = ImageTk.PhotoImage(img)
        self.canvas = tk.Canvas(self.master, width=img.width(), height=img.height(), borderwidth=0,
                                highlightthickness=0)
        self.canvas.pack(expand=True, side=TOP)
        self.canvas.img = img
        self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
        self.canvas.bind('<Button-1>', GetMousePos)
        self.canvas.bind('<Motion>', self.Mouvement)

    def ResetImage(self):
        onscreen = self.canvas.find_all()
        for i in range(len(onscreen)):
            if i != 0:
                self.canvas.delete(onscreen[i])
        list.clear()
        global x
        global y
        x = -1
        y = -1
        self.draw = 0

    def Mouvement(self, zz):
        if self.SelectionType.get('active') == " Square" and x != -1 and y != -1 and self.draw == 0:
            self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, width=2, outline="black")
            if len(list) == 2:
                self.canvas.create_rectangle(list[0][0], list[0][1], list[1][0], list[1][1], width=2, outline="black")
                self.draw = 1
                self.coords = list
                self.type = "Square"

        if self.SelectionType.get('active') == "  Circle" and x != -1 and y != -1 and self.draw == 0:
            self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, width=2, outline="black")
            if len(list) == 2:
                self.canvas.create_oval(list[0][0], list[0][1], list[1][0], list[1][1], width=2, outline="black")
                self.draw = 1
                self.coords = list
                self.type = "Circle"

        if self.SelectionType.get('active') == "  Other" and x != -1 and y != -1 and self.draw == 0:
            self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, width=2, outline="black")
            self.canvas.bind('<Button-2>', self.Trace)

    def Trace(self, zz):
        for i in range(len(list)):
            if i < len(list) - 1:
                self.canvas.create_line(list[i][0], list[i][1], list[i + 1][0], list[i + 1][1], width=2)
            if i == len(list) - 1:
                self.canvas.create_line(list[0][0], list[0][1], list[i][0], list[i][1], width=2)
        self.draw = 1
        self.coords = list
        self.type = "Other"

    def Export(self):
        if self.draw == 1:
            print("infos : ", self.type, self.coords, self.NameSelection.get(), self.scale)


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

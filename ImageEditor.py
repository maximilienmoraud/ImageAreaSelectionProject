import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import CSVParser

x = -1
y = -1
list = []
categorie = CSVParser.ReadCategorie()
formtype = "Default"

class Editor:
    def __init__(self, master):
        self.draw = 0
        self.coords = []
        self.type = ""
        self.scale = 0

        self.master = master

        self.Image()

        self.BoutonsForme = tk.Frame(self.master)
        self.BoutonsForme.pack(side=TOP)
        self.SquareButton = tk.Button(self.BoutonsForme, text='Rectangle', width=25, command=self.Square)
        self.SquareButton.pack(side=LEFT)
        self.CircleButton = tk.Button(self.BoutonsForme, text='Cercle', width=25, command=self.Circle)
        self.CircleButton.pack(side=LEFT)
        self.FreeButton = tk.Button(self.BoutonsForme, text='Forme libre', width=25, command=self.Free)
        self.FreeButton.pack(side=LEFT)
        self.BoutonsSave = tk.Frame(self.master)
        self.BoutonsSave.pack(side=TOP)
        self.Categorie = ttk.Combobox(self.BoutonsSave, values=categorie)
        self.Categorie.pack(side=LEFT)
        self.Categorie.bind("<<ComboboxSelected>>", self.ActionCombobox)
        self.SaveButton = tk.Button(self.BoutonsSave, text='Enregistrer la forme', width=25, command=self.Export)
        self.SaveButton.pack(side=RIGHT)
        self.NameSelection = Entry(self.BoutonsSave)
        self.NameSelection.pack(side=RIGHT)

        self.ExitButton = tk.Button(self.master, text='Terminer les modifications', width=25, command=self.CloseWindow)
        self.ExitButton.pack(side=TOP)

    def ActionCombobox(self, event):
        select = self.Categorie.get()
        if select == "Nouveau":
            self.NameSelection.delete(0, END)
            self.AutreCategorie = Entry(self.BoutonsSave)
            self.AutreCategorie.pack(side=LEFT)
        else:
            self.AutreCategorie = Entry(self.BoutonsSave)
            self.AutreCategorie.insert(END, select)
            self.NameSelection.delete(0, END)
            self.NameSelection.insert(END, select + '1')

    def Square(self):
        print('def square')
        global formtype
        formtype = "Square"
        self.ResetImage()

    def Circle(self):
        print('def Circle')
        global formtype
        formtype = "Circle"
        self.ResetImage()

    def Free(self):
        print('def Free')
        global formtype
        formtype = "Free"
        self.ResetImage()

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
        self.canvas = tk.Canvas(self.master, width=img.width(), height=img.height(), borderwidth=0, highlightthickness=0)
        self.canvas.pack(expand=True, side=TOP)
        self.canvas.img = img
        self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
        self.canvas.bind('<Button-1>', GetMousePos)
        self.canvas.bind('<Motion>', self.Mouvement)

    def Mouvement(self, zz):
        if formtype == "Square" and x != -1 and y != -1 and self.draw == 0:
            self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, width=2, outline="black")
            if len(list) == 2:
                self.canvas.create_rectangle(list[0][0], list[0][1], list[1][0], list[1][1], width=2, outline="black")
                self.draw = 1
                self.coords = list
                self.type = "Square"

        if formtype == "Circle" and x != -1 and y != -1 and self.draw == 0:
            self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, width=2, outline="black")
            if len(list) == 2:
                self.canvas.create_oval(list[0][0], list[0][1], list[1][0], list[1][1], width=2, outline="black")
                self.draw = 1
                self.coords = list
                self.type = "Circle"

        if formtype == "Free" and x != -1 and y != -1 and self.draw == 0:
            self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, width=2, outline="black")
            self.canvas.bind('<Button-3>', self.Trace)

    def Trace(self, zz):
        for i in range(len(list)):
            if i < len(list) - 1:
                self.canvas.create_line(list[i][0], list[i][1], list[i + 1][0], list[i + 1][1], width=2)
            if i == len(list) - 1:
                self.canvas.create_line(list[0][0], list[0][1], list[i][0], list[i][1], width=2)
        self.draw = 1
        self.coords = list
        self.type = "Free"

    def Export(self):
        if self.draw == 1:
            if self.Categorie.get() == 'Nouveau':
                global categorie
                categorie.append(self.AutreCategorie.get())
                CSVParser.WriteCategorie(categorie)
            print("infos : ", self.AutreCategorie.get(), self.NameSelection.get(), formtype, self.coords,  self.scale)
            form = [self.AutreCategorie.get(), self.NameSelection.get(), formtype, self.coords,  self.scale]
            CSVParser.ExportForm(form)


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

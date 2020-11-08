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

        self.Titre1 = tk.Label(self.master, text='Choix du type de forme', pady=10)
        self.Titre1.pack(side=TOP)

        self.FormFrame = tk.Frame(self.master)
        self.FormFrame.pack(side=TOP)
        self.SquareButton = tk.Button(self.FormFrame, text='Rectangle', width=40, height=3, command=self.Square)
        self.SquareButton.pack(side=LEFT)
        self.CircleButton = tk.Button(self.FormFrame, text='Cercle', width=40, height=3, command=self.Circle)
        self.CircleButton.pack(side=LEFT)
        self.FreeButton = tk.Button(self.FormFrame, text='Forme libre', width=40, height=3, command=self.Free)
        self.FreeButton.pack(side=LEFT)

        self.Titre2 = tk.Label(self.master, text='Choix de la catégorie de la forme', pady=10)
        self.Titre2.pack(side=TOP)

        self.CategorieFrame = tk.Frame(self.master)
        self.CategorieFrame.pack(side=TOP)
        self.Categorie = ttk.Combobox(self.CategorieFrame, values=categorie, width=60)
        self.Categorie.pack(side=LEFT)
        self.Categorie.bind("<<ComboboxSelected>>", self.ActionCombobox)

        self.Titre3 = tk.Label(self.master, text='Choix du nom de la forme', pady=10)
        self.Titre3.pack(side=TOP)

        self.NameSaveFrame = tk.Frame(self.master)
        self.NameSaveFrame.pack(side=TOP)
        self.NameSelection = Entry(self.NameSaveFrame, width=60)
        self.NameSelection.pack(side=LEFT)
        self.SaveButton = tk.Button(self.NameSaveFrame, text='Enregistrer la forme', width=60, command=self.Export)
        self.SaveButton.pack(side=RIGHT)

        self.Titre4 = tk.Label(self.master, text=' ')
        self.Titre4.pack(side=TOP)

        self.ExitButton = tk.Button(self.master, text='Terminer les modifications', width=120, command=self.CloseWindow)
        self.ExitButton.pack(side=TOP)

    def ActionCombobox(self, event):
        select = self.Categorie.get()
        if select == "Nouveau":
            self.NameSelection.delete(0, END)
            self.AutreCategorie = Entry(self.CategorieFrame, width=60)
            self.AutreCategorie.pack(side=LEFT)
        else:
            self.AutreCategorie = Entry(self.NameSaveFrame)
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

        if formtype == "Circle" and x != -1 and y != -1 and self.draw == 0:
            self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, width=2, outline="black")
            if len(list) == 2:
                self.canvas.create_oval(list[0][0], list[0][1], list[1][0], list[1][1], width=2, outline="black")
                self.draw = 1
                self.coords = list

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

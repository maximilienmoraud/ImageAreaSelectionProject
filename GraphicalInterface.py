from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkfilebrowser import askopenfilename
from PIL import ImageTk, Image
import CSVParser
import ImageEditor

tempcategorie = 0
tempname = 0
iscreate = 0
canvas = 0
data = 'Accueil.jpg'

class Menu:
    def __init__(self, master):
        self.draw = 0
        self.coords = []
        self.type = ""
        self.scale = 0

        self.master = master
        self.master.configure(bg='#2B2B2B')

        self.fontStyle0 = tkFont.Font(size=16)
        self.fontStyle1 = tkFont.Font(size=15)
        self.fontStyle2 = tkFont.Font(size=11, weight='bold')

        self.Separation = tk.Label(self.master, background='#2B2B2B', foreground='white', text=' ', padx='5')
        self.Separation.pack(side=LEFT)

        self.ListFile = tk.Frame(self.master)
        self.ListFile.pack(side=LEFT)

        self.FileButton = tk.Button(self.ListFile, font=self.fontStyle2, background='#3B3F42', foreground='white', text='Ouvrir un fichier', width=25, command=self.OpenFile)
        self.FileButton.pack(side=TOP)

        self.EditButton = tk.Button(self.ListFile, font=self.fontStyle2, background='#3B3F42', foreground='white', text='Créer des formes', width=25, command=self.OpenEditor)
        self.EditButton.pack(side=BOTTOM)

        self.Separation = tk.Label(self.master, background='#2B2B2B', foreground='white', text=' ', padx='5')
        self.Separation.pack(side=LEFT)

        self.ImageZone = tk.Frame(self.master)
        self.ImageZone.pack(side=LEFT)

        self.Image()

        self.Separation = tk.Label(self.master, background='#2B2B2B', foreground='white', text=' ', padx='5')
        self.Separation.pack(side=LEFT)

        self.ListFrame = tk.Frame(self.master)
        self.ListFrame.pack(side=LEFT)

        self.ListeCategorie = tk.Listbox(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white', width='30')
        self.ListeName = tk.Listbox(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white', width='30')
        self.ActualiseCategorie()
        self.ActualiseName()
        self.ListeCategorie.pack(side=TOP)
        self.ListeName.pack(side=TOP)
        self.ListeCategorie.bind("<<ListboxSelect>>", self.SelectCategorie)
        self.ListeName.bind("<<ListboxSelect>>", self.SelectName)

        self.Separation = tk.Label(self.master, background='#2B2B2B', foreground='white', text=' ', padx='5')
        self.Separation.pack(side=LEFT)

    def SelectCategorie(self, event):
        global tempcategorie
        if len(self.ListeCategorie.curselection())>0:
            temp=self.ListeCategorie.curselection()
            tempcategorie=int(temp[0])
            self.ActualiseCategorie()
            self.ActualiseName()
        self.ActualiseCategorie()
        print(tempcategorie)

    def SelectName(self, event):
        global tempname
        global iscreate
        print('new selected name')
        if len(self.ListeName.curselection())>0:
            temp=self.ListeName.curselection()
            tempname=int(temp[0])
        print(tempname)

        onscreen = self.canvas.find_all()
        for i in range(len(onscreen)):
            if i != 0:
                self.canvas.delete(onscreen[i])
        self.TraceForme(data, self.ListeCategorie.get(tempcategorie), self.ListeName.get(tempname))

        if iscreate == 0:
            self.SupprButton = tk.Button(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white', text='Supprimer', width=26)
            self.SupprButton.pack(side=TOP)
            print(tempcategorie)
            print(tempname)
            self.SupprButton.bind('<Button-1>', lambda a='test', b=data, c=self.ListeCategorie.get(tempcategorie), d=self.ListeName.get(tempname): CSVParser.SupprimeForm(a, b, c, d))
            iscreate = 1
        if iscreate == 1:
            self.SupprButton.destroy()
            self.SupprButton = tk.Button(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white', text='Supprimer', width=26)
            self.SupprButton.pack(side=TOP)
            print(tempcategorie)
            print(tempname)
            self.SupprButton.bind('<Button-1>', lambda a='test', b=data, c=self.ListeCategorie.get(tempcategorie), d=self.ListeName.get(tempname): CSVParser.SupprimeForm(a, b, c, d))

    def ActualiseCategorie(self):
        categorie = CSVParser.FiltreCategorie(data)
        i = len(categorie)
        j = 0
        self.ListeCategorie.delete(0, END)
        while j < i:
            self.ListeCategorie.insert(END, categorie[j])
            j = j + 1
        self.ListeCategorie.selection_set(tempcategorie)
        print('Actualisation Categorie Ok')

    def ActualiseName(self):
        name = CSVParser.FiltreName(data, self.ListeCategorie.get(tempcategorie))
        k = len(name)
        l = 0
        self.ListeName.delete(0, END)
        while l < k:
            self.ListeName.insert(END, name[l])
            l = l + 1
        self.ListeCategorie.selection_set(0)
        print('Actualisation Name Ok')

    def Image(self):
        # Fonction qui permet d'afficher l'image
        global canvas
        imgfullsize = Image.open(data)
        self.imagename = data
        OriginalWidth, OriginalHeight = imgfullsize.size
        img = ResizeImage(imgfullsize, self.master.winfo_screenwidth(), self.master.winfo_screenheight())
        ResizedWidth, ResizedHeight = img.size
        self.scale = OriginalWidth/ResizedWidth
        img = ImageTk.PhotoImage(img)
        if canvas == 0:
            self.canvas = tk.Canvas(self.ImageZone, width=img.width(), height=img.height(), borderwidth=0, highlightthickness=0)
            self.canvas.pack(expand=True, side=TOP)
            self.canvas.img = img
            self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
            canvas = 1
        if canvas == 1:
            self.canvas.destroy()
            self.canvas = tk.Canvas(self.ImageZone, width=img.width(), height=img.height(), borderwidth=0, highlightthickness=0)
            self.canvas.pack(expand=True, side=TOP)
            self.canvas.img = img
            self.canvas.create_image(0, 0, image=img, anchor=tk.NW)

    def OpenEditor(self):
        if data != 'Images/Accueil.jpg':
            self.newWindow = tk.Toplevel(self.master)
            self.app = ImageEditor.Editor(self.newWindow)

    def OpenFile(self):
        global data
        temp = askopenfilename()
        if len(temp) != 0 :
            data = temp
        self.Image()
        print(data)

    def TraceForme(self, data, tempcategorie, tempname):
        donnee = CSVParser.RecupCoord(data, tempcategorie, tempname)
        typeform = donnee[0]
        coordonnee = donnee[1]
        echelle = donnee[2]

        if typeform == "Square":
            self.canvas.create_rectangle(coordonnee[0][0], coordonnee[0][1], coordonnee[1][0], coordonnee[1][1], width=2, outline="black")
            self.draw = echelle

        if typeform == "Circle":
            self.canvas.create_oval(coordonnee[0][0], coordonnee[0][1], coordonnee[1][0], coordonnee[1][1], width=2, outline="black")
            self.draw = echelle

        if typeform == "Free":
            for i in range(len(coordonnee)):
                if i < len(coordonnee) - 1:
                    self.canvas.create_line(coordonnee[i][0], coordonnee[i][1], coordonnee[i + 1][0], coordonnee[i + 1][1], width=2)
                if i == len(coordonnee) - 1:
                    self.canvas.create_line(coordonnee[0][0], coordonnee[0][1], coordonnee[i][0], coordonnee[i][1], width=2)


def ResizeImage(img, ScreenWidth, ScreenHeight):
    originalWidth, originalHeight = img.size
    if (originalWidth > originalHeight) & ((ScreenWidth * 0.5 / originalWidth * originalHeight) < (ScreenHeight * 0.6)):
        return img.resize((int(ScreenWidth * 0.5), int((ScreenWidth * 0.5) / originalWidth * originalHeight)))
    else:
        return img.resize((int((ScreenHeight * 0.6) / originalHeight * originalWidth), int(ScreenHeight * 0.6)))
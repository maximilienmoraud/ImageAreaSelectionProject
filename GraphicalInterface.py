import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import CSVParser
import ImageEditor

tempcategorie = 0
tempname = 0
iscreate = 0

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
        self.EditButton = tk.Button(self.ListFile, font=self.fontStyle2, background='#3B3F42', foreground='white', text='Edit', width=25, command=self.OpenEditor)
        self.EditButton.pack(side=TOP)

        self.Separation = tk.Label(self.master, background='#2B2B2B', foreground='white', text=' ', padx='5')
        self.Separation.pack(side=LEFT)

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
        if iscreate == 0:
            self.SupprButton = tk.Button(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white', text='Supprimer', width=26)
            self.SupprButton.pack(side=TOP)
            print(tempcategorie)
            print(tempname)
            self.SupprButton.bind('<Button-1>', lambda a='test', b='PhotoChat.jpg', c=self.ListeCategorie.get(tempcategorie), d=self.ListeName.get(tempname): CSVParser.SupprimeForm(a, b, c, d))
            iscreate = 1
        if iscreate == 1:
            self.SupprButton.destroy()
            self.SupprButton = tk.Button(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white', text='Supprimer', width=26)
            self.SupprButton.pack(side=TOP)
            print(tempcategorie)
            print(tempname)
            self.SupprButton.bind('<Button-1>', lambda a='test', b='PhotoChat.jpg', c=self.ListeCategorie.get(tempcategorie), d=self.ListeName.get(tempname): CSVParser.SupprimeForm(a, b, c, d))

    def ActualiseCategorie(self):
        categorie = CSVParser.FiltreCategorie('PhotoChat.jpg')
        i = len(categorie)
        j = 0
        self.ListeCategorie.delete(0, END)
        while j < i:
            self.ListeCategorie.insert(END, categorie[j])
            j = j + 1
        self.ListeCategorie.selection_set(tempcategorie)
        print('Actualisation Categorie Ok')

    def ActualiseName(self):
        name = CSVParser.FiltreName('PhotoChat.jpg', self.ListeCategorie.get(tempcategorie))
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
        imgfullsize = Image.open("Images/PhotoChat.jpg")
        self.imagename = 'PhotoChat.jpg'
        OriginalWidth, OriginalHeight = imgfullsize.size
        img = ResizeImage(imgfullsize, self.master.winfo_screenwidth())
        ResizedWidth, ResizedHeight = img.size
        self.scale = OriginalWidth/ResizedWidth
        img = ImageTk.PhotoImage(img)
        self.canvas = tk.Canvas(self.master, width=img.width(), height=img.height(), borderwidth=0, highlightthickness=0)
        self.canvas.pack(expand=True, side=LEFT)
        self.canvas.img = img
        self.canvas.create_image(0, 0, image=img, anchor=tk.NW)

    def OpenEditor(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ImageEditor.Editor(self.newWindow)

def ResizeImage(img, ScreenWidth):
    originalWidth, originalHeight = img.size
    return img.resize((int(ScreenWidth / 2), int(((ScreenWidth / 2) / originalWidth) * originalHeight)))
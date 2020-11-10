import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import CSVParser
import ImageEditor

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
        self.Actualise(0)
        self.ListeCategorie.pack(side=TOP)
        self.ListeName.pack(side=TOP)
        self.ListeCategorie.bind("<<ListboxSelect>>", self.Select)

        self.ActualiseButton = tk.Button(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white',text='Actualiser', width=26, command= lambda a=0:self.Actualise(a))
        self.ActualiseButton.pack(side=TOP)

        self.SupprButton = tk.Button(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white',text='Supprimer', width=26)
        self.SupprButton.pack(side=TOP)
        self.SupprButton.bind('<Button-1>', lambda a='test', b='PhotoChat.jpg', c='Objet', d='Fenetre': CSVParser.SupprimeForm(a, b, c, d))

        self.Separation = tk.Label(self.master, background='#2B2B2B', foreground='white', text=' ', padx='5')
        self.Separation.pack(side=LEFT)

    def Select(self, event):
        index = self.ListeCategorie.curselection()
        self.Actualise(index)

    def Actualise(self, index):
        print('Actualisation ok')
        categorie = CSVParser.FiltreCategorie('PhotoChat.jpg')
        i = len(categorie)
        j = 0
        self.ListeCategorie.delete(0, END)
        while j < i:
            self.ListeCategorie.insert(END, categorie[j])
            j = j + 1
        print(index)
        self.ListeCategorie.selection_set(index)
        print(self.ListeCategorie.curselection())
        print(self.ListeCategorie.get(self.ListeCategorie.curselection()))

        name = CSVParser.FiltreName('PhotoChat.jpg', self.ListeCategorie.get(self.ListeCategorie.curselection()))
        k = len(name)
        l = 0
        self.ListeName.delete(0, END)
        while l < k:
            self.ListeName.insert(END, name[l])
            l = l + 1

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
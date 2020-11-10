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

        self.ListFile = tk.Frame(self.master)
        self.ListFile.pack(side=LEFT)
        self.EditButton = tk.Button(self.ListFile, font=self.fontStyle2, background='#3B3F42', foreground='white', text='Edit', width=25, command=self.OpenEditor)
        self.ExitButton = tk.Button(self.ListFile, font=self.fontStyle2, background='#3B3F42', foreground='white', text='Exit', width=25, command=self.CloseWindow)
        self.EditButton.pack(side=TOP)
        self.ExitButton.pack(side=TOP)

        self.Image()

        self.ListFrame = tk.Frame(self.master)
        self.ListFrame.pack(side=LEFT)

        self.ListeCategorie = tk.Listbox(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white',)
        categorie = CSVParser.FiltreCategorie('PhotoChat.jpg')
        l = len(categorie)
        i = 0
        while i < l:
            self.ListeCategorie.insert(END, categorie[i])
            i = i+1
        self.ListeCategorie.pack(side=TOP)

        self.ListeName = tk.Listbox(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white',)
        name = CSVParser.FiltreName('PhotoChat.jpg', 'Objet')
        l = len(name)
        i = 0
        while i < l:
            self.ListeName.insert(END, name[i])
            i = i+1
        self.ListeName.pack(side=TOP)

        #self.SupprButton = tk.Button(self.ListFrame, font=self.fontStyle2, background='#3B3F42', foreground='white',text='Supprimer', width=25, command=CSVParser.SupprimeForm('PhotoChat.jpg', 'Objet', 'fenetre'))
        #self.SupprButton.pack(side=TOP)

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

    def CloseWindow(self):
        self.master.destroy()

def ResizeImage(img, ScreenWidth):
    originalWidth, originalHeight = img.size
    return img.resize((int(ScreenWidth / 2), int(((ScreenWidth / 2) / originalWidth) * originalHeight)))
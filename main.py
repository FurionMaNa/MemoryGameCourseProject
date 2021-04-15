import tkinter as tk

import PIL
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage

from GameRepeatClass import GameRepeatClass

imageArr = []

def delButton():
    global buttonRepeatGame
    buttonRepeatGame.destroy()
    global buttonSearchGame
    buttonSearchGame.destroy()
    global buttonQuit
    buttonQuit.destroy()

def loadImage():
    global imageArr
    for num in range(32):
        pi = Image.open(str("resource/" + str(num + 1) + ".jpg"))
        pi = pi.resize((50, 50), PIL.Image.ANTIALIAS)
        pi = PhotoImage(pi)
        imageArr.append(pi)

def StartGameRepeat():
    loadImage()
    global imageArr
    pi = Image.open("resource/field.jpg")
    pi = pi.resize((50, 50), PIL.Image.ANTIALIAS)
    pi = PhotoImage(pi)
    game = GameRepeatClass(imageArr, pi, bg='#FF00FF', highlightbackground="#8B4513")
    game.place(x=100, y=100, width=400, height=400)
    delButton()


def StartGameSearch():
    delButton()


size = 600
root = tk.Tk()
root.resizable(False, False)
root.geometry('600x600')
img = Image.open('resource/bg.png')
imag = img.resize((600, 600), Image.ANTIALIAS)
image = ImageTk.PhotoImage(imag)
panel = tk.Label(root, image=image)
panel.pack(side="top", fill="both", expand="no")
buttonRepeatGame = tk.Button(root, text='Start Game Repeat', command=StartGameRepeat, bg='#DEB887')
buttonRepeatGame.place(x=200, y=200, width=200)
buttonSearchGame = tk.Button(root, text='Start Game Search', command=StartGameSearch, bg='#DEB887')
buttonSearchGame.place(x=200, y=300, width=200)
buttonQuit = tk.Button(root, text='Quit', command=root.quit, bg='#DEB887')
buttonQuit.place(x=200, y=400, width=200)
root.mainloop()

import json
import tkinter as tk
from tkinter import messagebox

import PIL
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage
from GameSearchClass import GameSearchClass

imageArr = []

def delButton():
    global buttonRepeatGame
    buttonRepeatGame.destroy()
    global buttonSearchGame
    buttonSearchGame.destroy()
    global buttonQuit
    buttonQuit.destroy()
    global l1
    l1.destroy()

def loadImage():
    global imageArr
    for num in range(32):
        pi = Image.open(str("resource/" + str(num + 1) + ".jpg"))
        pi = pi.resize((50, 50), PIL.Image.ANTIALIAS)
        pi = PhotoImage(pi)
        imageArr.append(pi)

def aboutAuthor():
    global root
    newWindow = tk.Toplevel(root)
    frame = tk.Frame(newWindow)
    newWindow.resizable(False, False)
    newWindow.geometry('600x200')
    l1 = tk.Label(frame, text="Приложение написал Симонов Вячеслав",
                    font="Arial 18")
    l1.pack()
    l2 = tk.Label(frame, text="Студент группы ЗИС-19",
                    font="Arial 18")
    l2.pack()
    frame.pack()

def onWin(self, score):
    f = open('resource/score.json', 'w')
    f.write('{"score" : ' + str(score) + ' }')
    f.close()
    messagebox.showinfo(title="Победа", message="Поздравляем! Вы победили")

def StartGameSearch():
    loadImage()
    global imageArr
    pi = Image.open("resource/field.jpg")
    pi = pi.resize((50, 50), PIL.Image.ANTIALIAS)
    pi = PhotoImage(pi)
    game = GameSearchClass(imageArr, pi, onWin, bg='#FFD700', highlightbackground="#32160a")
    game.place(x=100, y=100, width=400, height=400)
    delButton()

size = 600
root = tk.Tk()
root.resizable(False, False)
root.geometry('600x600')
img = Image.open('resource/bg.png')
imag = img.resize((600, 600), Image.ANTIALIAS)
image = ImageTk.PhotoImage(imag)
try:
    f = open('resource/score.json', 'r')
    score = json.loads(f.read())
except:
    score = 0
panel = tk.Label(root, image=image)
panel.pack(side="top", fill="both", expand="no")
l1 = tk.Label(root, text="Last Score: " + str(score['score']))
l1.place(x=500, y=20)
buttonRepeatGame = tk.Button(root, text='Start Game Search', command=StartGameSearch, bg='#DEB887')
buttonRepeatGame.place(x=200, y=200, width=200)
buttonSearchGame = tk.Button(root, text='О авторе', command=aboutAuthor, bg='#DEB887')
buttonSearchGame.place(x=200, y=300, width=200)
buttonQuit = tk.Button(root, text='Quit', command=root.quit, bg='#DEB887')
buttonQuit.place(x=200, y=400, width=200)
root.mainloop()
import tkinter as tk
from PIL import ImageTk, Image
from GameRepeatClass import GameRepeatClass

image = []

def delButton():
    global buttonRepeatGame
    buttonRepeatGame.destroy()
    global buttonSearchGame
    buttonSearchGame.destroy()
    global buttonQuit
    buttonQuit.destroy()


def StartGameRepeat():
    game = GameRepeatClass(image ,bg='#DEB887', highlightbackground="#8B4513")
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

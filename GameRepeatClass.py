import tkinter as tk
from random import randint


class GameRepeatClass(tk.Canvas):

    map = []
    size = 50

    def __init__(self, image, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.bind("<Button-1>", self.leftClick)
        self.image = image
        for row in range(8):
            self.map.append([])
            for col in range(8):
                self.map[row].append(-1)
        for row in range(8):
            for col in range(8):
                buf = randint(0, 32)
                while not self.findRepeat(buf):
                    buf = randint(0, 32)
                self.map[row][col] = buf
        self.draw()

    def leftClick(self, event):
        col = event.x // self.size
        row = event.y // self.size
        print(self.map[row][col])

    def draw(self):
        for i in range(8):
            for j in range(8):
                self.create_rectangle(self.size * j, self.size * i, self.size * (j + 1), self.size * (i + 1))
                self.create_text(self.size * j + 10, self.size * i + 10, text=self.map[i][j])

    def findRepeat(self, b):
        count = 0
        for i in range(8):
            for j in range(8):
                if int(b) == int(self.map[i][j]):
                    count += 1
                if count > 1:
                    return False
                if int(self.map[i][j]) == -1:
                    return True
        return True




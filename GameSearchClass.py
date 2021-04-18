import time
import tkinter as tk
from random import randint

from TileClass import TileClass


class GameSearchClass(tk.Canvas):

    __map = []
    __size = 50
    __count = 0
    __buf = None
    __click = 0

    def __init__(self, image, bgImage, onWin, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.bind("<Button-1>", self.leftClick)
        self.__onWin = onWin
        for row in range(8):
            self.__map.append([])
            for col in range(8):
                self.__map[row].append(TileClass(-1, image, bgImage, self.__size * col, self.__size * row, self.__size, self))
        for row in range(8):
            for col in range(8):
                buf = randint(0, 31)
                while not self.__findRepeat(buf):
                    buf = randint(0, 31)
                self.__map[row][col] = TileClass(buf, image, bgImage, self.__size * col+25, self.__size * row+25, self.__size, self)

        self.draw()

    def leftClick(self, event):
        self.__click += 1
        col = event.x // self.__size
        row = event.y // self.__size
        if not self.__map[row][col].status:
            self.__map[row][col].click()
            print(self.__map[row][col].number)
            self.draw()
            self.update()
            self.__count += 1
            if self.__count == 1:
                self.__buf = self.__map[row][col]
            elif self.__buf.number == self.__map[row][col].number:
                self.__count = 0
                time.sleep(0.5)
                self.__buf.number = -1
                self.__map[row][col].number = -1
            else:
                time.sleep(0.5)
                self.__buf.status = False
                self.__map[row][col].status = False
                self.__count = 0
            self.draw()
        if self.__win():
            self.__onWin(self, self.__click)


    def draw(self):
        self.delete("all")
        for i in range(8):
            for j in range(8):
                self.create_rectangle(self.__size * j, self.__size * i, self.__size * (j + 1), self.__size * (i + 1))
                self.__map[i][j].draw()

    def __findRepeat(self, b):
        count = 0
        for i in range(8):
            for j in range(8):
                if b == self.__map[i][j].number:
                    count += 1
                if count > 1:
                    return False
                if int(self.__map[i][j].number) == -1:
                    return True
        return True

    def __win(self):
        for i in range(8):
            for j in range(8):
                if self.__map[i][j].number != -1:
                    return False
        return True


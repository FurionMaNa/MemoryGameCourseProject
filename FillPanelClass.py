import time
import tkinter as tk
from random import randint
from TileClass import TileClass


class FillPanelClass:

    __row = []
    __size = 50

    def __init__(self, canvas, image, bgImage, x, y):
        self.image = image
        self.bgImage = bgImage
        self.x = x
        self.y = y
        self.canvas = canvas
        for col in range(6):
            self.__row.append(TileClass(randint(0, 31), image, bgImage, self.__size * col + x, y, self.__size, canvas))
            self.__row[col].click()
        self.draw()

    def getRow(self):
        return self.__row

    def draw(self):
        self.canvas.delete("all")
        for col in range(6):
            self.__row[col].draw()

from tkinter import Canvas

from FillPanelClass import FillPanelClass


class GameRepeatClass(Canvas):

    __fillPanel = None

    def __init__(self, image, bgImage, onWin, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.__fillPanel = FillPanelClass(self, image, bgImage, 25, 25)


from calculator import Calculator
from tkinter import button

class Button(button):
    def __init__(self,calc,root,text,callback):
        super(Button, self).__init__(root,text,command=self.pushed)
        self.calculator = calc
        self.callback = callback

    def pushed(self):
        self.calculator.input(self.callback)

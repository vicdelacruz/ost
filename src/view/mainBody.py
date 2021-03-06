'''
Created on 12 Apr 2018

@author: BIKOYPOGI
'''
from tkinter.ttk import Frame, Panedwindow, Labelframe
from tkinter.constants import HORIZONTAL, BOTH
from view.testprogramPane import TestprogramPane
from view.pinsPane import PinsPane

class MainBody(Frame):
    '''
    classdocs
    '''

    def __init__(self, parent, name = 'Test Program'):
        Frame.__init__(self, parent.master)
        self.parent = parent
        self.name = name
        self.window = Panedwindow(self, orient=HORIZONTAL)
        self.lframe = Labelframe(self)
        self.lframe = TestprogramPane(self)
        self.rframe = Labelframe(self)
        self.rframe = PinsPane(self)
        
    def show(self):
        self.window.pack(fill=BOTH, expand=True)
        self.window.add(self.lframe, weight=1)
        self.window.add(self.rframe, weight=1)
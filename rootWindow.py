import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from mainFrame import mainContainer
from sideFrames import addContainer, deleteContainer
import random, os, json

class rootWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Book tracker")
        self.config(padx=15, pady=15)

        # creating a frame and assigning it to container
        self.mainCont = mainContainer(self, controller=self, width=550, height=420)

        self.sideContainers = {}
        for f in (addContainer, deleteContainer):
            frame = f(self, width=200, height=420)
            self.sideContainers[f] = frame
            frame.grid(column=1, row=0, pady=15)

        self.mainCont.grid(column=0, row=0)
        self.show_frames(addContainer)

    def show_frames(self, cont):
            self.sideContainers[cont].tkraise()

        
        



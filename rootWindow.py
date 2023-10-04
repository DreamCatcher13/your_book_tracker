import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from mainFrame import mainContainer
import random, os, json

class rootWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Book tracker")
        self.config(padx=15, pady=15)

        # creating a frame and assigning it to container
        mainCont = mainContainer(self, height=400, width=500)
        sideContainer = tk.Frame(self, height=400, width=300)
        mainCont.grid(column=0, row=0)
        sideContainer.grid(column=1, row=0)

        



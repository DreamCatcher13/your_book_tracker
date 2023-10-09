import tkinter as tk
from tkinter import  messagebox, filedialog, ttk
import json

def select_to_display():
    """function to select a few lists with books"""
    messagebox.showinfo(title="Info", message="Select one list or a few")
    filetypes = (('json files', '*.json'), ('All files', '*.*'))
    filez = filedialog.askopenfilenames(title="Select your list", filetypes=filetypes)
    list_content = {}
    for f in filez:
        with open(f, "r") as lst:
            content = json.load(lst)
            # BUG -- if the same keys (author) in different lists, it will show only values from the last list 
            list_content = list_content | content  #merging dictionaries
    return list_content
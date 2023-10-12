import tkinter as tk
from tkinter import  messagebox, filedialog
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

def cleanEntries(*arg):
    """delete all text in Entry widget"""
    for i in arg:
        i.delete(0, tk.END)

def save():
    """function to select the directory in which you want to save a new list"""
    messagebox.showinfo(title="Select a directory", message="Select a directory, where you want to save a new list")
    dir = filedialog.askdirectory()
    return dir

def select():
    """function to select a list with books"""
    messagebox.showinfo(title="Select file", message="Select *.json file with your books")
    filetypes = (('json files', '*.json'), ('All files', '*.*'))
    book_list_file = filedialog.askopenfilename(title='Select your list', filetypes=filetypes)
    with open(book_list_file, "r") as f:
        jfile = json.load(f)
    return book_list_file, jfile  

def standard(str):
    """function to standardize author \ book"""
    str = " ".join(word[0].upper() + word[1:].lower() for word in str.split()) # thanks stackoverflow
    return str

def reload_list(bk, a, book_list):
    """get new values from a list after a book was deleted"""
    bk['values'] = []
    a.set('')
    with open(book_list, "r") as f:
        jfile = json.load(f)
    a['values'] = [k for k in jfile.keys()]

def del_book(bk, athr, jfile, book_list):
    """search and delete a book"""
    books = jfile[athr]
    books.remove(bk)
    if len(books) == 0:
        jfile.pop(athr)
    else:
        jfile[athr] = books
    with open(book_list, "w") as f:
        json.dump(jfile, f, indent=4)
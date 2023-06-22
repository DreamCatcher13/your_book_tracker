from tkinter import *
from tkinter import messagebox, filedialog
import string, random
import json

###  GLOBAL VARs  ###
LIST = ""

### notes  ###
# messagebox on success \ failure
# top.destroy()

def select():
    """function to select a list with books"""
    global LIST
    messagebox.showinfo(title="Select file", message="Select *.json file with your books")
    filetypes = (('json files', '*.json'), ('All files', '*.*'))
    book_list_file = filedialog.askopenfilename(title='Select your list', filetypes=filetypes)
    LIST = book_list_file  

def add_book():
    """function to add a book to json list"""
    top = Toplevel()
    top.config(padx=5, pady=5)
    top.grab_set()

    b_name = Label(top, text="Book title")
    a_name = Label(top, text="Author's name")
    book = Entry(top, width=20)
    author = Entry(top, width=20)
    
    b_name.grid(column=1, row=1)
    book.grid(column=2, row=1, padx=5)
    a_name.grid(column=1, row=2, pady=5)
    author.grid(column=2, row=2, padx=5, pady=5)

    def create_list():
        """function to create new json list"""
        pass

    def add_to_list():
        """function to add a book to existing json list"""
        select()
        list.insert(1.0, LIST)

    new = Button(top, text="Create new list", width=15, command=create_list)
    add = Button(top, text="Add to existing list", width=15, command=add_to_list)
    new.grid(column=1, row=3, pady=5)
    add.grid(column=2, row=3, pady=5)

def random_book():
    """function to pick a random book from the list"""
    select()

def authors():
    """function to display all authors from the list"""
    select()

def books():
    """function to display all books from a list"""
    select()

###  MAIN GUI window  ###

window = Tk()
window.title("Book tracker")
window.config(padx=15, pady=15)

title = Label(text="List of all your planned \ unfinished books")
book_add = Button(text="Add a book", width=20, command=add_book) 
a_list = Button(text="List all authors", width=20, command=authors)
b_list = Button(text="List all books", width=20, command=books)
b_rand = Button(text="Random book", width=20, command=random_book)
scroll = Scrollbar(orient="vertical")
scroll.grid(row=3, column=5, sticky="ns")
list = Text(height=20, width=80, yscrollcommand=scroll.set)
scroll.config(command=list.yview)

title.grid(column=2, row=1, columnspan=2, pady=(0, 5))
book_add.grid(column=1, row=2)
a_list.grid(column=2, row=2, padx=5)
b_list.grid(column=3, row=2, padx=5)
b_rand.grid(column=4, row=2, padx=5)
list.grid(column=1, row=3, columnspan=4, pady=(10, 10))

window.mainloop()


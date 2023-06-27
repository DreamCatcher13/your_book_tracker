from tkinter import *
from tkinter import messagebox, filedialog
import random
import json

###  GLOBAL VARs  ###
LIST = ""
DIR = ""
JFILE = ""

### notes  ###
# currently only single book , but maybe later books separated by ',' 

def save():
    """function to select the directory in which you want to save a new list"""
    global DIR
    messagebox.showinfo(title="Select a directory", message="Select a directory, where you want to save a new list")
    DIR = filedialog.askdirectory()

def select():
    """function to select a list with books"""
    global LIST, JFILE
    messagebox.showinfo(title="Select file", message="Select *.json file with your books")
    filetypes = (('json files', '*.json'), ('All files', '*.*'))
    book_list_file = filedialog.askopenfilename(title='Select your list', filetypes=filetypes)
    LIST = book_list_file
    with open(LIST, "r") as f:
        JFILE = json.load(f)  

def add_book():
    """function to add a book to json list"""
    global LIST, DIR, JFILE
    top = Toplevel()
    top.config(padx=5, pady=5)
    top.grab_set()

    b_name = Label(top, text="Book title")
    a_name = Label(top, text="Author's name")
    l_name = Label(top, text="New list's name")
    book = Entry(top, width=20)
    author = Entry(top, width=20)
    new_list = Entry(top, width=20)
    
    b_name.grid(column=1, row=1)
    book.grid(column=2, row=1, padx=5)
    a_name.grid(column=1, row=2, pady=5)
    author.grid(column=2, row=2, padx=5, pady=5)
    l_name.grid(column=1, row=3, pady=5)
    new_list.grid(column=2, row=3, padx=5, pady=5)

    def create_list():
        """function to create new json list"""
        save()
        l = new_list.get()
        athr = author.get()
        bk = book.get()
        if athr and l and bk:
            data = {
                athr: [bk]
            }
            jfile = DIR + f"/{l}.json"
            with open(jfile, "w") as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo(title="Success", message="New list was created")
        else:
            messagebox.showerror(title="Error", message="You must fill all the fields")

    def add_to_list():
        """function to add a book to existing json list"""
        select()
        athr = author.get()
        bk = book.get() 
        if athr and bk:
            if athr in JFILE.keys():
                JFILE[athr].append(bk)
                with open(LIST, "w") as f:
                    json.dump(JFILE, f, indent=4)
            else:
                new_author = {
                    athr: [bk]
                }
                JFILE.update(new_author)
                with open(LIST, "w") as f:
                    json.dump(JFILE, f, indent=4)
            messagebox.showinfo(title="Success", message="Book list was updated")
        else:
            messagebox.showerror(title="Error", message="Author and Book title field should NOT be empty")

    new = Button(top, text="Create new list", width=15, command=create_list)
    add = Button(top, text="Add to existing list", width=15, command=add_to_list)
    new.grid(column=1, row=4, pady=5)
    add.grid(column=2, row=4, pady=5)

def random_book():
    """function to pick a random book from the list"""
    global LIST, DIR, JFILE
    select()
    all_books = []
    list_box.delete(1.0, END)
    for k in JFILE.keys():
        all_books += JFILE[k]
    r_bk = random.choice(all_books)
    athr = [k for k, v in JFILE.items() if r_bk in JFILE[k]] # I am really pround of this line 
    display = f"Book to read:\n\t-- {r_bk} by {athr[0]}"
    list_box.insert(1.0, display)

def authors():
    """function to display all authors from the list"""
    global LIST, DIR, JFILE
    select()
    list_box.delete(1.0, END)
    display = [ f"\t-- {str(i)}" for i in JFILE.keys() ]
    list_box.insert(1.0, f"All authors from {LIST.split('/')[-1]}:\n")
    list_box.insert(2.0, "\n".join(display))

def books():
    """function to display all books from a list"""
    global LIST, DIR, JFILE
    select()
    display = []
    list_box.delete(1.0, END)
    for k, v in JFILE.items():
        athr = f"\t* {k}:\n"
        bks = [f"\t\t-- {i}" for i in v]
        result = athr + "\n".join(bks)
        display.append(result)
    list_box.insert(1.0, f"All books from {LIST.split('/')[-1]}:\n")
    list_box.insert(2.0, "\n".join(display))

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
list_box = Text(height=20, width=80, yscrollcommand=scroll.set)
scroll.config(command=list_box.yview)

title.grid(column=2, row=1, columnspan=2, pady=(0, 5))
book_add.grid(column=1, row=2)
a_list.grid(column=2, row=2, padx=5)
b_list.grid(column=3, row=2, padx=5)
b_rand.grid(column=4, row=2, padx=5)
list_box.grid(column=1, row=3, columnspan=4, pady=(10, 10))

window.mainloop()

#газ 06358
#ел 015126
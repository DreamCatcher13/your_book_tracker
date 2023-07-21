from tkinter import *
from tkinter import messagebox, filedialog
import random, os, json

###  GLOBAL VARs  ###
LIST = ""
DIR = ""
JFILE = ""
LIST_TO_DISPLAY = ""

### notes  ###
# currently only single book , but maybe later books separated by ',' 
# start thinking about classess or refactoring 

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

def select_to_display():
    """function to select a few lists with books"""
    global LIST_TO_DISPLAY
    messagebox.showinfo(title="Info", message="Select one list or a few")
    filetypes = (('json files', '*.json'), ('All files', '*.*'))
    filez = filedialog.askopenfilenames(title="Select your list", filetypes=filetypes)
    list_content = {}
    for f in filez:
        with open(f, "r") as lst:
            content = json.load(lst)
            # BUG -- if the same keys (author) in different lists, it will show only values from the last list 
            list_content = list_content | content  #merging dictionaries
    LIST_TO_DISPLAY = list_content


def del_book(bk, athr):
    """search and delete a book"""
    books = JFILE[athr]
    books.remove(bk)
    if len(books) == 0:
        JFILE.pop(athr)
    else:
        JFILE[athr] = books
    with open(LIST, "w") as f:
        json.dump(JFILE, f, indent=4)

def standard(str):
    """function to standardize author \ book"""
    str = " ".join(word[0].upper() + word[1:] for word in str.split()) # thanks stackoverflow
    return str

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
        l = "_".join(new_list.get().split())
        athr = standard(author.get())
        bk = standard(book.get())
        if athr and l and bk:
            data = {
                athr: [bk]
            }
            jfile = os.path.join(DIR, f"{l}.json")
            with open(jfile, "w") as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo(title="Success", message="New list was created")
        else:
            messagebox.showerror(title="Error", message="You must fill all the fields")

    def add_to_list():
        """function to add a book to existing json list"""
        select()
        athr = standard(author.get())
        bk = standard(book.get()) 
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

def delete_book():
    """fucntion to delete a book or an author from a list"""
    global LIST, DIR, JFILE
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

    def delete_bk():
        """function to delete a book"""
        select()
        athr = standard(author.get())
        bk = standard(book.get())
        if athr in JFILE.keys() and bk in JFILE[athr]:
            del_book(bk=bk, athr=athr)
            messagebox.showinfo(title="Success", message="Book was deleted from a list")
        elif bk:
            found = False
            for k in JFILE.keys():
               if bk in JFILE[k]:
                found = True
                del_book(bk=bk, athr=k)
                messagebox.showinfo(title="Success", message="Book was deleted from a list")
                break
            if not found:
                messagebox.showerror(title="Error", message="Book NOT found in the list")                                  
        else:
            messagebox.showerror(title="Error", message="You must enter a book title")

    def delete_author():
        """function to delete an author from a list"""
        select()
        athr = standard(author.get())
        if athr in JFILE.keys():
            JFILE.pop(athr)
            with open(LIST, "w") as f:
                json.dump(JFILE, f, indent=4)
            messagebox.showinfo(title="Success", message="Author was deleted")
        elif athr not in JFILE.keys():
            messagebox.showerror(title="Error", message="No such author in the list")
        else:
            messagebox.showerror(title="Error", message="Author field should NOT be empty")

    b_del = Button(top, text="Delete a book", width=15, command=delete_bk)
    a_del = Button(top, text="Delete an author", width=15, command=delete_author)
    b_del.grid(column=1, row=3, pady=5)
    a_del.grid(column=2, row=3, pady=5)

def random_book():
    """function to pick a random book from the list(s)"""
    global LIST_TO_DISPLAY
    select_to_display()
    all_books = []
    list_box.delete(1.0, END)
    for k in LIST_TO_DISPLAY.keys():
        all_books += LIST_TO_DISPLAY[k]
    r_bk = random.choice(all_books)
    athr = [k for k in LIST_TO_DISPLAY.keys() if r_bk in LIST_TO_DISPLAY[k]] # I am really pround of this line 
    display = f"Book to read:\n\t-- {r_bk} by {athr[0]}"
    list_box.insert(1.0, display)

def authors():
    """function to display all authors from the list(s)"""
    global LIST_TO_DISPLAY
    select_to_display()
    list_box.delete(1.0, END)
    display = [ f"\t-- {str(i)}" for i in LIST_TO_DISPLAY.keys() ]
    list_box.insert(1.0, f"All authors from your list(s):\n")
    list_box.insert(2.0, "\n".join(display))

def books():
    """function to display all books from the list(s)"""
    global LIST_TO_DISPLAY
    select_to_display()
    display = []
    list_box.delete(1.0, END)
    for k, v in LIST_TO_DISPLAY.items():
        athr = f"\t* {k}:\n"
        bks = [f"\t\t-- {i}" for i in v]
        result = athr + "\n".join(bks)
        display.append(result)
    list_box.insert(1.0, f"All books from your list(s):\n")
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
book_delete = Button(text="Delete a book", width=20, command=delete_book)
scroll = Scrollbar(orient="vertical")
scroll.grid(row=3, column=4, sticky="ns")
list_box = Text(height=20, width=60, yscrollcommand=scroll.set)
scroll.config(command=list_box.yview)

title.grid(column=1, row=1, columnspan=4, pady=(0, 5))
book_add.grid(column=1, row=4)
book_delete.grid(column=3, row=4)
a_list.grid(column=1, row=2, padx=5)
b_list.grid(column=2, row=2, padx=5)
b_rand.grid(column=3, row=2, padx=5)
list_box.grid(column=1, row=3, columnspan=3, pady=(10, 10))

window.mainloop()

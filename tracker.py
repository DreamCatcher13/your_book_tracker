from tkinter import *
from tkinter import messagebox, filedialog, ttk
import random, os, json
from rootWindow import rootWindow 


### notes  ###
# smt weird with reload list()
# start thinking about classess or refactoring 


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

def delete_book():
    """function to delete a book or an author from a list"""
    select()
    global LIST, DIR, JFILE
    top = Toplevel()
    top.config(padx=5, pady=5)
    top.grab_set()

    def selection_changed(event):
        a = author.get()
        book['values'] = JFILE[a]

    def reload_list():
        book['values'] = []
        author.set('')
        with open(LIST, "r") as f:
            JFILE = json.load(f)
        author['values'] = [k for k in JFILE.keys()]

    b_name = Label(top, text="Book's title")
    a_name = Label(top, text="Author's name")
    book = ttk.Combobox(top, state='readonly', width=20)
    author = ttk.Combobox(top, state='readonly', width=20, values=[k for k in JFILE.keys()])
    author.bind("<<ComboboxSelected>>", selection_changed)
    
    b_name.grid(column=1, row=1)
    book.grid(column=2, row=1, padx=5)
    a_name.grid(column=1, row=2, pady=5)
    author.grid(column=2, row=2, padx=5, pady=5)

    def delete_bk():
        """function to delete a book"""
        athr = author.get()
        bk = book.get()
        if athr and bk:
            del_book(bk=bk, athr=athr)
            reload_list()
            messagebox.showinfo(title="Success", message="Book was deleted from a list")
        else:
            messagebox.showerror(title="Error", message="Author and book fields should NOT be empty")                           
            
    def delete_author():
        """function to delete an author from a list"""
        athr = author.get()
        if athr:
            JFILE.pop(athr)
            with open(LIST, "w") as f:
                json.dump(JFILE, f, indent=4)
                reload_list()
            messagebox.showinfo(title="Success", message="Author was deleted")
        else:
            messagebox.showerror(title="Error", message="Author field should NOT be empty")

    b_del = Button(top, text="Delete a book", width=15, command=delete_bk)
    a_del = Button(top, text="Delete an author", width=15, command=delete_author)
    b_del.grid(column=1, row=3, pady=5)
    a_del.grid(column=2, row=3, pady=5)



###  MAIN GUI window  ###
"""
window = Tk()
window.title("Book tracker")
window.config(padx=15, pady=15)

title = Label(text="List of all your planned \ unfinished books")
book_add = Button(text="Add books", width=20, command=add_book) 
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
"""

window =  rootWindow()
window.mainloop()
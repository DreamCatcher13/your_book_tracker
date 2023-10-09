import tkinter as tk
from tkinter import  messagebox, filedialog, ttk


class addContainer(tk.Frame):
    def __init__(self, root,  *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.grid_propagate(0)


        self.book_name = ttk.Label(self, text="Book's title\nor a few, separated by ;")
        self.author_name = ttk.Label(self, text="Author's name")
        self.list_name = ttk.Label(self, text="New list's name")
        self.book = ttk.Entry(self, width=20)
        self.author = ttk.Entry(self, width=20)
        self.new_list = ttk.Entry(self, width=20)
        
        self.book_name.grid(column=1, row=1, padx=10)
        self.book.grid(column=1, row=2, pady=5)
        self.author_name.grid(column=1, row=3, padx=10, pady=5)
        self.author.grid(column=1, row=4, pady=5)
        self.list_name.grid(column=1, row=5, padx=10, pady=5)
        self.new_list.grid(column=1, row=6, pady=5)

        self.new = ttk.Button(self, text="Create a new list", width=15)#, command=create_list)
        self.add = ttk.Button(self, text="Add to an \nexisting list", width=15)#, command=add_to_list)
        self.new.grid(column=1, row=7, pady=5)
        self.add.grid(column=1, row=8, pady=5)
"""
    def cleanEntries():
        book.delete(0, END)
        author.delete(0, END)

    def create_list():
        #function to create new json list
        save()
        l = "_".join(new_list.get().split())
        athr = standard(author.get())
        bk = [standard(b) for b in book.get().split(sep=";")]
        if athr and l and bk:
            data = {
                athr: bk
            }
            jfile = os.path.join(DIR, f"{l}.json")
            with open(jfile, "w") as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo(title="Success", message="New list was created")
            cleanEntries()
            new_list.delete(0, END)
        else:
            messagebox.showerror(title="Error", message="You must fill all the fields")

    def add_to_list():
        #function to add books to existing json list
        select()
        athr = standard(author.get())
        bk = [standard(b) for b in book.get().split(sep=";")]
        if athr and bk:
            if athr in JFILE.keys():
                for b in bk:
                    JFILE[athr].append(b)
                with open(LIST, "w") as f:
                    json.dump(JFILE, f, indent=4)
            else:
                new_author = {
                    athr: bk
                }
                JFILE.update(new_author)
                with open(LIST, "w") as f:
                    json.dump(JFILE, f, indent=4)
            messagebox.showinfo(title="Success", message="Book list was updated")
            cleanEntries()
        else:
            messagebox.showerror(title="Error", message="Author and Book title field should NOT be empty")
"""

class deleteContainer(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.grid_propagate(0)


        self.book_name = ttk.Label(self, text="Book's title")
        self.author_name = ttk.Label(self, text="Author's name")
        self.book = ttk.Combobox(self, state='readonly', width=20)

        self.book_name.grid(column=1, row=1)
        self.book.grid(column=1, row=2, pady=5)
        self.author_name.grid(column=1, row=4, pady=5)


        self.book_del = ttk.Button(self, text="Delete a book", width=15)#, command=delete_bk)
        self.author_del = ttk.Button(self, text="Delete an author", width=15)#, command=delete_author)
        self.book_del.grid(column=1, row=5, pady=5)
        self.author_del .grid(column=1, row=6, pady=5)

"""
def delete_book():
    #function to delete a book or an author from a list
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
        #function to delete a book
        athr = author.get()
        bk = book.get()
        if athr and bk:
            del_book(bk=bk, athr=athr)
            reload_list()
            messagebox.showinfo(title="Success", message="Book was deleted from a list")
        else:
            messagebox.showerror(title="Error", message="Author and book fields should NOT be empty")                           
            
    def delete_author():
        #function to delete an author from a list
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
"""
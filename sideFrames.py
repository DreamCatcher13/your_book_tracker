import tkinter as tk
from tkinter import  messagebox, filedialog, ttk
from helpers import cleanEntries, save, standard, select, reload_list, del_book
import os, json


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

        self.new = ttk.Button(self, text="Create a new list", width=15, command=self.create_list)
        self.add = ttk.Button(self, text="Add to an \nexisting list", width=15, command=self.add_to_list)
        self.new.grid(column=1, row=7, pady=5)
        self.add.grid(column=1, row=8, pady=5)


    def create_list(self):
        """function to create new json list"""
        dir = save()
        l = "_".join(self.new_list.get().split())
        athr = standard(self.author.get())
        bk = [standard(b) for b in self.book.get().split(sep=";")]
        if athr and l and bk:
            data = {
                athr: bk
            }
            jfile = os.path.join(dir, f"{l}.json")
            with open(jfile, "w") as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo(title="Success", message="New list was created")
            cleanEntries(self.book, self.author, self.new_list)
        else:
            messagebox.showerror(title="Error", message="You must fill all the fields")

    def add_to_list(self):
        """function to add books to existing json list"""
        book_list, jfile = select()
        athr = standard(self.author.get())
        bk = [standard(b) for b in self.book.get().split(sep=";")]
        if athr and bk:
            if athr in jfile.keys():
                for b in bk:
                    jfile[athr].append(b)
                with open(book_list, "w") as f:
                    json.dump(jfile, f, indent=4)
            else:
                new_author = {
                    athr: bk
                }
                jfile.update(new_author)
                with open(book_list, "w") as f:
                    json.dump(jfile, f, indent=4)
            messagebox.showinfo(title="Success", message="Book list was updated")
            cleanEntries(self.author, self.book)
        else:
            messagebox.showerror(title="Error", message="Author and Book title field should NOT be empty")


class deleteContainer(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.grid_propagate(0)

        self.book_name = ttk.Label(self, text="Book's title")
        self.author_name = ttk.Label(self, text="Author's name")
        self.book = ttk.Combobox(self, state='readonly', width=20)
        self.author = ttk.Combobox(self, state='readonly', width=20)
        self.author.bind("<<ComboboxSelected>>", self.selection_changed)
        self.book_list = ""
        self.jfile = ""

        self.book_name.grid(column=1, row=1)
        self.book.grid(column=1, row=2, pady=5)
        self.author_name.grid(column=1, row=3, pady=5)
        self.author.grid(column=1, row=4, pady=5)

        self.choose_list = ttk.Button(self, text="Choose a list", width=15, command=self.choose)
        self.book_del = ttk.Button(self, text="Delete a book", width=15, command=self.delete_book)
        self.author_del = ttk.Button(self, text="Delete an author", width=15, command=self.delete_author)
        self.choose_list.grid(column=1, row=5, pady=5)
        self.book_del.grid(column=1, row=6, pady=5)
        self.author_del .grid(column=1, row=7, pady=5)

    def selection_changed(self, event):
        a = self.author.get()
        self.book['values'] = self.jfile[a]

    def choose(self):
        self.book_list, self.jfile = select()
        reload_list(self.book, self.author, self.book_list)
 
    def delete_book(self):
        """function to delete a book or an author from a list"""
        athr = self.author.get()
        bk = self.book.get()
        if athr and bk:
            del_book(bk=bk, athr=athr, jfile=self.jfile, book_list=self.book_list)
            reload_list(self.book, self.author, self.book_list)
            messagebox.showinfo(title="Success", message="Book was deleted from a list")
        else:
            messagebox.showerror(title="Error", message="Author and book fields should NOT be empty")                           
            
    def delete_author(self):
        """function to delete an author from a list"""
        athr = self.author.get()
        if athr:
            self.jfile.pop(athr)
            with open(self.book_list, "w") as f:
                json.dump(self.jfile, f, indent=4)
            reload_list(self.book, self.author, self.book_list)
            messagebox.showinfo(title="Success", message="Author was deleted")
        else:
            messagebox.showerror(title="Error", message="Author field should NOT be empty")

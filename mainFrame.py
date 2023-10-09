import tkinter as tk
from tkinter import  messagebox, filedialog, ttk
from sideFrames import addContainer, deleteContainer
from helpers import select_to_display
class mainContainer(tk.Frame):
    def __init__(self, root,controller, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.grid_propagate(0)
        self.controller = controller

        self.title = ttk.Label(self, text="List of all your planned \ unfinished books")
        self.book_add = ttk.Button(self, text="Add books", width=20, command=lambda: controller.show_frames(addContainer)) 
        self.a_list = ttk.Button(self, text="List all authors", width=20, command=self.authors)
        self.b_list = ttk.Button(self, text="List all books", width=20)#, command=books)
        self.b_rand = ttk.Button(self, text="Random book", width=20)#, command=random_book)
        self.book_delete = ttk.Button(self, text="Delete a book", width=20, command=lambda: controller.show_frames(deleteContainer))
        self.scroll = ttk.Scrollbar(self, orient="vertical")
        self.scroll.grid(row=3, column=4, sticky="ns")
        self.list_box = tk.Text(self, height=20, width=60, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.list_box.yview)

        self.title.grid(column=1, row=1, columnspan=4, pady=(0,5))
        self.book_add.grid(column=1, row=4)
        self.book_delete.grid(column=3, row=4)
        self.a_list.grid(column=1, row=2, padx=5)
        self.b_list.grid(column=2, row=2, padx=5)
        self.b_rand.grid(column=3, row=2, padx=5)
        self.list_box.grid(column=1, row=3, columnspan=3, pady=(10, 10), padx=(5,5))

    def authors(self):
        """function to display all authors from the list(s)"""
        list = select_to_display()
        self.list_box.delete(1.0, tk.END)
        display = [ f"\t-- {str(i)}" for i in list.keys() ]
        self.list_box.insert(1.0, f"All authors from your list(s):\n")
        self.list_box.insert(2.0, "\n".join(display))
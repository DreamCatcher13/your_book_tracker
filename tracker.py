from tkinter import *
from tkinter import messagebox
import string, random
import json


###  MAIN GUI window  ###

window = Tk()
window.title("Book tracker")
window.config(padx=15, pady=15)

title = Label(text="List of all your planned \ unfinished books")
book_add = Button(text="Add a book", width=20) 
a_list = Button(text="List all authors", width=20)
b_list = Button(text="List all books", width=20)
b_rand = Button(text="Random book", width=20)
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


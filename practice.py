from tkinter import * 
from tkinter import ttk

def radiobuttons(lst):
    win = Tk()
    win.geometry("500x400")
    win.title("Library Management System")
    Label(win, text="Select Book", font="times 20", anchor='n').pack()

    val = StringVar()

    for a in range(0, len(lst)):
        Radiobutton(win, text="Dosa", padx=10, variable = val, value=a+1, font=("times", 10, "underline","bold")).pack()

    win.mainloop()

# create a function to lock the size of column width
# def handle_click(e):
#     if my_tree.identify_region(e.x, e.y) == "separator":
#         return "break"


# win.state("zoomed")
# win.mainloop()
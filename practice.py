from tkinter import * 
from tkinter import ttk

data = [
    ["John", 3, "Pepperoni"],
    ["Mayank", 2, "Das"],
    ["Mary", 5, "Chees"],
    ["Deepak", 6, "Kumar"],
    ["John", 3, "Pepperoni"],
    ["Mayank", 2, "Das"],
    ["Mary", 5, "Chees"],
    ["Deepak", 6, "Kumar"],
    ["John", 3, "Pepperoni"],
    ["Mayank", 2, "Das"],
    ["Mary", 5, "Chees"],
    ["Deepak", 6, "Kumar"],
    ["John", 3, "Pepperoni"],
    ["Mayank", 2, "Das"],
    ["Mary", 5, "Chees"],
    ["Deepak", 6, "Kumar"],
    ["John", 3, "Pepperoni"],
    ["Mayank", 2, "Das"],
    ["Mary", 5, "Chees"],
    ["Deepak", 6, "kumar"],
    ["John", 3, "pepperoni"],
    ["Mayank", 2, "das"],
    ["Mary", 5, "Chees"],
    ["Deepak", 6, "kumar"],
    ["John", 3, "pepperoni"],
    ["Mayank", 2, "das"],
    ["mary", 5, "Chees"],
    ["deepak", 6, "kumar"],
    ["john", 3, "pepperoni"],
    ["mayank", 2, "das"],
    ["mary", 5, "Chees"],
    ["deepak", 6, "kumar"],
    ["john", 3, "pepperoni"],
    ["mayank", 2, "das"],
    ["mary", 5, "Chees"],
    ["deepak", 6, "kumar"]
]


win = Tk()
win.geometry("500x400")
Label(win, text="library management system", font="times 50", anchor='n').pack()

# styling for treeview --------------->
style = ttk.Style()
# pick a theme
style.theme_use("clam")

# configure our treeview colors, row height
style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=35,
    font="times 13 ",
    fieldbackground="#D3D3D3"
    )

# Change selected color
style.map("Treeview",
    background=[('selected', 'purple')]
    )

# create a function to lock the size of column width
def handle_click(e):
    if my_tree.identify_region(e.x, e.y) == "separator":
        return "break"

# create Treeview Frame
tree_frame = Frame(win)
tree_frame.pack(pady=20)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create a treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand= tree_scroll.set, height=10)  # height is by deafult 10(how many rows)
my_tree.pack()
my_tree.bind('<Button-1>', handle_click)
# configure the scrollbar
tree_scroll.config(command=my_tree.yview)

# define our columns 
my_tree['columns']= ("Name", "Id", "L_Name")

# formate our columns
my_tree.column('#0', width=50, minwidth=0)
my_tree.column('Name', anchor=CENTER, width=150, minwidth=50)
my_tree.column('Id', anchor=CENTER, width=100)
my_tree.column('L_Name', anchor=CENTER, width=150)

# create headings
my_tree.heading("#0", text="No.", anchor=W)
my_tree.heading("Name",text="Name", anchor=CENTER)
my_tree.heading("Id",text="Id", anchor=CENTER)
my_tree.heading("L_Name",text="Last Name", anchor=CENTER)
# change font of heading
style.configure("Treeview.Heading", font="times 15 bold")

# add data
# my_tree.insert(parent='', index='end',iid=0, text="Parent", values=("john", 3, "pepperoni"))
# my_tree.pack(pady=20)

# my_tree.insert(parent='0', index='end',iid=1, text="Parent", values=("mayank", 2, "das"))

# create striped row(colorful in odd or even order) tags
my_tree.tag_configure("oddrow", background="white")
my_tree.tag_configure("evenrow", background="lightblue")

cont = 0
for item in data:
    if cont % 2 == 0:
        my_tree.insert(parent='', index='end', iid=cont, text=str((cont+1)), values=item, tags=("evenrow"))
    else:
        my_tree.insert(parent='', index='end', iid=cont, text=str((cont+1)), values=item, tags=("oddrow"))

    cont +=1




win.state("zoomed")
win.mainloop()
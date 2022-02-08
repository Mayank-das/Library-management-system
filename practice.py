from tkinter import * 
from tkinter import ttk

def radiobuttons(lst):
    global count
    count = 0
    def ok_button_hover(e):
        ok_button.config(bg="#d6eaf8")
    
    def ok_button_hover_leave(e):
        ok_button.config(bg="#E5E7E9")
    
    def cancel_button_hover(e):
        cancel_button.config(bg="#d6eaf8")
    
    def cancel_button_hover_leave(e):
        cancel_button.config(bg="#E5E7E9")
    
    def ok_end():
        global count
        win.destroy()
        count +=1

    def cancel_end():
        win.destroy()
        
    win = Tk()
    win.geometry("420x145")
    win.title("Library Management System")
    Label(win, text="Please select Book", font=("times", 15, "bold", "underline"), anchor='n', bg='white').pack()
    
    val = StringVar()
    val.set(1)

    for a in range(0, len(lst)):
        Radiobutton(win, text=f"{lst[a][0]} by {lst[a][1]}", padx=10, variable = val, value=a+1, font=("times", 10), bg='white').pack(anchor=W, pady=0)

    frame = Frame(win, bg="#F2F3F4", relief=SUNKEN)
    frame.pack(anchor=NW,fill=BOTH, expand=True)

    ok_button = Button(frame, text="OK",border=0, borderwidth=1, bg="#E5E7E9", padx=30, relief=SOLID, command= ok_end)
    cancel_button = Button(frame, text="Cancel", border=0, borderwidth=1, bg="#E5E7E9", padx=15, relief=SOLID, command= cancel_end)
    
    cancel_button.pack(side=RIGHT, padx=10, pady=5, anchor=E)
    ok_button.pack(side=RIGHT, padx=10, pady=5, anchor=E)
    ok_button.bind("<Enter>", ok_button_hover)
    ok_button.bind("<Leave>", ok_button_hover_leave)
    cancel_button.bind("<Enter>", cancel_button_hover)
    cancel_button.bind("<Leave>", cancel_button_hover_leave)

    win.resizable(0,0)
    win.configure(bg='white')
    win.mainloop()

    if count == 0:
        return False
    else:
        return lst[int(val.get())-1]

print("hello")

value = [radiobuttons([("Fundamental Of Computer Science", "P K Sinha"),
                ("Digital Electronics And Computer Organization", "M M Mano"),
                ("English Communication I", "Malti Agarwal")])]

print(value)
print(type(value))
print(value[0][1])


print("world")


# create a function to lock the size of column width
# def handle_click(e):
#     if my_tree.identify_region(e.x, e.y) == "separator":
#         return "break"


# win.state("zoomed")
# win.mainloop()
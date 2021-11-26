from tkinter import * 

def button_hover(e):
    btn["bg"]="yellow"

def button_hover_leave(e):
    btn["bg"]= "SystemButtonFace"

win = Tk()
win.geometry("500x400")
Label(win, text="library management system", font="times 50", anchor='n').pack()

btn = Button(win, text='hello')
btn.pack()

btn.bind("<Enter>", button_hover)
btn.bind("<Leave>", button_hover_leave)

win.mainloop()
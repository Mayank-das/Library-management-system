from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as msg

# hover effect
def add_button_hover(e):
    add_button.config(bg="#cccccc")
    
def add_button_hover_leave(e):
    add_button.config(bg="SystemButtonFace")

def delete_button_hover(e):
    delete_button.config(bg="#cccccc")
    
def delete_button_hover_leave(e):
    delete_button.config(bg="SystemButtonFace")

def list_button_hover(e):
    list_button.config(bg="#cccccc")
    
def list_button_hover_leave(e):
    list_button.config(bg="SystemButtonFace")

def issue_button_hover(e):
    issue_button.config(bg="#cccccc")
    
def issue_button_hover_leave(e):
    issue_button.config(bg="SystemButtonFace")

def return_button_hover(e):
    return_button.config(bg="#cccccc")
    
def return_button_hover_leave(e):
    return_button.config(bg="SystemButtonFace")

def confirm_button_hover(e):
    confirm_button.config(bg="#cccccc")
    
def confirm_button_hover_leave(e):
    confirm_button.config(bg="SystemButtonFace")

def back_button_hover(e):
    back_button.config(bg="#cccccc")
    
def back_button_hover_leave(e):
    back_button.config(bg="SystemButtonFace")

def continue_button_hover(e):
    continue_button.config(bg="#cccccc")
    
def continue_button_hover_leave(e):
    continue_button.config(bg="SystemButtonFace")

# back button
def back_button_func(text2):
    global back_button
    
    back_button = Button(win, text="← Back", font="time 15 bold", activebackground='#d3b99e',activeforeground='white', command= lambda: back_func(text2))
    back_button_window = my_canvas.create_window(40,40, anchor='nw', window=back_button)
    back_button.bind("<Enter>", back_button_hover)
    back_button.bind("<Leave>", back_button_hover_leave)

    # back from another frame to frame 1
    def back_func(fr):
        headline_label.destroy()
        headline(260,30,"Library Management System")
        back_button.destroy()
        fr.destroy()
        frame1()

# back from frame 6 to frame 5
def back_from_f6tof5(hn, func_n):
    global back_button
    back_button = Button(win, text="← Back", font="time 15 bold", activebackground='#d3b99e', activeforeground='white', command= lambda: back_func2(hn, func_n))
    back_button_window = my_canvas.create_window(40,40, anchor='nw', window=back_button)
    back_button.bind("<Enter>", back_button_hover)
    back_button.bind("<Leave>", back_button_hover_leave)

    def back_func2(hn, func_n):
        # headline_label.destroy()
        # headline(260,30,"Library Management System")
        f6.destroy()
        back_button.destroy()
        frame5(325,30,hn, func_n)

# confirm button function
def confirm_button_func():
    global confirm_button
    confirm_button = Button(f2, text="Confirm", font="Times 15 bold", activebackground="#d3b99e", activeforeground='white', command=lambda: confirm_func())
    confirm_button.grid(row = 2, column=1,pady=30)
    confirm_button.bind("<Enter>", confirm_button_hover)
    confirm_button.bind("<Leave>", confirm_button_hover_leave)

    def confirm_func():
        value = msg.askyesno("Adding book to library", "Confirm ! Do you want to add book in Library")
        if value:
            msg.askokcancel("Adding book to library", "Congratulation your book added successfully")

# delete button function
def delete_button_func():
    global delete_button
    delete_button = Button(f2, text="Delete", font="Times 15 bold", activebackground="#d3b99e", activeforeground='white', command=lambda: delete_func())
    delete_button.grid(row = 2, column=1,pady=30)
    delete_button.bind("<Enter>", delete_button_hover)
    delete_button.bind("<Leave>", delete_button_hover_leave)

    def delete_func():
        value = msg.askyesno("Deleting book from library", "Confirm ! Do you want to delete book from Library")
        if value:
            msg.askokcancel("Deleting book from library", "Congratulation you successfully delete the book")

# Issue's continue button function
def continue_func(rn, na, hn, func_n):
    # if roll_no ==  or name ==
    f5.destroy()
    back_button.destroy()
    frame6(rn,na, hn, func_n)

# Issue book function
def issue_func():
    global issue_button
    issue_button = Button(f6, text="Issue", font="Times 15 bold", activebackground="#d3b99e", activeforeground='white', command=lambda: issue())
    issue_button.grid(row = 4, column=1,pady=30)
    issue_button.bind("<Enter>", issue_button_hover)
    issue_button.bind("<Leave>", issue_button_hover_leave)

    def issue():
        value = msg.askyesno("Issue book from library", "Confirm ! Do you want to issue book from Library")
        if value:
            msg.askokcancel("Issue book from library", "Congratulation you successfully issue the book")

# Return book function
def return_func():
    global return_button
    return_button = Button(f6, text="Return", font="Times 15 bold", activebackground="#d3b99e", activeforeground='white', command=lambda: returns())
    return_button.grid(row = 4, column=1,pady=30)
    return_button.bind("<Enter>", return_button_hover)
    return_button.bind("<Leave>", return_button_hover_leave)

    def returns():
        value = msg.askyesno("Return book from library", "Confirm ! Do you want to return book to Library")
        if value:
            msg.askokcancel("Return book from library", "Congratulation you successfully return the book")

# Frame 1  -------------------------------->
def frame1():
    global add_button, delete_button, list_button, issue_button, return_button,f1
    # Create a frame
    f1 = Frame(win, bg='#d3b99e')
    f1_window = my_canvas.create_window(260,150, anchor='nw', window=f1)

    # adding imaeges
    img_label1 = Label(f1, image=img1, bg='#d3b99e', borderwidth=0)
    img_label1.grid(row=0, column=0, padx=(50,0), pady=(30,10))
    img_label2 = Label(f1, image=img2, bg='#d3b99e')
    img_label2.grid(row=0, column=2, pady=(30,10))
    img_label3 = Label(f1, image=img3, bg='#d3b99e')
    img_label3.grid(row=0, column=4, padx=(0,50), pady=(30,10))
    img_label4 = Label(f1, image=img4, bg='#d3b99e')
    img_label4.grid(row=2, column=1, pady=(30,10))
    img_label5 = Label(f1, image=img5, bg='#d3b99e')
    img_label5.grid(row=2, column=3, pady=(30,10))

    # adding buttons
    add_button = Button(f1, text='Add Book', font="Times 20", activebackground="#d3b99e",activeforeground="white", command=lambda: frame2(338,30, "Adding Book to Library", confirm_button_func))
    add_button.grid(row=1, column=0, padx=(50,0))
    delete_button = Button(f1, text='Delete Book', font="Times 20", activebackground="#d3b99e", activeforeground='white', command=lambda: frame2(280,30, "Deleting Book from Library", delete_button_func))
    delete_button.grid(row=1, column=2)
    list_button = Button(f1, text='Books List', font="Times 20", activebackground="#d3b99e",activeforeground='white')
    list_button.grid(row=1, column=4, padx=(0,50))
    issue_button = Button(f1, text='Issue Book', font="Times 20", activebackground="#d3b99e", activeforeground='white', command=lambda: frame5(325,30,"Issue Book from Library", issue_func))
    issue_button.grid(row=3, column=1, pady=(0,30))
    return_button = Button(f1, text='Return Book', font="Times 20", activeforeground='white', activebackground="#d3b99e", command=lambda: frame5(325,30,"Return Book to Library", return_func))
    return_button.grid(row=3, column=3, pady=(0,30))

    # Hover effect on Buttons
    add_button.bind("<Enter>", add_button_hover)
    add_button.bind("<Leave>", add_button_hover_leave)
    delete_button.bind("<Enter>", delete_button_hover)
    delete_button.bind("<Leave>", delete_button_hover_leave)
    list_button.bind("<Enter>", list_button_hover)
    list_button.bind("<Leave>", list_button_hover_leave)
    issue_button.bind("<Enter>", issue_button_hover)
    issue_button.bind("<Leave>", issue_button_hover_leave)
    return_button.bind("<Enter>", return_button_hover)
    return_button.bind("<Leave>", return_button_hover_leave)

# Frame 2 --------------------------->
def frame2(x, y, head_name, btn):
    global f2

    f1.destroy()
    headline_label.destroy()
    headline(x, y, head_name)

    # creating Frame 2
    f2 = Frame(win, bg='#d3b99e')
    f2_window = my_canvas.create_window(330,190, anchor='nw', window=f2)

    # book & author label
    book_name_label = Label(f2, text="Enter Book name - ", font= "Times 20 bold", bg="#d3b99e").grid(row = 0, column=0,padx=(50,0), pady=(60,30))
    author_name_label = Label(f2, text="Enter Author name - ", font= "Times 20 bold", bg="#d3b99e").grid(row = 1, column=0,padx=(50,0), pady=30)

    # book & author entry
    book_name = StringVar()
    author_name = StringVar()

    book_entry = Entry(f2, textvariable=book_name, font= "Times 20")
    book_entry.grid(row = 0, column=2,padx=(0,50), pady=(60,30), columnspan=2)
    author_entry = Entry(f2, textvariable=author_name, font= "Times 20")
    author_entry.grid(row = 1, column=2,padx=(0,50), pady=30, columnspan=2)
    
    btn()

    back_button_func(f2)

# # Frame 3 --------------------------->
# def frame3():
#     global f3,delete_button
#     f1.destroy()
#     headline_label.destroy()
#     headline(280,30,"Deleting Book from Library")
    
#     # creating Frame 3
#     f3 = Frame(win, bg='#d3b99e')
#     f3_window = my_canvas.create_window(330,190, anchor='nw', window=f3)

#     # book & author label
#     book_name_label = Label(f3, text="Enter Book name - ", font= "Times 20 bold", bg="#d3b99e").grid(row = 0, column=0,padx=(50,0), pady=(60,30))
#     author_name_label = Label(f3, text="Enter Author name - ", font= "Times 20 bold", bg="#d3b99e").grid(row = 1, column=0,padx=(50,0), pady=30)

#     # book & author entry
#     book_name = StringVar()
#     author_name = StringVar()

#     book_entry = Entry(f3, textvariable=book_name, font= "Times 20")
#     book_entry.grid(row = 0, column=2,padx=(0,50), pady=(60,30), columnspan=2)
#     author_entry = Entry(f3, textvariable=author_name, font= "Times 20")
#     author_entry.grid(row = 1, column=2,padx=(0,50), pady=30, columnspan=2)

#     # delete button
#     # delete_button = Button(f3, text="Delete", font="Times 15 bold", activebackground="#d3b99e", activeforeground='white', command=delete_func)
#     # delete_button.grid(row = 2, column=1,pady=30)
#     # delete_button.bind("<Enter>", delete_button_hover)
#     # delete_button.bind("<Leave>", delete_button_hover_leave)
#     delete_button_func()
#     back_button_func(f3)

# Frame 4 --------------------------->
# def frame4():
#     pass

# # Frame 5 --------------------------->
def frame5(x,y,had_name, func_n):
    global f5, continue_button, roll_no, name
    f1.destroy()
    headline_label.destroy()
    headline(x,y,had_name)

    # creating Frame 5
    f5 = Frame(win, bg='#d3b99e')
    f5_window = my_canvas.create_window(330,190, anchor='nw', window=f5)

    # for ask roll no & name label
    roll_no_label = Label(f5, text="Enter Roll no. - ", font= "Times 20 bold", bg="#d3b99e").grid(row = 0, column=0,padx=(50,0), pady=(60,30))
    name_label = Label(f5, text="Enter Your Name - ", font= "Times 20 bold", bg="#d3b99e").grid(row = 1, column=0,padx=(50,0), pady=30)

    # roll no & name entry
    roll_no = StringVar()
    name = StringVar()

    roll_no_entry = Entry(f5, textvariable=roll_no, font= "Times 20")
    roll_no_entry.grid(row = 0, column=2,padx=(0,50), pady=(60,30), columnspan=2)
    name_entry = Entry(f5, textvariable=name, font= "Times 20")
    name_entry.grid(row = 1, column=2,padx=(0,50), pady=30, columnspan=2)

    back_button_func(f5)
    # continue button
    continue_button = Button(f5, text="Continue", font="Times 15 bold", activebackground="#d3b99e", activeforeground='white', command=lambda: continue_func(roll_no.get(), name.get(), had_name, func_n))
    continue_button.grid(row = 2, column=1,pady=30)
    continue_button.bind("<Enter>", continue_button_hover)
    continue_button.bind("<Leave>", continue_button_hover_leave)

    # print(f"roll no = {roll_no.get()} \nname = {name.get()}")
    

# # Frame 6 --------------------------->
def frame6(rn, na, hn, func_n):
    global f6, continue_button
    headline_label.destroy()
    headline(325,30,hn)

    # creating Frame 6
    f6 = Frame(win, bg='#d3b99e')
    f6_window = my_canvas.create_window(330,190, anchor='nw', window=f6)

    # for print roll no & name 
    roll_no_label = Label(f6, text="Roll no. :- ", font= "Times 20 bold", bg="#d3b99e").grid(row = 0, column=0,padx=(50,0), pady=(60,20))
    name_label = Label(f6, text="Name :- ", font= "Times 20 bold", bg="#d3b99e").grid(row = 1, column=0,padx=(50,0), pady=(0,20))

    print_roll_no = Label(f6, text=rn , font= "Times 20 bold", bg="#d3b99e").grid(row = 0, column=2,padx=(50,0), pady=(60,20))
    print_name = Label(f6, text=na , font= "Times 20 bold", bg="#d3b99e").grid(row = 1, column=2,padx=(50,0), pady=(0,20))

    # book & author label
    book_name_label = Label(f6, text="Enter Book name - ", font= "Times 20 bold", bg="#d3b99e").grid(row = 2, column=0,padx=(50,0), pady=30)
    author_name_label = Label(f6, text="Enter Author name - ", font= "Times 20 bold", bg="#d3b99e").grid(row = 3, column=0,padx=(50,0), pady=30)

    # book & author entry
    book_name = StringVar()
    author_name = StringVar()

    book_entry = Entry(f6, textvariable=book_name, font= "Times 20")
    book_entry.grid(row = 2, column=2,padx=(0,50), pady=30, columnspan=2)
    author_entry = Entry(f6, textvariable=author_name, font= "Times 20")
    author_entry.grid(row = 3, column=2,padx=(0,50), pady=30, columnspan=2)

    # issue/return button function call
    func_n()

    back_from_f6tof5(hn, func_n)

if __name__=='__main__':
    # Normal initializing of the program
    win = Tk()
    win.geometry("1000x700")
    win.minsize(800, 450)
    win.title("Library Management System (By Mayank das)")
    win.wm_iconbitmap(r"Images\Icon image\My_Library_icon.ico")               # Add Icon

    # Taking backgraund image
    bg_image = Image.open(r'Images\Background image\bg_image1.jpg')
    bg_image = bg_image.resize((1380,730))
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Taking other images
    image1 = Image.open(r'Images\Add_book.png')
    image2 = Image.open(r'Images\Delete_book.png')
    image3 = Image.open(r'Images\Books_list.png')
    image4 = Image.open(r'Images\issue_book.png')
    image5 = Image.open(r'Images\Return_book.png')

    image1 = image1.resize((100,100))
    image2 = image2.resize((100,100))
    image3 = image3.resize((100,100))
    image4 = image4.resize((100,100))
    image5 = image5.resize((100,100))

    img1 = ImageTk.PhotoImage(image1)
    img2 = ImageTk.PhotoImage(image2)
    img3 = ImageTk.PhotoImage(image3)
    img4 = ImageTk.PhotoImage(image4)
    img5 = ImageTk.PhotoImage(image5)

    # create a canvas ---------
    my_canvas = Canvas(win, width=100, height=100)
    my_canvas.pack(fill="both", expand=True)

    # adding scrollbar 
    # my_scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=my_canvas.yview)
    # my_scrollbar.pack(side=RIGHT, fill=Y)
    # my_canvas.configure(yscrollcommand=my_scrollbar.set)
    # my_canvas.bind('<configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # add image in canvas
    my_canvas.create_image(0,0, image=bg_photo, anchor = "nw")

    # add label of library management system in canvas
    # library_label = my_canvas.create_text(700, 50, text= 'Library Management System', font="Times 50 underline bold")
    def headline(a,b,text1):
        global headline_label
        headline_label = Label(win, text= text1, font="Times 50 underline bold", bg="#d3b99e")
        headline_label_window = my_canvas.create_window(a,b, anchor='nw', window=headline_label)

    headline(260,30,"Library Management System")
    frame1()

    win.state("zoomed")
    win.mainloop()

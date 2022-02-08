from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter.messagebox as msg
import Database_for_my_library as my_db
global mysqlobj

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

def isu_rtn_button_hover(e):
    isu_rtn_button.config(bg="#cccccc")
    
def isu_rtn_button_hover_leave(e):
    isu_rtn_button.config(bg="SystemButtonFace")

def ad_button_hover(e):
    ad_button.config(bg="#cccccc")
    
def ad_button_hover_leave(e):
    ad_button.config(bg="SystemButtonFace")

def back_button_hover(e):
    back_button.config(bg="#cccccc")
    
def back_button_hover_leave(e):
    back_button.config(bg="SystemButtonFace")

def continue_button_hover(e):
    continue_button.config(bg="#cccccc")
    
def continue_button_hover_leave(e):
    continue_button.config(bg="SystemButtonFace")

def login_button_hover(e):
    login_button.config(bg="#cccccc")
    
def login_button_hover_leave(e):
    login_button.config(bg="SystemButtonFace")

def logout_button_hover(e):
    logout_button.config(bg="#cccccc")
    
def logout_button_hover_leave(e):
    logout_button.config(bg="SystemButtonFace")

# back button
def back_button_func(text2):
    global back_button
    
    back_button = Button(win, text="← Back", font="time 15 bold", activebackground='#d3d3d3',activeforeground='white', command= lambda: back_func(text2))
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

# back from frame 5 to frame 4
def back_from_f5tof4(x, y, hn, btn_n,btn_f):
    global back_button
    back_button = Button(win, text="← Back", font="time 15 bold", activebackground='#d3d3d3', activeforeground='white', command= lambda: back_func2(hn, btn_n, btn_f))
    back_button_window = my_canvas.create_window(40,40, anchor='nw', window=back_button)
    back_button.bind("<Enter>", back_button_hover)
    back_button.bind("<Leave>", back_button_hover_leave)

    def back_func2(hn, btn_n, btn_f):
        f5.destroy()
        back_button.destroy()
        frame4(x,y,hn, btn_n, btn_f)

# confirm button function
def confirm_func(bn, an):
    if bn == "" or an == "":
        msg.showwarning("Library Management System", "No Book name or Author name is found ! So please enter Book name and Author name")
    else:
        value = msg.askyesno("Adding book to library", "Confirm ! Do you want to add book in Library")
        book_name.set("")
        author_name.set("")
        if value:
            my_db.add_book(bn, an)

# delete button function
def delete_func(bn,an):
    if bn == "" or an == "":
        msg.showwarning("Library Management System", "No Book name or Author name is found ! So please enter Book name and Author name")
    else:
        value = msg.askyesno("Deleting book from library", "Confirm ! Do you want to delete book from Library")
        book_name.set("")
        author_name.set("")
        if value:
            my_db.delete_book(bn)

# Issue and return page continue button function
def continue_func(x,y,rn, hn, btn_n, btn_f):
    if rn == "":
        msg.showwarning("Library Management System", "No Roll number is found ! So please enter Roll no.")
    
    else :
        try:
            int(rn)
            bol = my_db.find_itm("student_table", "id", rn)
            if bol == True:
                na = my_db.fetch_stu_name(rn, hn)
                f4.destroy()
                back_button.destroy()
                frame5(x,y,rn,na, hn, btn_n, btn_f)
            else:
                msg.showwarning("Library Management System", "The given roll no is not find")
        except:
            msg.askokcancel("Library Management System", "Roll no must be integer ! So please enter right Roll no")

# This function is created for choosing a particular book of any author
def radiobuttons(lst, hn):
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
        root.destroy()
        count +=1

    def cancel_end():
        root.destroy()
        
    root = Tk()
    root.geometry("420x145")
    if len(lst) >= 4:
        root.geometry("420x160")
    root.title(hn)
    root.wm_iconbitmap(r"Images\Icon image\My_Library_icon.ico")
    Label(root, text="Please select Book", font=("times", 15, "bold", "underline"), anchor='n', bg='white').pack()
    
    val = StringVar()
    val.set(1)

    for a in range(0, len(lst)):
        Radiobutton(root, text=f"{lst[a][0]} by {lst[a][1]}", padx=10, variable = val, value=a+1, font=("times", 10), bg='white').pack(anchor=W, pady=0)

    frame = Frame(root, bg="#F2F3F4", relief=SUNKEN)
    frame.pack(anchor=NW,fill=BOTH, expand=True)

    ok_button = Button(frame, text="OK",border=0, borderwidth=1, bg="#E5E7E9", padx=30, relief=SOLID, command= ok_end)
    cancel_button = Button(frame, text="Cancel", border=0, borderwidth=1, bg="#E5E7E9", padx=15, relief=SOLID, command= cancel_end)
    
    cancel_button.pack(side=RIGHT, padx=10, pady=5, anchor=E)
    ok_button.pack(side=RIGHT, padx=10, pady=5, anchor=E)
    ok_button.bind("<Enter>", ok_button_hover)
    ok_button.bind("<Leave>", ok_button_hover_leave)
    cancel_button.bind("<Enter>", cancel_button_hover)
    cancel_button.bind("<Leave>", cancel_button_hover_leave)

    root.resizable(0,0)
    root.configure(bg='white')
    root.mainloop(1)

    if count == 0:
        return False
    else:
        return lst[int(val.get())-1]

# Issue book function
def issue_func(rn, bn, an, hn):
    if bn == "" and an == "":
        msg.showwarning("Issue book from library", "No Book name or Author name is found ! So please enter Book name and Author name")
    else:
        bk_or_athr = my_db.find_book_and_author(bn, an, hn)
        if len(bk_or_athr)>1:
            bk_or_athr = [radiobuttons(bk_or_athr, hn)]

        if bk_or_athr != False:
            bn = bk_or_athr[0][0]
            value = msg.askyesno("Issue book from library", f"Book name = {bk_or_athr[0][0]} \nAuthor name = {bk_or_athr[0][1]} \n\nConfirm ! Do you want to issue this book from Library")
            
            if value:
                my_db.issue_book(rn, bn)
                book_name.set("")
                author_name.set("")

# Return book function
def return_func(rn, bn, an, hn):
    if bn == "" and an == "":
        msg.showwarning("Return book to library", "No Book name or Author name is found ! So please enter Book name and Author name")
    else:
        bk_or_athr = my_db.find_book_and_author(bn, an, hn)
        if len(bk_or_athr)>1:
            bk_or_athr = [radiobuttons(bk_or_athr, hn),]

        if bk_or_athr != False:
            bn = bk_or_athr[0][0]
            value = msg.askyesno("Return book to library", f"Book name = {bk_or_athr[0][0]} \nAuthor name = {bk_or_athr[0][1]} \n\nConfirm ! Do you want to return this book to Library")
            if value:
                my_db.return_book(rn, bn)
                book_name.set("")
                author_name.set("")

# login function
def login(event):
    hst = host.get()
    usr = user.get()
    pwd = password.get()
    try:
        mysqlobj = my_db.connect_mysql(hst.strip(), usr.strip(), pwd.strip())
        my_db.create_db_tables()
        f0.destroy()
        frame1()

    except:
        if (hst=="" or usr=="" or pwd==""):
            msg.showwarning("Library Management System", "There is no empty field is allowd !\n So please fill all fields ")
        else:
            msg.showwarning("Library Management System", "Host name / User name / Password is wrong !\n So please enter right Host name / User name / Password ")

# logout function
def logout():
    my_db.close_connection()
    logout_button.destroy()
    f1.destroy()
    frame0()

# Frame 0  -------------------------------->
def frame0():
    global f0, login_button, host, user, password
    # Create a frame 0
    f0 = Frame(win, bg='#d3d3d3')
    f0_window = my_canvas.create_window(340,170, anchor='nw', window=f0)

    # host, username & password label
    host_label = Label(f0, text="Enter Host name - ", font= "Times 20 bold", bg="#d3d3d3").grid(row = 0, column=0,padx=(50,0), pady=(60,30))
    user_label = Label(f0, text="Enter User name - ", font= "Times 20 bold", bg="#d3d3d3").grid(row = 1, column=0,padx=(50,0), pady=30)
    password_label = Label(f0, text="Enter Password - ", font= "Times 20 bold", bg="#d3d3d3").grid(row = 2, column=0,padx=(50,0), pady=30)

    # host, username & password entry
    host = StringVar()
    user = StringVar()
    password = StringVar()

    host_entry = Entry(f0, textvariable=host, font= "Times 20")
    host_entry.grid(row = 0, column=2,padx=(0,50), pady=(60,30), columnspan=2)
    user_entry = Entry(f0, textvariable=user, font= "Times 20")
    user_entry.grid(row = 1, column=2,padx=(0,50), pady=30, columnspan=2)
    password_entry = Entry(f0, textvariable=password, font= "Times 20")
    password_entry.grid(row = 2, column=2,padx=(0,50), pady=30, columnspan=2)

    login_button = Button(f0, text="Login", font="Times 15 bold", activebackground="#d3d3d3", activeforeground='white', command= lambda: login(2))
    login_button.grid(row = 3, column=1,pady=30)
    login_button.bind("<Return>", login)
    login_button.bind("<Enter>", login_button_hover)
    login_button.bind("<Leave>", login_button_hover_leave)

# Frame 1  -------------------------------->
def frame1():
    global add_button, delete_button, list_button, issue_button, return_button,f1, logout_button
    f0.destroy()
    # Create a frame 1
    f1 = Frame(win, bg='#d3d3d3')
    f1_window = my_canvas.create_window(260,150, anchor='nw', window=f1)

    # adding imaeges
    img_label1 = Label(f1, image=img1, bg='#d3d3d3', borderwidth=0)
    img_label1.grid(row=0, column=0, padx=(50,0), pady=(30,10))
    img_label2 = Label(f1, image=img2, bg='#d3d3d3')
    img_label2.grid(row=0, column=2, pady=(30,10))
    img_label3 = Label(f1, image=img3, bg='#d3d3d3')
    img_label3.grid(row=0, column=4, padx=(0,50), pady=(30,10))
    img_label4 = Label(f1, image=img4, bg='#d3d3d3')
    img_label4.grid(row=2, column=1, pady=(30,10))
    img_label5 = Label(f1, image=img5, bg='#d3d3d3')
    img_label5.grid(row=2, column=3, pady=(30,10))

    # adding buttons
    add_button = Button(f1, text='Add Book', font="Times 20", activebackground="#d3d3d3",activeforeground="white", command=lambda: frame2(338,30, "Adding Book to Library", "Add", confirm_func))
    add_button.grid(row=1, column=0, padx=(50,0))
    delete_button = Button(f1, text='Delete Book', font="Times 20", activebackground="#d3d3d3", activeforeground='white', command=lambda: frame2(280,30, "Deleting Book from Library", "Delete", delete_func))
    delete_button.grid(row=1, column=2)
    list_button = Button(f1, text='Books List', font="Times 20", activebackground="#d3d3d3",activeforeground='white', command=lambda: frame3())
    list_button.grid(row=1, column=4, padx=(0,50))
    issue_button = Button(f1, text='Issue Book', font="Times 20", activebackground="#d3d3d3", activeforeground='white', command=lambda: frame4(325,30,"Issue Book from Library", "Issue", issue_func))
    issue_button.grid(row=3, column=1, pady=(0,30))
    return_button = Button(f1, text='Return Book', font="Times 20", activeforeground='white', activebackground="#d3d3d3", command=lambda: frame4(340,30,"Return Book to Library", "Return", return_func))
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

    logout_button = Button(win, text="Logout", font="time 15 bold", activebackground='#d3d3d3', activeforeground='white', command= lambda: logout())
    logout_button_window = my_canvas.create_window(1250,30, anchor='nw', window=logout_button)
    logout_button.bind("<Enter>", logout_button_hover)
    logout_button.bind("<Leave>", logout_button_hover_leave)

# Frame 2 --------------------------->
def frame2(x, y, head_name, btn_n, btn_f):
    global f2, ad_button, book_name, author_name

    f1.destroy()
    logout_button.destroy()
    headline_label.destroy()
    headline(x, y, head_name)

    # creating Frame 2
    f2 = Frame(win, bg='#d3d3d3')
    f2_window = my_canvas.create_window(340,190, anchor='nw', window=f2)

    # book & author label
    book_name_label = Label(f2, text="Enter Book name - ", font= "Times 20 bold", bg="#d3d3d3").grid(row = 0, column=0,padx=(50,0), pady=(60,30))
    author_name_label = Label(f2, text="Enter Author name - ", font= "Times 20 bold", bg="#d3d3d3").grid(row = 1, column=0,padx=(50,0), pady=30)

    # book & author entry
    book_name = StringVar()
    author_name = StringVar()

    book_entry = Entry(f2, textvariable=book_name, font= "Times 20")
    book_entry.grid(row = 0, column=2,padx=(0,50), pady=(60,30), columnspan=2)
    author_entry = Entry(f2, textvariable=author_name, font= "Times 20")
    author_entry.grid(row = 1, column=2,padx=(0,50), pady=30, columnspan=2)
    
    # btn(book_name.get(), author_name.get())
    ad_button = Button(f2, text=btn_n, font="Times 15 bold", activebackground="#d3d3d3", activeforeground='white', command=lambda: btn_f(book_name.get(), author_name.get()))
    ad_button.grid(row = 2, column=1,pady=30)
    ad_button.bind("<Enter>", ad_button_hover)
    ad_button.bind("<Leave>", ad_button_hover_leave)

    back_button_func(f2)

# Frame 3 --------------------------->
def frame3():
    global f3
    f1.destroy()
    logout_button.destroy()
    headline_label.destroy()
    headline(375,30,"All Books in Library")
    
    # creating Frame 3
    f3 = Frame(win, bg='#d3d3d3')
    f3_window = my_canvas.create_window(380,190, anchor='nw', window=f3)

    # Treeview Scrollbar
    tree_scroll = Scrollbar(f3, bg="#d3d3d3")
    tree_scroll.pack(side=RIGHT, fill=Y, pady=20, padx=(0,20))

    # styling for treeview --------------->
    style = ttk.Style()
    # pick a theme
    style.theme_use("clam")

    # configure our treeview colors, row height
    style.configure("Treeview",
        background="#d3d3d3",
        foreground="black",
        rowheight=35,
        font="times 12 ",
        fieldbackground="#d3d3d3"
        )

    # Change selected color
    style.map("Treeview",
        background=[('selected', 'purple')]
        )

    # create a function to lock the size of column width
    def handle_click(e):
        if my_tree.identify_region(e.x, e.y) == "separator":
            return "break"

    # Create a treeview
    my_tree = ttk.Treeview(f3, yscrollcommand= tree_scroll.set, height=10)  # height is by deafult 10(how many rows)
    my_tree.pack(padx=(20,0), pady=20)
    my_tree.bind('<Button-1>', handle_click)
    # configure the scrollbar
    tree_scroll.config(command=my_tree.yview)

    # define our columns 
    my_tree['columns']= ("B_Name", "A_Name")

    # formate our columns
    my_tree.column('#0', width=80, minwidth=0)
    my_tree.column('B_Name', anchor=W, width=250, minwidth=50)
    my_tree.column('A_Name', anchor=W, width=200)

    # create headings
    my_tree.heading("#0", text="Id", anchor=W)
    my_tree.heading("B_Name",text="Book Name", anchor=CENTER)
    my_tree.heading("A_Name",text="Author Name", anchor=CENTER)
    # change font of heading
    style.configure("Treeview.Heading", font="times 15 bold")

    # create striped row(colorful in odd or even order) tags
    my_tree.tag_configure("oddrow", background="white")
    my_tree.tag_configure("evenrow", background="lightblue")

    books_list = my_db.display_books()
    cont = 0
    for item in books_list:
        if cont % 2 == 0:
            my_tree.insert(parent='', index='end', iid=cont, text=str((cont+1)), values=item, tags=("evenrow"))
        else:
            my_tree.insert(parent='', index='end', iid=cont, text=str((cont+1)), values=item, tags=("oddrow"))

        cont +=1

    back_button_func(f3)


# Frame 4 --------------------------->
def frame4(x,y,had_name, btn_n, btn_f):
    global f4, continue_button, roll_no, name
    f1.destroy()
    logout_button.destroy()
    headline_label.destroy()
    headline(x,y,had_name)

    # creating Frame 4
    f4 = Frame(win, bg='#d3d3d3')
    f4_window = my_canvas.create_window(330,220, anchor='nw', window=f4)

    # for ask roll no
    roll_no_label = Label(f4, text="Enter Roll no. - ", font= "Times 25 bold", bg="#d3d3d3").grid(row = 0, column=0,padx=(50,0), pady=(80,30))

    # roll no entry
    roll_no = StringVar()

    roll_no.set("")

    roll_no_entry = Entry(f4, textvariable=roll_no, font= "Times 20")
    roll_no_entry.grid(row = 0, column=2,padx=(0,50), pady=(80,30), columnspan=2)

    back_button_func(f4)
    # continue button
    continue_button = Button(f4, text="Continue", font="Times 15 bold", activebackground="#d3d3d3", activeforeground='white', command=lambda: continue_func(x,y,roll_no.get(), had_name, btn_n, btn_f))
    continue_button.grid(row = 2, column=1,pady=(30,50))
    continue_button.bind("<Enter>", continue_button_hover)
    continue_button.bind("<Leave>", continue_button_hover_leave)
    

# # Frame 5 --------------------------->
def frame5(x,y,rn, na, hn, btn_n, btn_f):
    global f5, isu_rtn_button, book_name, author_name
    
    # creating Frame 5
    f5 = Frame(win, bg='#d3d3d3')
    f5_window = my_canvas.create_window(330,170, anchor='nw', window=f5)

    # for print roll no & name 
    roll_no_label = Label(f5, text="Roll no. :- ", font= "Times 20 bold", bg="#d3d3d3").grid(row = 0, column=0,padx=(50,0), pady=(60,20))
    name_label = Label(f5, text="Name :- ", font= "Times 20 bold", bg="#d3d3d3").grid(row = 1, column=0,padx=(50,0), pady=(0,20))

    print_roll_no = Label(f5, text=rn , font= "Times 20 bold", bg="#d3d3d3").grid(row = 0, column=2,padx=(50,0), pady=(60,20))
    print_name = Label(f5, text=na , font= "Times 20 bold", bg="#d3d3d3").grid(row = 1, column=2,padx=(50,0), pady=(0,20))

    # book & author label
    book_name_label = Label(f5, text="Enter Book name - ", font= "Times 20 bold", bg="#d3d3d3").grid(row = 2, column=0,padx=(50,0), pady=20)
    or_label = Label(f5, text="or", font= "Times 20 bold", bg="#d3d3d3").grid(row = 3, column=1)
    author_name_label = Label(f5, text="Enter Author name - ", font= "Times 20 bold", bg="#d3d3d3").grid(row = 4, column=0,padx=(50,0), pady=20)

    # book & author entry
    book_name = StringVar()
    author_name = StringVar()

    book_entry = Entry(f5, textvariable=book_name, font= "Times 20")
    book_entry.grid(row = 2, column=2,padx=(0,50), pady=20, columnspan=2)
    author_entry = Entry(f5, textvariable=author_name, font= "Times 20")
    author_entry.grid(row = 4, column=2,padx=(0,50), pady=20, columnspan=2)

    # issue/return button function call
    isu_rtn_button = Button(f5, text=btn_n , font="Times 15 bold", activebackground="#d3d3d3", activeforeground='white', command=lambda: btn_f(rn, book_name.get(),author_name.get(), hn))
    isu_rtn_button.grid(row = 5, column=1,pady=30)
    isu_rtn_button.bind("<Enter>", isu_rtn_button_hover)
    isu_rtn_button.bind("<Leave>", isu_rtn_button_hover_leave)

    back_from_f5tof4(x,y,hn, btn_n, btn_f)

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

    # add image in canvas
    my_canvas.create_image(0,0, image=bg_photo, anchor = "nw")

    # add label of library management system in canvas
    def headline(a,b,text1):
        global headline_label
        headline_label = Label(win, text= text1, font="Times 50 underline bold", bg="#d3d3d3")
        headline_label_window = my_canvas.create_window(a,b, anchor='nw', window=headline_label)

    headline(260,30,"Library Management System")
    frame0()

    win.state("zoomed")
    win.mainloop()

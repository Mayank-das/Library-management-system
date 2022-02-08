import mysql.connector
import tkinter.messagebox as msg

# connecting mysql----
def connect_mysql(hst, usr, pwd):
    global mysqlobj
    mysqlobj = mysql.connector.connect(
        host = f"{hst}",
        user = f"{usr}",
        password = f"{pwd}"
    )
    print("connected successfully")
    return mysqlobj

# close mysql connection
def close_connection():
    mysqlobj.close()
    print("closed successfully")

# Create database and tables(student and books)
def create_db_tables():
    crsr = mysqlobj.cursor()
    crsr.execute("Create Database IF NOT EXISTS My_Library_Database")
    print("database Created successfully")
    crsr.execute("Use My_Library_Database")
    print("using database successfully")
    
    crsr.execute("create table IF NOT EXISTS Book_table(Book varchar(50) primary key, Author varchar(50))")
    crsr.execute("create table IF NOT EXISTS Student_table(Id int primary key, Name varchar(50), Book varchar(50), foreign key (Book) references Book_table(Book))")
    print("tables Created successfully")

    query_book = "INSERT INTO Book_table(Book, Author) values(%s, %s)"
    value_book = [("Fundamental Of Computer Science", "P K Sinha"),
                ("Digital Electronics And Computer Organization", "M M Mano"),
                ("Mathematics I", "Gorakh Prasad"),
                ("Principles Of Management", "L M Prasad"),
                ("English Communication I", "Malti Agarwal"),
                ("Advanced Programming In C", "E Balaguruswamy"),
                ("Data Structure And Algorithms", "Narasimha Karumanchi"),
                ("Business Data Processing", "Elias M Awad"),
                ("Organisational Behabior", "L M Prasad"),
                ("Mathematics II", "H K Prasad"),
                ("Object Oriented Programming In C++", "E Balaguruswamy"),
                ("System Analysis And Design", "Elias M Awad"),
                ("Discrete Mathematics", "Marc Lipson"),
                ("Database Management System", "Sudarshan"),
                ("Operating System", "Peterson"),
                ("Web Designing And Application", "Satish Jain"),
                ("Visual Programming", "Mohammed Azam"),
                ("Data Communication And Computer Networks", "Forouzan"),
                ("Information And Cyber Security", "Mayank Bhushan"),
                ("Management Information System", "O Brian"),
                ("Java Programming", "E Balaguruswamy"),
                ("Computer Graphics And Animation", "Harington"),
                ("Software Engineering", "R S Pressman"),
                ("Fundamental Of E-Commerce", "David Whiteley"),
                ("Artificial Intelligence", "E Rich"),
                ("Multimedia And Applications", "Tay Vaughan"),
                ("Enterprise Resource Planning", "Rahul V Altekar"),
                ("Client Server Computing", "Patrick Smith"),
                ("Mobile Computing", "Shambhu Upadhyaya"),
                ("Data Warehousing And Mining", "M H Dunhan"),
                ("Data Compression", "David Salomon"),
                ("Software Testing", "Ron Patton"),
                ("Introduction To System Software", "Leland L Beck"),
                ("Cloud Computing", "Rajkumar Buyya"),
                ("Framework with ASP .Net Programming", "E Balaguruswamy"),
                ("Web Technology And Applications", "Burdman")]
    query_stu = "INSERT INTO Student_table(Id, Name) values(%s, %s)"
    value_stu = [(1, "Aadarsh Tyagi"), (2, "Aaditya Sharma"), (3, "Abdul Samad"), (4, "Abhay Chauhan"), 
                (5, "Abhinay Chauhan"), (6, "Abhishek"), (7, "Abhishek Pal"), (8, "Aditya Raghav"), 
                (9, "Akansha"), (10, "Akash"), (11, "Akash Pundir"), (13, "Akshay Thakur"), (14, "Aman kumar"), 
                (15, "Aniket Bhati"),(16, "Ankit Goswami"), (17, "Ankit Kumar"), (18, "Ankit Pal"), (19, "Ankul Kumar"), (20, "Ankul Kumar"),(21, "Ankush Kumar"), (22, "Arjun Singh"), (23, "Arpi Dubey"), (26, "Asish Pandey"), 
                (27, "Asish Tripathi"), (28, "Avnish Kumar"), (29, "Ayush Agarwal"), (30, "Bablu Kumar"),
                (31, "Bhuvneshwar Yadav"), (32, "Chitrit Raj Chauhan"), (33, "Deepak"),

                (58, "Lavi kumar"), (59, "Mayank Das"), (60, "Mayank Sharma"),
                (64, "Mohd Danish"), (73, "Mohd Shuib Khan"), (88, "Prince Dolor"), (91, "Pururaj"), (117, "Shubham")]
    try:
        crsr.executemany(query_book, value_book)
        crsr.executemany(query_stu, value_stu)
        print("inserted successfully")
    except:
        print("same data can not be entered in table/database")
    
    mysqlobj.commit()
    crsr.close()

# find book/ author/ student or any item in table
def find_itm(t_name, c_name, item):
    crsr=mysqlobj.cursor()
    crsr.execute("Use My_Library_Database")
    itm_list = []
    crsr.execute("select "+ c_name +" from " + t_name)
    records = crsr.fetchall()
    for r in records:
        itm_list.append(r[0])
    try:
        item = int(item)
        if item not in itm_list:
            return False
        else:
            return True
    except:
        if item.title() not in itm_list:
            return False
        else:
            return True

# find book if it present on particular student or not
def find_bk_by_rn(heading, rn):
    crsr=mysqlobj.cursor()
    crsr.execute("Use My_Library_Database")
    try:
        int(rn)
        try:
            crsr.execute("select book from Student_table where id =" + str(rn))
            bk = crsr.fetchone()
            if bk[0] == None:
                return ''
            else :
                return bk[0]
        except:
            msg.showwarning(heading , "Your entered number is out of range")
            return 'out of range'
    except:
        msg.showwarning(heading , "Roll no must be integer")
        return 'not integer'

# Insert book into table
def add_book(bk_name, atr_name):
    crsr = mysqlobj.cursor()
    crsr.execute("Use My_Library_Database")
    try:
        query = "insert into Book_table(book, author) values(%s, %s)"
        values = [(bk_name.title(), atr_name.title())]
        crsr.executemany(query, values)
        msg.showinfo("Adding book to library", "Congratulation your book is added successfully")
    except:
        msg.showwarning("Adding book to library","Same value does not enter again")

    mysqlobj.commit()
    crsr.close()

# delete book from table
def delete_book(bk_name):
    crsr = mysqlobj.cursor()
    crsr.execute("Use My_Library_Database")
    query = "delete from Book_table where book = %s"
    values = (bk_name,)
    boolean = find_itm("Book_table", "book", bk_name)
    if boolean == True:
        try:
            crsr.execute(query, values)
            msg.showinfo("Deleting book from library", "Congratulation you successfully delete the book")

        except :
            msg.showwarning("Deleting book from library", "Could not delete! because this book is already issued to any person")
    else:
        msg.showwarning("Deleting book from library", "Book does not find")

    mysqlobj.commit()
    crsr.close()

# display all books
def display_books():
    crsr = mysqlobj.cursor()
    crsr.execute("Use My_Library_Database")

    crsr.execute("select * from Book_table")
    records = crsr.fetchall()
    return records

# Fatch student name
def fetch_stu_name(rn, heading):
    crsr = mysqlobj.cursor()
    crsr.execute("Use My_Library_Database")

    crsr.execute(f"select Name from student_table where id = '{rn}'")
    name = crsr.fetchone()
    if name == None:
        msg.showwarning(heading, "The given roll no is not exist")

    return name[0]


# Find book and author
def find_book_and_author(bk, atr, heading):
    crsr = mysqlobj.cursor()
    crsr.execute("Use My_Library_Database")

    if bk == "":
        crsr.execute(f"select * from Book_table where author = '{atr}'")
        bk_or_atr = crsr.fetchall()
    else:
        crsr.execute(f"select * from Book_table where book = '{bk}'")
        bk_or_atr = crsr.fetchall()

    if bk_or_atr == []:
        msg.showwarning(heading, "You entered wrong book name")
        return False
    else:
        return bk_or_atr

# Issue book 
def issue_book(rl_n, bk_name):
    crsr = mysqlobj.cursor()
    crsr.execute("Use My_Library_Database")
    boolean = find_bk_by_rn("Issue book from library", rl_n)
    if boolean == '':
        try:
            query = "update Student_table set book = %s where id = %s"
            values = (bk_name.title(), rl_n)
            crsr.execute(query, values)
            mysqlobj.commit()
            msg.showinfo("Issue book from library", "Successfully issued the book")
        except:
            msg.showwarning("Issue book from library", "You entered wrong book name")
    elif boolean == 'out of range':
        pass
    elif boolean == 'not integer':
        pass
    else:
        msg.showwarning("Issue book from library", f'You already have a book name as {boolean}')
    crsr.close()

# return book 
def return_book(rl_n, bk_name):
    crsr = mysqlobj.cursor()
    crsr.execute("Use My_Library_Database")
    boolean = find_bk_by_rn("Return book to library", rl_n)
    if boolean == bk_name.title():
        crsr.execute(f"update Student_table set book = null where id = {rl_n}")
        mysqlobj.commit()
        msg.showinfo("Return book to library", "Successfully return the book")
    elif boolean == '':
        msg.showwarning("Return book to library", 'Any book did not issued to you')
    elif boolean == 'not integer':
        pass
    elif boolean == 'out of range':
        pass
    else:
        msg.showwarning("Return book to library", "You entered wrong book name")
    crsr.close()

if __name__ == '__main__':
    # hst = input("Enter host name : ")
    # usr = input("Enter user name : ")
    # pwd = input("Enter password : ")
    # connect_mysql(hst, usr, pwd)

    connect_mysql('localhost','root', 'mayankpassword')
    create_db_tables()

    # delete_book('hati')
    # print(find("emp1_db", "name", "pururaj"))
    # print(display_books())
    # print(find_bk_by_rn(1))
    # issue_book(1, 'ayank')

    # q =0
    # while q==0:
    #     n=input("1. add book\n2. delete book\n3. display all books\n4. issue book\n5. return book\n9. for quit \nchoose any value:")

    #     if n=='1':
    #         bk = input("Enter book name :")
    #         at = input("Enter author name :")
    #         add_book(bk,at)
    #     elif n=='2':
    #         bk = input("Enter book name :")
    #         delete_book(bk)
    #     elif n=='3':
    #         lst = display_books()
    #         n=0
    #         for i in lst:
    #             n+=1
    #             print(str(n) +"). "+i[0]+ "  "+ i[1])
    #     elif n=='4':
    #         bk = input("Enter book name :")
    #         rn = input("Enter your roll no :")
    #         issue_book(rn, bk)
    #     elif n=='5':
    #         bk = input("Enter book name :")
    #         rn = input("Enter your roll no :")
    #         return_book(rn,bk)
    #     elif n=='9':
    #         q += 1
    #     else:
    #         print("not valid")

    kl = find_book_and_author("","e balaguruswamy","library")
    print(len(kl))
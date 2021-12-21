import mysql.connector

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
    crsr.execute("Create Database IF NOT EXISTS TRY")
    print("database Created successfully")
    crsr.execute("Use try")
    print("using database successfully")
    
    crsr.execute("create table IF NOT EXISTS Emp2_db(work varchar(50) primary key, time varchar(50))")
    print("table Created successfully")
    crsr.execute("create table IF NOT EXISTS Emp1_db(Id int primary key, Name varchar(50), work varchar(50), foreign key (work) references emp2_db(work))")
    try:
        crsr.execute("insert into emp2_db(work, time) values('ayank', '2hr'),('ururaj', '3hr'),('hubham', '4hr') ")
        crsr.execute("insert into emp1_db(id, name, work) values(1,'Mayank', 'ayank'),(2,'Pururaj', 'ururaj'),(3,'Shubham', 'hubham') ")
        print("inserted successfully")
    except:
        print("same data can not be entered in table/database")
    
    mysqlobj.commit()
    crsr.close()

# find book/ author/ student or any item in table
def find_itm(t_name, c_name, item):
    crsr=mysqlobj.cursor()
    crsr.execute("Use try")
    itm_list = []
    crsr.execute("select "+ c_name +" from " + t_name)
    records = crsr.fetchall()
    for r in records:
        itm_list.append(r[0])
    print(itm_list)
    if item.title() not in itm_list:
        return False
    else:
        return True

# find book if it present on particular student or not
def find_bk_by_rn(rn):
    crsr=mysqlobj.cursor()
    crsr.execute("Use try")
    crsr.execute("select work from emp1_db where id =" + rn)


# Insert book into table
def add_book(bk_name, atr_name):
    crsr = mysqlobj.cursor()
    crsr.execute("Use try")
    try:
        query = "insert into emp2_db(work, time) values(%s, %s)"
        values = [(bk_name, atr_name)]
        crsr.executemany(query, values)
        print("inserted successfully")
    except:
        print("not execute or same value does not enter again")

    mysqlobj.commit()
    crsr.close()


# delete book from table
def delete_book(bk_name):
    crsr = mysqlobj.cursor()
    crsr.execute("Use try")
    query = "delete from emp2_db where work = %s"
    values = (bk_name,)
    boolean = find_itm("emp2_db", "work", bk_name)
    if boolean == True:
            crsr.execute(query, values)
            print("deleted successfully")
    else:
        print("value does not find")

    mysqlobj.commit()
    crsr.close()

# display all books
def display_books():
    crsr = mysqlobj.cursor()
    crsr.execute("Use try")

    crsr.execute("select * from emp2_db")
    records = crsr.fetchall()
    return records

# return book 
def return_book(rl_n, bk_name):
    crsr = mysqlobj.cursor()
    crsr.execute("Use try")
    boolean = find_bk_by_rn(rl_n)
    if boolean == True:
        query = "update emp1_db set work = '' "
    else:
        print("you have no book")

if __name__ == '__main__':
    # hst = input("Enter host name : ")
    # usr = input("Enter user name : ")
    # pwd = input("Enter password : ")
    # connect_mysql(hst, usr, pwd)

    connect_mysql('localhost','root', 'mayankpassword')
    create_db_tables()

    # delete_book('hati')
    # print(find("emp1_db", "name", "pururaj"))
    print(display_books())

    # q =0
    # while q==0:
    #     n=input("1. add book\n2. delete book\n9. for quit \nchoose any value:")

    #     if n==1:
    #         add_book('hati', '1hr')
    #     elif n==9:
    #         q += 1
    #     else:
    #         print("not ready")
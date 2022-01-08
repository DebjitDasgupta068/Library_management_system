def issue():
    import sqlite3
    from tabulate import tabulate
    import datetime
    conn=sqlite3.connect('Library.sqlite')
    cur=conn.cursor()
    
    print("\n1. Create new ISSUE DATABASE")
    print("2. Append existinging ISSUE DATABASE")
    op=int(input("Enter your own choice: "))
    
    if(op==1):
        cur.executescript('''
            DROP TABLE IF EXISTS Issue;

            CREATE TABLE Issue (
            Issue_id VARCHAR(128) NOT NULL PRIMARY KEY UNIQUE,
            Book_id INTEGER NOT NULL,
            Student_roll INTEGER NOT NULL,
            Issue_date TEXT NOT NULL,
            Exp_Return_date TEXT NOT NULL
            )    
            ''')
            
        print("NEW Isuue DATABASE created successfully")
        
    elif(op==2):
        print("CREATING NEW RECORDS IN ISSUE DATABASE")
    else:
        print("Wrong choice! Enter Again")
        return
    while(True):
    
        try: 
            Roll=int(input("Enter Student roll no. : "))

            print("\nCurrent Stocks Present\n")
    
            cur.execute(" SELECT book_id,book_name,book_quantity,book_authour FROM main ")
            myresult = cur.fetchall()
            print(tabulate(myresult, headers=['Book ID','Book Name', 'In Stock','Author'], tablefmt='psql'))

            book_id=input("Enter book id(s) of the books student wants to be borrow : ").split(",")
            x = tuple(book_id)
            for i in x:
                    cur.execute('''SELECT book_name FROM main WHERE book_id = ?''',(i,))
                    n=cur.fetchone()[0]
                    I_id=n+str(Roll)
                    d1=datetime.datetime.now()
                    d2=d1+datetime.timedelta(days=+150)
                    query="INSERT INTO Issue (Issue_id, Book_id, Student_roll, Issue_date, Exp_Return_date) VALUES (?,?,?,?,?)"
                    data=(I_id,i,Roll,d1,d2)
                    cur.execute(query,data)
                    cur.execute('UPDATE main SET book_quantity = book_quantity - 1 WHERE book_id = ?',(i,))
                    conn.commit()
    
            print("\n********PRINTING ISSUE TABLE********\n")
    
            cur.execute("SELECT Issue_id, Book_id, Student_roll, Issue_date, Exp_Return_date FROM Issue")
            myresult = cur.fetchall()
            print(tabulate(myresult, headers=['Issue ID', 'Book ID', 'Student Roll No.', 'Issue Date','Expected Return Date'], tablefmt='psql'))
        
        except SyntaxError:
            print("Wrong choice! Please watch out for the Syntax!")
        except TypeError:
            print("Please Enter VALID information from the MAIN LIBRARY DATABASE")
        except sqlite3.IntegrityError:
            print("Book has already been issued to the student!")
        
        print("\n Do you want to continue Issuing books to students?")
        print("1. YES")
        print("2. NO")
        np=int(input("Enter your choice: "))
        if(np==1):
            continue
        elif(np==2):
            break
        else:
            print("Wrong choice! Enter Again")
            return
    



         






    



    
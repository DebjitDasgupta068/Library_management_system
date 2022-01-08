# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:45:12 2021

@author: Subir
"""

def return_books():
    
    import sqlite3
    from tabulate import tabulate
    import datetime
    
    con=sqlite3.connect('Library.sqlite')
    cur=con.cursor()
    
    while(True):
        
        R=int(input("Enter the Student Roll Number: "))
        cur.execute("SELECT DISTINCT Student_roll FROM Issue")
        curr_roll=cur.fetchall()

        flag=0
        for i in curr_roll:
            if (R!=i[0]):
                print("Checking If the student has been issued books!.....\n")
                flag=1
                continue
            else:
                flag=0
                break
        
        if(flag==1):
            print("The Student has NO BOOKS TO RETURN")
        
        else:
        
            querySelect="SELECT Issue_id, Book_id, Student_roll, Issue_date, Exp_Return_date FROM Issue "
            queryWhere="WHERE student_roll= " + str(R)
            query=querySelect+queryWhere
            cur.execute(query)
            curr_issue=cur.fetchall()
            print("\n\nPRINTING THE STUDENT DETAILS FROM ISSUE DATABASE\n\n")
            print(tabulate(curr_issue,headers=['Issue ID', 'Book ID', 'Student Roll No.', 'Issue Date','Expected Return Date'], tablefmt='psql'))
            
            print("\n1. Are the books returned in PERFECT CONDITION?")
            print("2. Are the books DAMAGED or LOST?")
            ch=int(input("Enter your choice: "))
            
            if(ch==1):
                
                query="SELECT Exp_Return_date FROM Issue WHERE student_roll= " + str(R)
                cur.execute(query)
                curr_exp_ret_date=cur.fetchall()
                
                d1=datetime.datetime.now()
                fine=0
                
                for i in curr_exp_ret_date:
                    
                    exp_ret_date = datetime.datetime.strptime(i[0], '%Y-%m-%d %H:%M:%S.%f')
                                        
                    if(d1>exp_ret_date):
                        cur.execute("SELECT Issue_id FROM Issue WHERE Exp_Return_date= ?",(i[0],))
                        curr_issue=cur.fetchone()[0]
                        print("\nSTUDENT IS LATE FOR RETURNING BOOK: ",curr_issue)
                    
                    #calculate the no.of days passed between actual return and expected return
                        
                        x=d1-exp_ret_date
                        fine+=10*(x.days)
                        
                if(fine!=0):
                    print("\nFine for RETURNING BOOKS LATE: Rs",fine)
                    
            
                Bid=input("\nEnter the Book Id(s) of the Book Returned: ").split(',')
                x=tuple(Bid)
                try:
                    for i in x:
                        cur.execute("UPDATE main SET book_quantity=book_quantity + 1 WHERE book_id=?",(i,))
                        
                        cur.execute("SELECT Issue_id FROM Issue WHERE Student_roll=? AND book_id=?",(R,i))
                        Iid=cur.fetchone()[0]
                        cur.execute("DELETE FROM Issue Where Issue_id=?",(Iid,))
                        con.commit()
            
                    print("\n***BOOK RETURNED SUCCESFULLY AND STOCK UPDATED***\n")
                except TypeError:
                    print("Please Enter VALID information from the ISSUE database")
                
            elif(ch==2):
            
                n=int(input("Enter the number of books NOT RETURNED: "))
                price=500*n
                print("Penalty to be paid for DAMAGING/LOSING book(s): ",price)
        
            else:
                print("Wrong choice! Enter Again")
                return
        
        print("1. Continue Returning Books to the LIBRARY")
        print("2. Exit Return Function")
        op1=int(input("Enter your choioce: "))
        if(op1==1):
            continue
        elif(op1==2):
            break;
        else:
            print("Wrong choice! Enter Again")

                
       
        
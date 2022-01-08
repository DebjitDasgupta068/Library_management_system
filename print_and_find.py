# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:20:19 2021

@author: Subir
"""

def print_func():
    import sqlite3
    from tabulate import tabulate
    con=sqlite3.connect('Library.sqlite')
    cur=con.cursor()
    
    while(True):
        print("\n1. DISPLAY THE CURRENT MAIN LIBRARY DATABASE")
        print("2. DISPLAY THE RECORDS OF A PARTICULAR STUDENT DATABASE")
        print("3. DISPLAY THE CURRENT ISSUE DATABASE")
        
        op=int(input("Enter your choice: "))
        if(op==1):
            print("\n\n********** PRINTING THE MAIN LIBRARY DATABASE ***********\n\n")
    
            cur.execute(" SELECT book_id,book_name,book_quantity,book_authour FROM main ")
            curr_lib=cur.fetchall()  
            print(tabulate(curr_lib,headers=['Book ID','Book Name','Quantity','Authour'],tablefmt='psql'))
        
        elif(op==2):
            print("\n\n**********PRINTING THE RECORDS FOR A PARTICULAR STUDENT***********\n\n")
            
            roll=int(input("Enter student roll no you want to find record "))
            
            cur.execute("SELECT DISTINCT Student_roll FROM Issue")
            curr_roll=cur.fetchall()

            flag=0
            for i in curr_roll:
                if (roll!=i[0]):
                    print("Checking If the student has been issued books!.....\n")
                    flag=1
                    continue
                else:
                    flag=0
                    break
        
            if(flag==1):
                print("NO BOOKS HAS BEEN ISSUED TO THIS STUDENT!")
            else:
                cur.execute(''' SELECT Issue.Student_roll,Issue.Issue_id, main.book_name, Issue.Issue_date, Issue.Exp_Return_date from main JOIN Issue on main.book_id=Issue.book_id WHERE Student_roll=(?) ORDER BY Issue.Issue_id''',(roll,))
                table=cur.fetchall()
                print(tabulate(table,headers=[ 'Student Roll', 'Issue ID', 'Book Name','Issue Date','Expected Return Date'],tablefmt='psql'))

            
            
        elif(op==3):
            print("\n********PRINTING THE ISSUE DATABASE*********\n")
    
            cur.execute("SELECT Issue_id, Book_id, Student_roll, Issue_date, Exp_Return_date FROM Issue")
            myresult = cur.fetchall()
            print(tabulate(myresult, headers=['Issue ID', 'Book ID', 'Student Roll No.', 'Issue Date','Expected Return Date'], tablefmt='psql'))

        else:
            print("Wrong Choice! Enter Again")
        
        print("Do you want to DISPLAY RECORDS and DATABASES again?")
        print("1. Yes")
        print("2. No")
        ch=int(input("Enter your choice: "))
        if(ch==1):
            continue
        elif(ch==2):
            break
        else:
            print("Wrong choice! Enter again")
            return
            



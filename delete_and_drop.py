# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:42:18 2021

@author: Subir
"""

def delete():
    
    import sqlite3
    from tabulate import tabulate
    
    conn=sqlite3.connect('Library.sqlite')
    cur=conn.cursor()
    
    print("\n\n********** PRINTING THE CURRENT LIBRARY DATABASE ***********\n\n")
    
    cur.execute(" SELECT book_id,book_name,book_quantity,book_authour FROM main ")
    curr_lib=cur.fetchall()  
    print(tabulate(curr_lib,headers=['Book ID','Book Name','Quantity','Authour'],tablefmt='psql'))
    
    print("\n1. Delete One/Multiple Record(s)")
    print("2. Delete the Existing LIBRARY")
    op=int(input("Enter you choice: "))
    
    if(op==1):
        Bid=input("Enter the Book Id(s) of the Record(s) to be Deleted: ").split(',')
        x=tuple(Bid)
        for i in x:
            cur.execute("SELECT book_id,book_name,book_quantity,book_authour FROM main WHERE book_id=?",(i,))
            curr_lib=cur.fetchall()
            print(tabulate(curr_lib,headers=['Book ID','Book Name','Quantity','Authour'],tablefmt='psql'))
        
            queryDelete="DELETE FROM main "
            queryWhere="WHERE book_id= "+ i
            query=queryDelete+queryWhere
            cur.execute(query)
            conn.commit()
        
        print("\nRecord(s) Deleted Successfully")
        
        print("\n\n********* PRINTING THE UPDATED LIBRARY **********\n\n")
    
        cur.execute(" SELECT book_id,book_name,book_quantity,book_authour FROM main ")
        curr_lib=cur.fetchall()  
        print(tabulate(curr_lib,headers=['Book ID','Book Name','Quantity','Authour'],tablefmt='psql'))
        
    elif(op==2):
        cur.execute("DROP TABLE IF EXISTS main")
        conn.commit()
        print("\nLIBRARY DELETED SUCCESSFULLY\n")
    
    else:
        print("Wrong Choice! Enter Again")
        


        
        
    
    
    
    
    
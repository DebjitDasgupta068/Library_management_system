# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:42:28 2021

@author: Subir
"""

def edit():
    
    import sqlite3
    from tabulate import tabulate
    
    con=sqlite3.connect('Library.sqlite')
    cur=con.cursor()
    
    print("\n\n********** PRINTING THE CURRENT LIBRARY DATABASE ***********\n\n")
    
    cur.execute(" SELECT book_id,book_name,book_quantity,book_authour FROM main ")
    curr_lib=cur.fetchall()  
    print(tabulate(curr_lib,headers=['Book ID','Book Name','Quantity','Authour'],tablefmt='psql'))
    
    BID=int(input("Enter the Book ID for which the details are to be altered: "))
    
    querySelect = "SELECT * FROM main"
    queryWhere = " WHERE book_id = " + str(BID)
    query = querySelect + queryWhere
    cur.execute(query)
    
    curr_lib=cur.fetchall()
    print("\n")
    print(tabulate(curr_lib,headers=['Book ID','Book Name','Quantity','Authour'],tablefmt='psql'))
    print("\n")
    
    print("Enter which field you would like to Edit: \n")
    print("1. Book Name")
    print("2. Quantity")
    print("3. Authour")

    ch=int(input("\nEnter your choice from above options: ")) 
    
    if(ch==1):
        Bname=input("Enter the new Name of the Book: ")
        sql_update_query = """UPDATE main SET book_name = ? where book_id = ?"""
        data=(Bname,BID)
    elif(ch==2):
        Bquant=int(input("Enter the new quantity of the Book: "))
        sql_update_query = """UPDATE main SET book_quantity = ? where book_id = ?"""
        data=(Bquant,BID)
    elif(ch==3):
        Bauth=input("Enter the new authour of the book: ")
        sql_update_query = """UPDATE main SET book_authour = ? where book_id = ?"""
        data = (Bauth, BID)
        
    cur.execute(sql_update_query, data)
    con.commit()
    print("\n Record Updated successfully")
    
    print("\n\n********* PRINTING THE UPDATED LIBRARY **********\n\n")
    
    cur.execute(" SELECT book_id,book_name,book_quantity,book_authour FROM main ")
    curr_lib=cur.fetchall()  
    print(tabulate(curr_lib,headers=['Book ID','Book Name','Quantity','Authour'],tablefmt='psql'))
    
    

    
    
    
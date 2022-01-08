# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:02:07 2021

@author: Subir
"""

import add_and_build
import edit_and_update
import delete_and_drop
import issue_and_record
import return_and_stock
import print_and_find
import sqlite3

print("\n\n*********WELCOME TO THE LIBRARY MANAGEMENT SOFTWARE***********\n\n")
try:
    while(True):
        print("\nWelcmome to the main menu!\n")
        print("1. Add Books and/or Build NEW LIBRARY")
        print("2. Delete Records and/or Delete PRE-EXISTING LIBARRY")
        print("3. Edit and Update DETAILS in LIBRARY")
        print("4. Issue Books to STUDENTS")
        print("5. Return Books to LIBRARY")
        print("6. Print Current LIBRARY")
        print("7. Exit LIBRARY")
    
        opt=int(input("Enter your choice from above: "))
    
        if(opt==1):
            print("\n********CREATING LIBRARY AND RECORD DETAILS*******\n")
            add_and_build.add_or_create_main()
            
        elif(opt==2):
            print("\n********REMOVING RECORDS AND DELETE PRE-EXISTING LIBRARY*******\n")
            delete_and_drop.delete()
        
        elif(opt==3):
            print("\n********EDITING LIBRARY AND RECORD DETAILS*******\n")
            edit_and_update.edit()
        
        elif(opt==4):
            print("\n********ISSUING BOOKS TO STUDENNTS AND CREATE RECORDS**********\n")
            issue_and_record.issue()
    
        elif(opt==5):
            print("\n********RETURNING ISSUED BOOKS TO LIBRARY AND UPDATE STOCK*********\n")
            return_and_stock.return_books()
    
        elif(opt==6):
            print("\n**********DISPLAY ALL PRESENT DATABASES AND RECORDS*************\n")
            print_and_find.print_func()
        
        elif(opt==7):
            print("EXITING THE LIBRARY! HAVE A NICE DAY AHEAD")
            break
        else:
            print("Wrong choice! Please Enter Again in Main Menu: ")
            continue
        
except ValueError:
    print("Please Enter the CORRECT AND VALID information")
except sqlite3.OperationalError:
    print("CONNECTION TO DATABASE FAILED! TRY AGAIN IN 30 SECS")
        






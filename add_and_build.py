

def add_or_create_main():
    
    import sqlite3
    from tabulate import tabulate

    conn=sqlite3.connect('Library.sqlite')
    cur=conn.cursor()
    
    print("\n1. CREATE MAIN LIBRARY DATABASE")
    print("2. APPEND EXISTING MAIN LIBRARY DATABASE")
    op=int(input("Enter your own choice: "))
    
    if(op==1):
        cur.executescript('''
    
            DROP TABLE IF EXISTS main;
             
            CREATE TABLE main(
    
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_name VARCHAR(20) NOT NULL UNIQUE,
                book_quantity INT NOT NULL,
                book_authour VARCHAR(20) NOT NULL 
            )
        ''')
    elif(op==2):
         print("ADDING NEW BOOK RECORDS TO MAIN LIBRARY DATABASE")
    else:
        print("Wrong choice! Enter Again")
        return
    
    while(True):
        try:
        
            book_name=input("Enter the Book Name ")
            book_quantity=int(input("Enter the quantity of the Book shipment "))
            book_authour=input("Enter the Authour of the Book ")
            
            cur.execute('''INSERT INTO main (book_name,book_quantity,book_authour) VALUES (?,?,?)''', (book_name,book_quantity,book_authour))
            conn.commit()
            
            print("\n\n************** NEW LIBRARY ****************\n\n")
            cur.execute(" SELECT book_id,book_name,book_quantity,book_authour FROM main ")
            curr_lib=cur.fetchall()
                
            print(tabulate(curr_lib,headers=['Book ID','Book Name','Quantity','Authour'],tablefmt='psql'))
            
        except SyntaxError:
            print("Wrong choice! Please watch out for the Syntax!")
        except TypeError:
            print("Please Enter VALID INFORMATION in the MAIN LIBRARY DATABASE")
        except sqlite3.IntegrityError:
            print("BOOK has ALREADY been ADDED to the LIBRARY!")

        
        print("\n\n1. Continue with building the libarry ")
        print("2. Exit building the library ")
            
        ch=int(input("Enter your choice! "))
        if(ch==1):
            continue
        elif(ch==2):
            print("Thank you and have a nice day ahead!")
            break;
        else:
            print("Wrong Choice! Enter Again")
    
        
    

    
    
    
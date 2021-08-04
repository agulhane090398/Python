import cx_Oracle

##  CREATE CONNECTION
dsn_tns = cx_Oracle.makedsn('DESKTOP-6N33FGK', '1521', service_name='XE') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user='hr', password='hr', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
print(conn.version)

##  CURSOR TO EXECUTE COMMAND
##cur=conn.cursor()

##query='''
##CREATE TABLE STUDENTS_DATABASE(
##ROLL_NO NUMBER(3) PRIMARY KEY,
##FIRST_NAME VARCHAR2(20),
##LAST_NAME VARCHAR2(20),
##CLASS NUMBER,
##MARKS NUMBER)
##'''
##cur.execute(query)
##conn.commit()
flag=1
while(flag==1):
##  MENU
    print('Menu \Enter your choice for DATABASE MANAGEMENT : \n 1.ADD STUDENT DETAILS\n 2.REMOVE STUDENT DETAILS \n 3.UPDATE STUDENT DETAILS\n 4.VIEW ALL STUDENT DETAILS\n 5.VIEW SPECIFIC STUDENTS DETAIL \n 6.EXIT \n')
    ch=int(input())

    if ch==1:
        roll=int(input("Enter ROLL_NO: "))
        name=input("Enter FIRST_NAME: ")
        lname=input("Enter LAST_NAME: ")
        C=int(input("Enter CLASS: "))
        MARKS=int(input("Enter MARKS: "))
        l=[(roll,name,lname,C,MARKS)]
        print(l)
##        cur = conn.cursor()
##        cur.bindarraysize = 1
##        cur.setinputsizes(int, 100)
##        cur.executemany("insert into STUDENTS_DATABASE values (:1, :2, :3, :4, :5)", l)
##        conn.commit()
##        # Now query the results back
##        cur2 = conn.cursor()
##        cur2.execute('select * from mytab')
##        res = cur2.fetchall()
##        print (res)
##        cur.close()
##        cur2.close()

        
        
        try:
            cur = conn.cursor()
            cur.bindarraysize = 1
            cur.setinputsizes(int, 100)
            cur.executemany("insert into STUDENTS_DATABASE values (:1, :2, :3, :4, :5)", l)
            conn.commit()
            print('1 Row inserted')
            # Now query the results back
            cur2 = conn.cursor()
            cur2.execute('select * from STUDENTS_DATABASE')
            res = cur2.fetchall()
        except cx_Oracle.DatabaseError:
            print('Failed to insert row')
        except Exception as er:
                print(er)
 
        else:
            # To commit the transaction manually
            conn.commit()
            print('Multiple records are inserted successfully')

        conn.commit()
        
        

    elif ch==2:
        roll=int(input("Enter ROLL_NO to delete record: "))
        cur = conn.cursor()
        query=f"delete from STUDENTS_DATABASE where roll_no={roll}"
        cur.execute(query)
        conn.commit()
        
        print('1 Row deleted')
        

    elif ch==3:
        roll=int(input("Enter ROLL_NO to modify record: "))
##      delete the record
        cur = conn.cursor()
        query=f"delete from STUDENTS_DATABASE where roll_no={roll}"
        cur.execute(query)
        cur.close()
        conn.commit()
        
##      create rord with same roll no
        roll=int(input("Enter new ROLL_NO: "))
        name=input("Enter FIRST_NAME: ")
        lname=input("Enter LAST_NAME: ")
        C=int(input("Enter CLASS: "))
        MARKS=int(input("Enter MARKS: "))

        l=[(roll,name,lname,C,MARKS)]
        print("you have enter the record:",l)

        try:
            cur = conn.cursor()
            cur.bindarraysize = 1
            cur.setinputsizes(int, 100)
            cur.executemany("insert into STUDENTS_DATABASE values (:1, :2, :3, :4, :5)", l)
            conn.commit()
            print('1 Row modified')
            # Now query the results back
            cur2 = conn.cursor()
            cur2.execute('select * from STUDENTS_DATABASE')
            res = cur2.fetchall()
        except cx_Oracle.DatabaseError:
            print('Failed to insert row')
        except Exception as er:
                print(er)
 
        else:
            # To commit the transaction manually
            conn.commit()
            print('Multiple records are inserted successfully')

        conn.commit()
        
        
       

    elif ch==4:
        cur = conn.cursor()
        query="select * from STUDENTS_DATABASE"
        cur.execute(query)
        res=cur.fetchall()

        for it in res:
            print(it)
        

    elif ch==5:
        roll=int(input("Enter the student ROLL_NO: "))
        cur = conn.cursor()
        query=f"select * from STUDENTS_DATABASE where roll_no={roll}"
        cur.execute(query)
        res=cur.fetchall()
        
        for it in res:
            print(it)

    elif ch==6:
        flag=0
        print('EXITING!!')
        

    else:
        print('\nenter a valid choice!\n')


##query="drop table STUDENTS_DATABASE"
##cur.execute(query)
conn.commit()
cur.close()
conn.close()





##import sqlite3
##
##conn = sqlite3.connect('pythonDB.db')
##c = conn.cursor()
##
##def create_table():
##	c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)')
##
##def data_entry():
##	number = 1234
##	name = "GeeksforGeeks"
##	c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (number, name))
##	conn.commit()
##
##create_table()
##data_entry()
##
##c.close()
##conn.close()

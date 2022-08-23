import functools
import pyodbc
from shutil import ExecError



def connectDB(func):
    @functools.wraps(func)
    def innerWrapper(*args):
        try:
            conn= pyodbc.connect('''
                 
                Driver={SQL Server};
                Server=DESKTOP-UDFFDCR\SQLEXPRESS;
                Database=emp_db;
                Trusted_Connection=yes; 
        ''')
        except:
            print('Database Connection error')
            return None
        else:
            cursor = conn.cursor()
            rt = func(cursor, *args)
            conn.commit()
            conn.close()
            return rt
    return innerWrapper


@connectDB
def createPhonebook(cursor):
    try:
        cursor.execute('''
            create table Contacts(
            name varchar(25)
            ,number int ); 
        ''')
        print("table created")
    except Exception as e:
        print(type(e).__name__)
        print("Create table exception")
    

@connectDB
def addRecord(cursor,name,phone):
    rt={}
    try:
        cursor.execute(''' 
            insert into Contacts(name,number) values(?,?);''',(name,phone)
        )
        rt={"msg":"record-added"}
    except Exception as e:
        rt={"msg":str(e)}

    return rt

@connectDB
def searchByName(cursor,name):
    cursor.execute(''' 
        select * from Contacts
        where name = ? ;''',(name)
    )
    rt={}
    a=cursor.fetchall()
    for i in a:
        rt[i[0]] =i[1]
    return rt
    

@connectDB
def searchByNumber(cursor,phone):
    cursor.execute(''' 
        select * from Contacts
        where number = ? ;''',(phone)
    )
    rt={}
    a=cursor.fetchall()
    for i in a:
        rt[i[0]] =i[1]
    return rt
    

@connectDB
def listAll(cursor):
    cursor.execute(''' 
        select * from Contacts;
    ''')
    rt={}
    a=cursor.fetchall()
    for i in a:
        rt[i[0]] =i[1]
    return rt

    
@connectDB
def deleteByName(cursor,name):
    rt={}
    try:
        cursor.execute(''' 
            delete from Contacts
            where name = ? ;''',(name)
        )
        rt = {"msg":"record-deleted"}
    except Exception as e:
        rt ={"msg":str(e)}

    return rt
    

@connectDB
def deleteByNumber(cursor,phone):
    rt={}
    try:
        cursor.execute(''' 
            delete from Contacts
            where number = ? ;''',(phone)
        )
        rt = {"msg":"record-deleted"}
    except Exception as e:
        rt ={"msg":str(e)}

    return rt


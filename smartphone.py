import sqlite3
connection=sqlite3.connect("Mobile.db")
listoftable = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='SMARTPHONES' ").fetchall()
if listoftable!=[]:
    print("TABLE ALRREADY THERE")
else:
    connection.execute('''CREATE TABLE SMARTPHONES(
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     SERIALNO INTEGER,
                     BRAND TEXT,
                     MODELNAME TEXT,
                     MANUFACTUREYEAR INTEGER,
                     MANUFACTUREMONTH TEXT,
                     PRICE INTEGER
);''')
    print("table created successfully")

while True:
    print("Select an option from the menu")
    print("1. Add a mobile phone")
    print("2. view all mobile phone")
    print("3. search a mobile phone")
    print("4. update a mobile phone")
    print("5. delete a mobile phone")
    print("6.EXIT")

    choice = int(input("Select choice: "))
    if choice == 1:
        getserialno = input("Enter serial no: ")
        getbrand = input("Enter brand: ")
        getmodelname = input("Enter modelname: ")
        getmanufactureyear = input("Enter manufacture year: ")
        getmanufacturemonth = input("Enter manufacture month: ")
        getprice = input("Enter price: ")
        connection.execute("INSERT INTO SMARTPHONES(SERIALNO,BRAND,MODELNAME,MANUFACTUREYEAR,MANUFACTUREMONTH,PRICE)\
        VALUES("+getserialno+",'"+getbrand+"','"+getmodelname+"',"+getmanufactureyear+",'"+getmanufacturemonth+"',"+getprice+")")
        connection.commit()

        print("Inserted Successfully")
    elif choice == 2:
        result = connection.execute("SELECT * FROM SMARTPHONES")
        for i in result:
            print("ID", i[0])
            print("SERIALNO", i[1])
            print("BRAND", i[2])
            print("MODELNAME", i[3])
            print("MANUFACTUREYEAR", i[4])
            print("MANUFACTUREMONTH", i[5])
            print("PRICE", i[6])
    elif choice == 3:
        getserialno = input("Enter the serialno to be searched: ")
        result = connection.execute("SELECT * FROM SMARTPHONES WHERE SERIALNO= " + getserialno)
        for i in result:
            print("ID", i[0])
            print("SERIALNO", i[1])
            print("BRAND", i[2])
            print("MODELNAME", i[3])
            print("MANUFACTUREYEAR", i[4])
            print("MANUFACTUREMONTH", i[5])
            print("PRICE", i[6])
    elif choice == 4:
        getserialno = input("Enter serialno to be updated: ")

        getbrand = input("Enter brand: ")
        getmodelname = input("Enter modelname: ")
        getmanufactureyear = input("Enter manufacture year: ")
        getmanufacturemonth = input("Enter manufacture month: ")
        getprice = input("Enter price: ")

        connection.execute("UPDATE SMARTPHONES SET BRAND='" +getbrand+ "',\
        MODELNAME='" + getmodelname + "',MANUFACTUREYEAR=" + getmanufactureyear + ",MANUFACTUREMONTH='"+getmanufacturemonth+"',\
         PRICE="+getprice+" WHERE SERIALNO=" + getserialno)
        connection.commit()
        print("updated successfully")
        result = connection.execute("SELECT * FROM SMARTPHONES")
        for i in result:
            print("ID", i[0])
            print("SERIALNO", i[1])
            print("BRAND", i[2])
            print("MODELNAME", i[3])
            print("MANUFACTUREYEAR", i[4])
            print("MANUFACTUREMONTH", i[5])
            print("PRICE", i[6])
    elif choice == 5:
        getserialno = input("Enter serialno to be deleted: ")
        connection.execute("DELETE FROM SMARTPHONES WHERE SERIALNO=" + getserialno)
        connection.commit()
        print("Deleted Successfully")
        result = connection.execute("SELECT * FROM SMARTPHONES")
        for i in result:
            print("ID", i[0])
            print("SERIALNO", i[1])
            print("BRAND", i[2])
            print("MODELNAME", i[3])
            print("MANUFACTUREYEAR", i[4])
            print("MANUFACTUREMONTH", i[5])
            print("PRICE", i[6])
    elif choice == 6:
        connection.close()
        break
    else:
        print("Invalid choice: ")







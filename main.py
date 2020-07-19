import ConnectDB , Insert , CheckInv , CreateInvoice , getpass , cls
print("----------------Login--------------------")
usr_name = input("Username : ")
passwd = getpass.getpass()
db , cursor = ConnectDB.connect(usr_name , passwd)
cursor.execute("USE Project;")
if db == 0 or cursor == 0:
    print("Invalid username or password!!!")
else:
    cls.clr()
    print("1. Insert values into database : ")
    print("2. Check inventory for items : ")
    print("3. Create Invoice : ")
    opt = int(input("Select an option : "))
    if opt == 1:
        Insert.Insert(db , cursor)
    elif opt == 2:
        CheckInv.CheckInv(cursor)
    elif opt == 3:
        CreateInvoice.Invoice(cursor)
    else:
        print("Wrong Option....... Exiting")
        ConnectDB.disconnect(db)
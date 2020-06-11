import cls , SQL_Q
def CheckInv(cursor):
    print("Tables: ")
    print("1. AC")
    print("2. Fridges")
    print("3. Kitchen Appliances")
    print("4. TV")
    print("5. Washing Machine")
    opt = int(input("Select the table to check inventory of item : "))
    cls.clr()
    if opt == 1:
        pid = input(print("Enter the Product ID to check inventory for the item : "))
        cursor.execute(SQL_Q.CAC.format(pid))
        stock = cursor.fetchone()
        if stock is None:
            print("Wrong Product ID entered")
        else:
            print("There are" , stock , "items of Product ID" , pid , "available in stock.")
    elif opt == 2:
        pid = input(print("Enter the Product ID to check inventory for the item : "))
        cursor.execute(SQL_Q.CFR.format(pid))
        stock = cursor.fetchone()
        if stock is None:
            print("Wrong Product ID entered")
        else:
            print("There are", stock, "items of Product ID", pid, "available in stock.")
    elif opt == 3:
        pid = input(print("Enter the Product ID to check inventory for the item : "))
        cursor.execute(SQL_Q.CKA.format(pid))
        stock = cursor.fetchone()
        if stock is None:
            print("Wrong Product ID entered")
        else:
            print("There are", stock, "items of Product ID", pid, "available in stock.")
    elif opt == 4:
        pid = input(print("Enter the Product ID to check inventory for the item : "))
        cursor.execute(SQL_Q.CTV.format(pid))
        stock = cursor.fetchone()
        if stock is None:
            print("Wrong Product ID entered")
        else:
            print("There are", stock, "items of Product ID", pid, "available in stock.")
    elif opt == 5:
        pid = input(print("Enter the Product ID to check inventory for the item : "))
        cursor.execute(SQL_Q.CWS.format(pid))
        stock = cursor.fetchone()
        if stock is None:
            print("Wrong Product ID entered")
        else:
            print("There are", stock, "items of Product ID", pid, "available in stock.")
    else:
        print("Wrong Option........ Exiting")

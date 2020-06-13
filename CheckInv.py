import cls , SQL_Q ,tabulate
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
        print("1. Search with Product ID as keyword: ")
        print("2. Search with Company as keyword : ")
        print("3. Search with Colour as keyword : ")
        a = int(input("Select an option : "))
        cls.clr()
        if a == 1:
            pid = input(print("Enter the Product ID to check inventory for the item : "))
            cursor.execute(SQL_Q.CAC1.format(pid))
            result = cursor.fetchall()
            if len(result) == 0:
                print("Wrong Product ID entered")
            else:
                comp = result[0][1]
                mod = result[0][2]
                desc = result[0][3]
                prc = result[0][4]
                pic = result[0][5]
                col = result[0][6]
                print("Requested Item: ")
                print("Product ID : " , pid)
                print("Company : " , comp)
                print("Model : " , mod)
                print("Description : " , desc)
                print("Colour : " , col)
                print("Price : " , prc)
                print("Pieces Available : " , pic)
        elif a == 2:
            comp = input("Enter the name of Company to be searched : ")
            cursor.execute(SQL_Q.CAC2.format(comp))
            result = cursor.fetchall()
            result.insert(0 , ["Product ID" , "Company" , "Model" , "Description" , "Price" , "Pieces Available" , "Colour"])
            if len(result) == 1:
                print("Items from" , comp , "are unavailable")
            else:
                print("Requested Items: ")
                print(tabulate.tabulate(result , headers="firstrow" , tablefmt="pretty"))
        elif a == 3:
            col = input("Enter the Colour of item to be searched : ")
            cursor.execute(SQL_Q.CAC3.format(col))
            result = cursor.fetchall()
            result.insert(0, ["Product ID", "Company", "Model", "Description", "Price", "Pieces Available", "Colour"])
            if len(result) == 1:
                print("Items with entered colour are unavailable")
            else:
                print("Requested Items: ")
                print(tabulate.tabulate(result , headers="firstrow" , tablefmt="pretty"))
        else:
            print("Wrong Option........ Exiting")
    elif opt == 2:
        print("1. Search with Product ID as keyword: ")
        print("2. Search with Company as keyword : ")
        print("3. Search with Colour as keyword : ")
        a = int(input("Select an option : "))
        cls.clr()
        if a == 1:
            pid = input(print("Enter the Product ID to check inventory for the item : "))
            cursor.execute(SQL_Q.CFR1.format(pid))
            result = cursor.fetchall()
            if len(result) == 0:
                print("Wrong Product ID entered")
            else:
                comp = result[0][1]
                mod = result[0][2]
                desc = result[0][3]
                prc = result[0][4]
                pic = result[0][5]
                col = result[0][6]
                print("Requested Item: ")
                print("Product ID : ", pid)
                print("Company : ", comp)
                print("Model : ", mod)
                print("Description : ", desc)
                print("Colour : ", col)
                print("Price : ", prc)
                print("Pieces Available : ", pic)
        elif a == 2:
            comp = input("Enter the name of Company to be searched : ")
            cursor.execute(SQL_Q.CFR2.format(comp))
            result = cursor.fetchall()
            result.insert(0, ["Product ID", "Company", "Model", "Description", "Price", "Pieces Available", "Colour"])
            if len(result) == 1:
                print("Items from" , comp , "are unavailable")
            else:
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
        elif a == 3:
            col = input("Enter the colour of item to be searched : ")
            cursor.execute(SQL_Q.CFR3.format(col))
            result = cursor.fetchall()
            result.insert(0, ["Product ID", "Company", "Model", "Description", "Price", "Pieces Available", "Colour"])
            if len(result) == 1:
                print("Items with entered colour are unavailable")
            else:
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
        else:
            print("Wrong Option......... Exiting")
    elif opt == 3:
        print("1. Search with Product ID as keyword: ")
        print("2. Search with Company as keyword : ")
        print("3. Search with Type as keyword : ")
        a = int(input("Select an option : "))
        cls.clr()
        if a == 1:
            pid = input(print("Enter the Product ID to check inventory for the item : "))
            cursor.execute(SQL_Q.CKA1.format(pid))
            result = cursor.fetchall()
            if len(result) == 0:
                print("Wrong Product ID entered")
            else:
                type = result[0][1]
                comp = result[0][2]
                name = result[0][3]
                prc = result[0][4]
                pic = result[0][5]
                print("Requested Item: ")
                print("Product ID : ", pid)
                print("Company : ", comp)
                print("Type : ", type)
                print("Name : " , name)
                print("Price : ", prc)
                print("Pieces Available : ", pic)
        elif a == 2:
            comp = input("Enter the name of Company to be searched : ")
            cursor.execute(SQL_Q.CKA2.format(comp))
            result = cursor.fetchall()
            result.insert(0, ["Product ID", "Type" , "Company", "Name" , "Price", "Pieces Available"])
            if len(result) == 1:
                print("Items from" , comp , "are unavailable")
            else:
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
        elif a == 3:
            print("1. Dishwasher : ")
            print("2. Food Processor : ")
            print("3. Mixer : ")
            print("4. Microwave Oven : ")
            b = int(input("Select an option : "))
            if b == 1:
                cursor.execute(SQL_Q.CKA3.format("Dishwasher"))
                result = cursor.fetchall()
                result.insert(0, ["Product ID", "Type", "Company", "Name", "Price", "Pieces Available"])
                print("Requested Items : ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
            elif b == 2:
                cursor.execute(SQL_Q.CKA3.format("Food Processor"))
                result = cursor.fetchall()
                result.insert(0, ["Product ID", "Type", "Company", "Name", "Price", "Pieces Available"])
                print("Requested Items : ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
            elif b == 3:
                cursor.execute(SQL_Q.CKA3.format("Mixer"))
                result = cursor.fetchall()
                result.insert(0, ["Product ID", "Type", "Company", "Name", "Price", "Pieces Available"])
                print("Requested Items : ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
            elif b == 4:
                cursor.execute(SQL_Q.CKA3.format("Microwave Oven"))
                result = cursor.fetchall()
                result.insert(0, ["Product ID", "Type", "Company", "Name", "Price", "Pieces Available"])
                print("Requested Items : ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
            else:
                print("Wrong Option..... Exiting")
        else:
            print("Wrong Option....... Exiting")
    elif opt == 4:
        print("1. Search with Product ID as keyword: ")
        print("2. Search with Company as keyword : ")
        print("3. Search with Screen Size as keyword : ")
        a = int(input("Select an option : "))
        cls.clr()
        if a == 1:
            pid = input(print("Enter the Product ID to check inventory for the item : "))
            cursor.execute(SQL_Q.CTV1.format(pid))
            result = cursor.fetchall()
            if len(result) == 0:
                print("Wrong Product ID entered")
            else:
                comp = result[0][1]
                name = result[0][2]
                size = result[0][3]
                prc = result[0][4]
                pic = result[0][5]
                desc = result[0][6]
                print("Requested Item: ")
                print("Product ID : ", pid)
                print("Company : ", comp)
                print("Name : ", name)
                print("Screen Size (inches) : " , size)
                print("Description : ", desc)
                print("Price : ", prc)
                print("Pieces Available : ", pic)
        elif a == 2:
            comp = input("Enter the name of Company to be searched : ")
            cursor.execute(SQL_Q.CTV2.format(comp))
            result = cursor.fetchall()
            result.insert(0, ["Product ID", "Company", "Name", "Size", "Price", "Pieces Available", "Description"])
            if len(result) == 1:
                print("Items from" , comp , "are unavailable")
            else:
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
        elif a == 3:
            size = int(input("Enter the screen size of item to be searched : "))
            cursor.execute(SQL_Q.CTV3.format(size))
            result = cursor.fetchall()
            result.insert(0, ["Product ID", "Company", "Name", "Size", "Price", "Pieces Available", "Description"])
            if len(result) == 1:
                print("Items with screen size" , size , "inches are unavailable")
            else:
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
        else:
            print("Wrong Option........ Exiting")
    elif opt == 5:
        print("1. Search with Product ID as keyword: ")
        print("2. Search with Company as keyword : ")
        print("3. Search with Colour as keyword : ")
        print("4. Search with Type as keyword : ")
        a = int(input("Select an option : "))
        cls.clr()
        if a == 1:
            pid = input(print("Enter the Product ID to check inventory for the item : "))
            cursor.execute(SQL_Q.CWS1.format(pid))
            result = cursor.fetchall()
            if len(result) == 0:
                print("Wrong Product ID entered")
            else:
                comp = result[0][1]
                mod = result[0][2]
                desc = result[0][3]
                prc = result[0][4]
                type = result[0][5]
                pic = result[0][6]
                col = result[0][7]
                print("Requested Item: ")
                print("Product ID : ", pid)
                print("Company : ", comp)
                print("Type: " , type)
                print("Model : ", mod)
                print("Description : ", desc)
                print("Colour : ", col)
                print("Price : ", prc)
                print("Pieces Available : ", pic)
        elif a == 2:
            comp = input("Enter the name of Company to be searched : ")
            cursor.execute(SQL_Q.CWS2.format(comp))
            result = cursor.fetchall()
            result.insert(0, ["Product ID", "Company", "Model", "Description", "Price", "Type" , "Pieces Available", "Colour"])
            if len(result) == 1:
                print("Items from" , comp , "are unavailable")
            else:
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
        elif a == 3:
            col = input("Enter the colour of item to be searched : ")
            cursor.execute(SQL_Q.CWS3.format(col))
            result = cursor.fetchall()
            result.insert(0, ["Product ID", "Company", "Model", "Description", "Price", "Type" , "Pieces Available", "Colour"])
            if len(result) == 1:
                print("Items with entered colour are unavailable")
            else:
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
        elif a == 4:
            print("1. Semi Automatic : ")
            print("2. Fully Automatic Top Load : ")
            print("3. Fully Automatic Front Load : ")
            b = int(input("Select an option : "))
            if b == 1:
                cursor.execute(SQL_Q.CWS4.format("Semi Automatic"))
                result = cursor.fetchall()
                result.insert(0, ["Product ID", "Company", "Model", "Description", "Price", "Type", "Pieces Available", "Colour"])
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
            elif b == 2:
                cursor.execute(SQL_Q.CWS4.format("Fully Automatic Top Load"))
                result = cursor.fetchall()
                result.insert(0, ["Product ID", "Company", "Model", "Description", "Price", "Type", "Pieces Available", "Colour"])
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
            elif b == 3:
                cursor.execute(SQL_Q.CWS4.format("Fully Automatic Front Load"))
                result = cursor.fetchall()
                result.insert(0, ["Product ID", "Company", "Model", "Description", "Price", "Type", "Pieces Available", "Colour"])
                print("Requested Items: ")
                print(tabulate.tabulate(result, headers="firstrow", tablefmt="pretty"))
            else:
                print("Wrong Option....... Exiting")
        else:
            print("Wrong Option........ Exiting")
    else:
        print("Wrong Option........ Exiting")
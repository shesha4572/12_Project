import cls , SQL_Q
def Insert(db , cursor):
    print("Tables: ")
    print("1. AC")
    print("2. Fridges")
    print("3. Kitchen Appliances")
    print("4. TV")
    print("5. Washing Machine")
    opt = int(input("Select the table to insert values into: "))
    cls.clr()
    if opt == 1:
        print("1. Insert one row : ")
        print("2. Insert multiple rows : ")
        a = int(input("Select one option : "))
        if a == 1:
            cls.clr()
            pid = input("Product_ID : ")
            company = input(("Company : "))
            model = input("Model : ")
            desc = input("Description : ")
            price = float(input("Price : "))
            pieces = int(input("Pieces : "))
            colour = input("Colour : ")
            try:
                cursor.execute(SQL_Q.IAC.format(pid , company , model , desc , price , pieces , colour))
                db.commit()
                print("1 row inserted successfuly into table AC")
            except:
                db.rollback()
                print("Error in inserting row(s) to table")
        elif a == 2:
            b = int(input("Enter number of rows to be inserted into table AC : "))
            cls.clr()
            for i in range(0 , b):
                pid = input("Product_ID : ")
                company = input(("Company : "))
                model = input("Model : ")
                desc = input("Description : ")
                price = float(input("Price : "))
                pieces = int(input("Pieces : "))
                colour = input("Colour : ")
                try:
                    cursor.execute(SQL_Q.IAC.format(pid, company, model, desc, price, pieces, colour))
                    db.commit()
                except:
                    db.rollback()
                    print("Error in inserting row(s) into table")
                    break
            else:
                print(b , "row(s) inserted successfully into table AC")
        else:
            print("Wrong Option....... Exiting")
    elif opt == 2:
        print("Insert one row : ")
        print("Insert multiple rows : ")
        a = int(input("Select an option : "))
        if a == 1:
            cls.clr()
            pid = input("Product_ID : ")
            company = input(("Company : "))
            model = input("Model : ")
            desc = input("Description : ")
            price = float(input("Price : "))
            pieces = int(input("Pieces : "))
            colour = input("Colour : ")
            try:
                cursor.execute(SQL_Q.IFR.format(pid, company, model, desc, price, pieces, colour))
                db.commit()
                print("1 row inserted successfuly into table FRIDGES")
            except:
                db.rollback()
                print("Error in inserting row(s) to table")

        elif a == 2:
            b = int(input("Enter the number of rows to be inserted into table FRIDGES : "))
            cls.clr()
            for i in range(0 , b):
                pid = input("Product_ID : ")
                company = input(("Company : "))
                model = input("Model : ")
                desc = input("Description : ")
                price = float(input("Price : "))
                pieces = int(input("Pieces : "))
                colour = input("Colour : ")
                try:
                    cursor.execute(SQL_Q.IFR.format(pid, company, model, desc, price, pieces, colour))
                    db.commit()
                except:
                    db.rollback()
                    print("Error in inserting row(s) to table")
                    break
            else:
                print(b , 'row(s) inserted successfully into table FRIDGES')
        else:
            print("Wrong Option....... Exiting")
    elif opt == 3:
        print("1. Insert one row : ")
        print("2. Insert multiple rows : ")
        a = int(input("Select an option : "))
        if a == 1:
            cls.clr()
            pid = input("Product_ID : ")
            company = input(("Company : "))
            type = input("Type : ")
            name = input("Name : ")
            price = float(input("Price : "))
            pieces = int(input("Pieces : "))
            try:
                cursor.execute(SQL_Q.IKA.format(pid , type , company , name , price , pieces))
                db.commit()
                print("1 row inserted successfuly into table K_APPS")
            except:
                db.rollback()
                print("Error in inserting row(s) to table")
        elif a == 2:
            b = int(input("Enter the number of rows to be inserted into table K_APPS : "))
            cls.clr()
            for i in range(0 , b):
                pid = input("Product_ID : ")
                company = input(("Company : "))
                type = input("Type : ")
                name = input("Name : ")
                price = float(input("Price : "))
                pieces = int(input("Pieces : "))
                try:
                    cursor.execute(SQL_Q.IKA.format(pid, type, company, name, price, pieces))
                    db.commit()
                except:
                    db.rollback()
                    print("Error in inserting row(s) to table")
                    break
            else:
                print(b , "row(s) inserted into table K_APPS")
        else:
            print("Wrong Option........ Exiting")
    elif opt == 4:
        print("1. Insert one row : ")
        print("2. Insert multiple rows : ")
        a = int(input("Select an option : "))
        if a == 1:
            cls.clr()
            pid = input("Product_ID : ")
            company = input(("Company : "))
            name = input("Name : ")
            desc = input("Description : ")
            price = float(input("Price : "))
            pieces = int(input("Pieces : "))
            size = int(input("Size : "))
            try:
                cursor.execute(SQL_Q.ITV.format(pid , company , name , size , price , pieces , desc))
                db.commit()
                print("1 row inserted successfuly into table TV")
            except:
                db.rollback()
                print("Error in inserting row(s) to table")
        elif a == 2:
            b = int(input("Enter the number of rows to be inserted into table TV : "))
            cls.clr()
            for i in range(0 , b):
                pid = input("Product_ID : ")
                company = input(("Company : "))
                name = input("Name : ")
                desc = input("Description : ")
                price = float(input("Price : "))
                pieces = int(input("Pieces : "))
                size = int(input("Size : "))
                try:
                    cursor.execute(SQL_Q.ITV.format(pid, company, name, size, price, pieces, desc))
                    db.commit()
                except:
                    db.rollback()
                    print("Error in inserting row(s) to table")
                    break
            else:
                print(b , "row(s) inserted successfully into table TV")
        else:
            print("Wrong Option....... Exiting")
    elif opt == 5:
        print("1. Insert one row : ")
        print("2. Insert multiple rows : ")
        a = int(input("Select an option : "))
        if a == 1:
            cls.clr()
            pid = input("Product_ID : ")
            company = input(("Company : "))
            model = input("Model : ")
            desc = input("Description : ")
            price = float(input("Price : "))
            pieces = int(input("Pieces : "))
            colour = input("Colour : ")
            type = input("Type : ")
            try:
                cursor.execute(SQL_Q.IWS.format(pid , company , model , desc , price , type , pieces , colour))
                db.commit()
                print("1 row inserted successfuly into table WSH_MCH")
            except:
                db.rollback()
                print("Error in inserting row(s) to table")
        elif a == 2:
            b = int(input("Enter the number of rows to be inserted into table WSH_MCH : "))
            cls.clr()
            for i in range(0 , b):
                pid = input("Product_ID : ")
                company = input(("Company : "))
                model = input("Model : ")
                desc = input("Description : ")
                price = float(input("Price : "))
                pieces = int(input("Pieces : "))
                colour = input("Colour : ")
                type = input("Type : ")
                try:
                    cursor.execute(SQL_Q.IWS.format(pid, company, model, desc, price, type, pieces, colour))
                    db.commit()
                except:
                    db.rollback()
                    print("Error in inserting row(s) to table")
                    break
            else:
                print(b , "rows inserted successfully into table WSH_MCH")
        else:
            print("Wrong Option....... Exiting")
    else:
        print("Wrong Option......... Exiting")
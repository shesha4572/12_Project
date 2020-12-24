import cls , SQL_Q , tabulate
def Invoice(db , cursor):
    lst_pid = []
    lst_qty = []
    final_items = []
    tot_price = 0
    check = True
    n = int(input("Enter the number of products to be added to invoice : "))
    cls.clr()
    for i in range(0 , n):
        pid = input("Enter the Product ID of the item: ")
        qty = int(input("Enter the number of items sold : "))
        lst_pid.append(pid)
        lst_qty.append(qty)
        cls.clr()
    for i in lst_pid:
        if i[0] == "A":
            try:
                cursor.execute(SQL_Q.PAC.format(i))
                result = list(cursor.fetchone())
                result.insert(3, lst_qty[lst_pid.index(i)])
                final_items.append(result)
                tot_price += float(result[2]) * lst_qty[lst_pid.index(i)]
                cursor.execute(SQL_Q.UAC.format(lst_qty[lst_pid.index(i)], i))
                db.commit()
            except:
                print("Entered Product ID", i , "is not available in database")
                check = False
        elif i[0] == "F":
            try:
                cursor.execute(SQL_Q.PFR.format(i))
                result = list(cursor.fetchone())
                result.insert(3, lst_qty[lst_pid.index(i)])
                final_items.append(result)
                tot_price += float(result[2]) * lst_qty[lst_pid.index(i)]
                cursor.execute(SQL_Q.UFR.format(lst_qty[lst_pid.index(i)], i))
            except:
                print("Entered Product ID", i , "is not available in database")
                check = False
        elif i[0] == "K":
            try:
                cursor.execute(SQL_Q.PKA.format(i))
                result = list(cursor.fetchone())
                result.append("N/A")
                result.insert(3, lst_qty[lst_pid.index(i)])
                final_items.append(result)
                tot_price += float(result[2]) * lst_qty[lst_pid.index(i)]
                cursor.execute(SQL_Q.UKA.format(lst_qty[lst_pid.index(i)], i))
            except:
                print("Entered Product ID", i[0] , "is not available in database")
                check = False
        elif i[0] == "T":
            try:
                cursor.execute(SQL_Q.PTV.format(i))
                result = list(cursor.fetchone())
                result.append("N/A")
                result.insert(3, lst_qty[lst_pid.index(i)])
                final_items.append(result)
                tot_price += float(result[2]) * lst_qty[lst_pid.index(i)]
                cursor.execute(SQL_Q.UTV.format(lst_qty[lst_pid.index(i)], i))
            except:
                print("Entered Product ID", i , "is not available in database")
                check = False
        elif i[0] == "W":
            try:
                cursor.execute(SQL_Q.PWS.format(i))
                result = list(cursor.fetchone())
                result.insert(3, lst_qty[lst_pid.index(i)])
                final_items.append(result)
                tot_price += float(result[2]) * lst_qty[lst_pid.index(i)]
                cursor.execute(SQL_Q.UWS.format(lst_qty[lst_pid.index(i)], i))
            except:
                print("Entered Product ID", i , "is not available in database")
                check = False
        else:
            print("Entered Product ID", i , "is not available in database")
            check = False
    while check:
        cls.clr()
        f = open("invoice.txt" , "w")
        f.write("Invoice:")
        f.write("\n")
        final_items.insert(0 , ["Company" , "Model" , "Price" , "Quantity" , "Colour"])
        f.writelines(tabulate.tabulate(final_items , headers = "firstrow" , tablefmt = "pretty"))
        f.write("\n")
        price_t = [["Total Price", tot_price]]
        f.writelines(tabulate.tabulate(price_t , tablefmt = "pretty"))
        check = False
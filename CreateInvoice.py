import cls
def Invoice(cursor):
    lst_pid = []
    lst_qty = []
    n = int(input("Enter the number of products to be added to invoice : "))
    cls.clr()
    for i in range(0 , n):
        pid = input("Enter the Product ID of the item: ")
        qty = int(input("Enter the number of items sold : "))
        lst_pid.append(pid)
        lst_qty.append(qty)
        cls.clr()
    
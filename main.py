import ConnectDB , Insert , CheckInv , CreateInvoice
db , cursor = ConnectDB.connect()
cursor.execute("USE Project;")
CheckInv.CheckInv(cursor)
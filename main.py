import ConnectDB , Insert , CheckInv , CreateInvoice
db , cursor = ConnectDB.connect()
cursor.execute("USE Project;")
Insert.Insert(db , cursor)
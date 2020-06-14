import ConnectDB , Insert , CheckInv , CreateInvoice
db , cursor = ConnectDB.connect()
cursor.execute("USE Project;")
CreateInvoice.Invoice(cursor)
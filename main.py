import ConnectDB , Insert , CheckInv
db , cursor = ConnectDB.connect()
cursor.execute("USE Project;")
CheckInv.CheckInv(db , cursor)
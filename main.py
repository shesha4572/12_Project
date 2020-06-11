import ConnectDB , Insert
db , cursor = ConnectDB.connect()
cursor.execute("USE Project;")
Insert.Insert(db , cursor)
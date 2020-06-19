import mysql.connector
def connect(user , passwd):
    try:
        db = mysql.connector.connect(host = "localhost" , user = user , passwd = passwd)
        cursor = db.cursor()
        return db , cursor
    except:
        return 0 , 0
def disconnect(db):
    db.close()
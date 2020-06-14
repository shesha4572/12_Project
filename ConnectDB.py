import mysql.connector
def connect():
    db = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "iiaass123")
    cursor = db.cursor()
    return db , cursor
def disconnect(db):
    db.close()
import pymysql

class db_connect():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    db_connection = pymysql.connect(
        user    = 'root',
            passwd  = '1234',
            host    = '127.0.0.1',
            db      = 'test01',
            charset = 'utf8'
    )

    db = db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT *
            FROM questions
        """)
    result = cursor.fetchall()

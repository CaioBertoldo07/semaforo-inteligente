import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='230903',
            database='semaforointeligente'
        )
        self.cursor = self.conn.cursor(dictionary=True)
    
    def execute(self, sql, params=None):
        """ Para INSERT, UPDATE, DELETE """
        self.cursor.execute(sql, params or ())
        self.conn.commit()
        return self.cursor
    
    def query(self, sql, params=None):
        """ Para SELECT """
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
    def close(self):
        self.cursor.close()
        self.conn.close()

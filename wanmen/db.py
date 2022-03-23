import re
import sqlite3

from attr import has

class WanmenDb:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect('./wanmen.db')
        print ("数据库打开成功")
        self.createTable()

    def truncate(self):
        c = self.conn.cursor()
        c.execute("DELETE FROM wanmen;")
        self.conn.commit()
        print ("数据表清空成功")

    def select(self, name):
        c = self.conn
        cursor = c.execute("SELECT id,download from wanmen WHERE name = '" + name + "'")
        return cursor

    def hasFlag(self, name):
        hasFlag = False
        res = self.select(name)
        for row in res:
            hasFlag = True
        return hasFlag

    def insert(self,name,download):
        c = self.conn.cursor()
        c.execute("INSERT INTO wanmen (NAME,download) \
        VALUES ('"+name+"', "+ str(download) +")")
        self.conn.commit()
        print("已标记")

    def createTable(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS wanmen(
                ID integer PRIMARY KEY autoincrement,
                name           TEXT    NOT NULL,
                download            INT     NOT NULL
            )
        ''')
        print ("数据表创建成功")
        self.conn.commit()

    def __del__( self ):
        self.conn.close()

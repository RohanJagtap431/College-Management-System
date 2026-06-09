import mysql.connector as connector

class DBhelper:
    def __init__(self):
        try:
            self.con = connector.connect(host = 'localhost',
                                     port = '3306',
                                     user = 'root',
                                     password = 'YOUR_PASSWORD',
                                     database = 'collage_management')

            self.cur = self.con.cursor()
            print("Database Connected Successfully")
        except Exception as e:
            print(e)
            

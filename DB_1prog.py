import mysql.connector as connector

class DBhelper:
    def __init__(self):
        self.con = connector.connect(host="localhost", user="root", password="", database="dbtest")
        
    def insert_user(self, userid, userName, phone):
        query = "insert into info(userId, userName, phone)values({},'{}','{}')".format(userid,userName,phone)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data saved.")
        print()
    
    def fetch_all(self):
        query = "select * from info"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("userId: ",row[0])
            print("userName: ",row[1])
            print("phone: ",row[2])
        print("created")
        print()
    
    def delete(self,userId):
        query = "delete from info where userId = {}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted details.")
        print()

    def update(self, userId, newName, newphone):
        query = "update info set userName='{}', phone='{}' where userId={}".format(newName,newphone,userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated details.")
        print()

helper = DBhelper()
#helper.insert_user(10,"Ashish","425678910")
#helper.insert_user(20,"Danish","4256789101")
#helper.insert_user(30,"Aniket","4256781101")
#helper.insert_user(40,"Vinit","8996781101")
#helper.insert_user(25,"Sahil","8996781561")
#helper.fetch_all()
#helper.delete(25)
#helper.update(30,"Anny","087654321")
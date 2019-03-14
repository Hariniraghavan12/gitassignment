import sqlite3
class dbupdate:
    def dbupdation(self):
        db = sqlite3.connect("C:\Users\h.a.vijayaraghavan\csvdataidle.db")
        cursor = db.cursor()
        q="update Employee_Project set flag='Y' where Rolloff_date like '%/%/2099';"
        cursor.execute(q)
        db.commit()
        db.close()


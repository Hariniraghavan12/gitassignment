import sqlite3
from sqlite3 import OperationalError
class Creation:
    def dbCreation(self):
        conn = sqlite3.connect('C:\Users\h.a.vijayaraghavan\csvdataidle.db')
        c = conn.cursor()

        # Open and read the file as a single buffer
        fd = open('CreateQueries.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        # all SQL commands (split on ';')
        sqlCommands = sqlFile.split(';')

        # Execute every command from the input file
        for command in sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                c.execute(command)
            except OperationalError, msg:
                print "Command skipped: ", msg


        conn.commit()
        conn.close()

#obj1=Creation()
#obj1.dbCreation()

import TableCreation as t
import InsertQueries as i
import UpdateQuery as u
if __name__ == '__main__':
    objc=t.Creation()
    objc.dbCreation()
    obji=i.Insertion()
    obji.insertQuery()
    obju = u.dbupdate()
    obju.dbupdation()
# Example 1-13. PP4E\Preview\update_db_shelve.py

from initdata import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue'] # fetch sue
sue['pay'] *= 5
db['sue'] = tom # update sue
db['tom'] = sue # add a new record
db.close()

'cheking db'
db=shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])
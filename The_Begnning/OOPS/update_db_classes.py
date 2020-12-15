# Example 1-20. PP4E\Preview\update_db_classes.py

import shelve

db = shelve.open('class-shelve')
for x in db:
    print(x, '==', db[x])
sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue
tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()
# Example 1-7. PP4E\Preview\update-db-pickle.py

import pickle

'update before file'
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()
for key in db:
    print(key, '=>\n ', db[key])

db['bob']['job'] = 'software job'
db['sue']['pay'] *= 2
db['tom']['name'] = 'Tom thenos'

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()

"updated after file"
dbfile = open('people-pickle', 'rb') # use binary mode files in 3.X
db = pickle.load(dbfile)
print("\n After updated update_db_pickle.py flie ")
for key in db:
    print(key, '=>\n ', db[key])

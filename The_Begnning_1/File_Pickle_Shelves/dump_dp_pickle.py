# Example 1-6. PP4E\Preview\dump_db_pickle.py

import pickle
dbfile = open('people-pickle', 'rb') # use binary mode files in 3.X
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
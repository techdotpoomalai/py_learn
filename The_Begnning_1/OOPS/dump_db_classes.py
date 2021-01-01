# Example 1-19. PP4E\Preview\dump_db_classes.py

import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>', db[key].name, db[key].pay, db[key].job)
bob = db['bob']
sue=db['sue']
print(bob.lastName())
print(db['tom'].lastName())
print(db['sue'].lastName(),'\t', sue.lastName()[0:-1])
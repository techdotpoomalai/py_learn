# Example 1-11. PP4E\Preview\make_db_shelve.py
from initdata import bob, sue, tom

import shelve
db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] =tom
db.close()
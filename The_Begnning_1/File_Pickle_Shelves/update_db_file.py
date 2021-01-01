
# Example 1-4. PP4E\Preview\update_db_file.py
from make_db_file import loadDbase, storeDbase
db = loadDbase()
db['sue']['pay'] *= 2
db['tom']['name'] = 'Tom Thonos'
db['bob']['job'] = 'software job'
storeDbase(db)
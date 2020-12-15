# Example 1-8. PP4E\Preview\make_db_pickle_recs.py

from initdata import bob, sue, tom
import pickle

for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()

"This is bob file data cheaking"
bobfile=open('bob.pkl', 'rb')
bob=pickle.load(bobfile)
bobfile.close()
print(bob)
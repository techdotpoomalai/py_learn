# Example 1-10. PP4E\Preview\update_db_pickle_recs.py

import pickle
suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()
print("before update\n",sue)

sue['pay'] *= 3
sue['job']='Engineer'
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()

'sue file data cheaking after update'

suefile=open('sue.pkl','rb')
sue=pickle.load(suefile)
suefile.close()
print("After update\n",sue)
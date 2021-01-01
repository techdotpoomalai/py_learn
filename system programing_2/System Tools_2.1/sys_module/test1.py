from more import more
import sys

# more(sys.__doc__,5)
# print(sys.platform,'\n', sys.maxsize,'\n', sys.version)
# if sys.platform[:3] == 'win': print('hello windows')

import traceback, sys
def grail(x):
    print('\n\n')
    raise TypeError('already got one')

try:
    # graill('arthur')
    grail('arthur')


except:
    print('\n')
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])
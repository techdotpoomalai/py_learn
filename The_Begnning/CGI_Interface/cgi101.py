#!/usr/bin/python
#C:/Users/user/AppData/Local/Programs/Python/Python38-32/python.exe

import cgi as h

form = h.FieldStorage()    # parse form data
print('Content-type: text/html\n')  # hdr plus blank line
print('<title>Reply Page</title>')      # html reply page
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    # Example 1-31. PP4E\Preview\cgi-bin\cgi101.py
    print('<h1>Hello <i>%s</i>!</h1>' % h.escape(form['user'].value))
import os

# print(os.path.split(r'D:/PYTHON/py_learn\System Tools/os_module/basic_interface.txt'))
# print(os.path.join(r'D:\PYTHON/py_learn\System Tools\os_module', 'basic_interface.txt'))
# path_name=r'D:\PYTHON\py_learn\System Tools\os_module\basic_interface.txt'
# print(os.path.dirname(path_name))
# print('\n')
# print(os.path.basename(path_name))

# print(os.path.splitext(r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw'))
# print(os.path.join(*path_name.split(os.sep)))
# print(os.path(path_name))


# mixed=r'C:\\temp\\public/files/index.html'
# print(os.path.normpath(mixed))
# print(os.path.normpath(r'C:\temp\\sub\.\file.ext'))
# print(os.chdir(r'C:\Users')
# print(os.getcwd())



# DOS cell comments
# print(os.system('dir /B'))
# os.system('type test.py')
# print('The Meaning of Life')

# open('basic_interface.txt').read()
# "# a Python program\nprint('The Meaning of Life')\n"
# text=os.popen('type basic_interface.txt').read()
# # print(text)
# listing = os.popen('dir /B').readlines()
# print(listing)

import subprocess
# subprocess.call('python print.py')
# subprocess.call('cmd /C "type print.py"')
# subprocess.call('type print.py', shell=True)
# subprocess.call('cmd /C "type print.py"')
# pipe = subprocess.Popen('python print.py', stdout=subprocess.PIPE)
# print(pipe)
# print(pipe.communicate())
# print(pipe.returncode)
# print(pipe.stdout.read())
# print(pipe.wait())
# from subprocess import PIPE, Popen
# c=Popen('python print.py', stdout=PIPE).communicate()[0]
# print(c)
# import os
# print(os.popen('python print.py').read())
# print(os.system("python print.py arg arg &"))
# print(os.system("start print.py arg arg"))


os.startfile("D:/Fron Endpoomalai_res_boot.htm") # open file in your web browser
os.startfile("C:/Users/user/Desktop/Document/d.docx") # open file in Microsoft Word
os.startfile("D:/PYTHON/py_learn/System Tools/os_module/print.py") # run file with Python

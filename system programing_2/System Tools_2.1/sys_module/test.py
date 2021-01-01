# line = 'aaa\nbbb\nccc\n'
# print(line.splitlines())
# mystr = 'xxxSPAMxxx'
# print(mystr.find('AM'))
# mystr = 'SHRUBBERY'
# print(mystr.isalpha(),mystr.isdigit(),mystr.split(','))
# print(' '.join(['A', 'dead', 'parrot']))

from os import system

system('cls')

file = open('spam.txt', 'w')
# file.write('Hi\n')
file.write("spam \n" *5)
file.close()

file=open('spam.txt')
t=file.read()
print(t)
#!/usr/bin/python3
f= open('myfile2.txt', 'w')
print('This is the first line.', file=f)
print('Second line same as the first.', file=f)
print('This is the last line', file=f)
f.close

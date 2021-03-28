#!/usr/bin/python3
f= open('myfile.txt', 'r')
data = f.read()
print(data)
leng = len(data)
print(leng)
f.close()

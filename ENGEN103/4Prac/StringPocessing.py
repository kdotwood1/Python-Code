#!/usr/bin/python3
name = "Cpt James Kirk"
print (name[0])
print (name[4:9])
print (name[10:])
if "X" in name:
	print(name, "has an X")
for ch in name:
	if ch != ' ':
		print (ch, end="")
print("\n")

name = name[:9] + 't' + ' ' + name[10:]
print(name)
name [10] = 'T'
print(name)

#str object does not support item assignment

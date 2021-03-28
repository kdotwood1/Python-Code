#!/usr/bin/python3
Today = [ 12212, 17617, 16968, 13375, 11378, 17617, 12062, 19891, 11274, 10582, 16213, 19891, 11274,12062, 19891]
People  =  { 16968:"Out",  13375:"Out",  11378:"In",  11777:"In", 16320:"Out",  15091:"Out",  11274:"Out",  10582:"In", 15335:"In",   12212:"Out",   17617:"In",   12062:"Out", 19891:"In" }

#2
for i in range(len(Today)):
	print(Today[i])

#3
print('Enter a cardax number to see if they have entered/exited today')
checker = int(input())
if checker in Today:
	print(checker, 'has used the door today')
else:	
	print(checker, 'has not used the door today')

#4
print(People)

#5
print(len(People))

#6
if checker in People.keys():
	print(checker, 'is a valid card number')
#7
	print('The person is', People[checker])
else:
	print(checker, 'is unknown')

#8
if People[checker] == 'In':
	People[checker] = 'Out'
	print(checker, 'is now Out')
else:
	People[checker] = 'In'
	print(checker, 'is now In')
print(People)

#9
for i in range(len(Today)):
	chan = Today[i]
	if int(chan) in People.keys():
		if People[chan] == 'In':
			People[chan] = 'Out'
		else:
			People[chan] = 'In'
print(People)


#10
Inside = []
insi = ''
for inpeep in People:
	if People[inpeep] == 'In':
		Inside.append(inpeep)
		insi += str(inpeep) + '\n'
print(Inside)

#11
f = open('inside.txt','w')
f.write(insi)
f.close()

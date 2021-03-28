#!/usr/bin/python3
#Ask user to pick between paper, scissors or rock
#Computer generates its choice randomly
#decides who has won
#paper > rock > scissors > paper, let this be represented numerically (1,2,3,1)
#if same choice display "Draw"
#if comp =3 person =2 display "I win"
#if comp =2 person =1 display "I win"
#if comp =1 person =2 display "You win"
#if comp =2 person =3 display "You win"
#else whoever has 0 wins

print('Please type the number associated')
print('Paper (0), Scissors (1), Rock (2)?')
user = int(input())

from random import randint
comp = randint(0, 2)
print(comp)

if comp == user:
	print('Draw')
elif comp==0 and user==2:
	print('I win')
elif comp==2 and user==0:
	print('You win')
elif comp > user:
	print('I win')
else:
	print('You win')

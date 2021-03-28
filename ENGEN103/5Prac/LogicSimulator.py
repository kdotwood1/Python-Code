#!/usr/bin/python3
#a Pseudocode
#Ask user if powerInput1 is ON or OFF and store result1
#Ask user if powerInput2 is ON or OFF and store result2
#Ask user if the gate to the output is an AND or OR and store gateType
#Determine if power is ON or OFF
#Display finalResult to user

print('Please type one of the two options in capital letters')
print('Is the power input 1 ON or OFF?')
result1 = input()
print('Is the power input 2 ON or OFF?')
result2 = input()
print('Is the circuit in parallel (OR) or series (AND) ?')
gateType = input()

powerResult = result1 + gateType + result2 
if result1 == result2:
	print('The power is ', result1)
elif result1 != result2 and gateType == 'AND': 
	print('The power is OFF')
else:
	print('The power is ON')

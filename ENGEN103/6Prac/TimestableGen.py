#!/usr/bin/python3
print("This is a times table generator")
print("Please enter a minimum value between 1 & 9")
mini = int(input())
print("And a maximum between 1 & 9")
maxi = int(input())
if (maxi >= mini):
	for x in range(mini, (maxi + 1)):
		print(x, "Times Table")
		for y in range(1, 10):
			print(x, "x", y, "=", x*y)
		print(" ")
	print(" ")
else:
	print("The minimum must be smaller than te maximum")

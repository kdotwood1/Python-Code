#!/usr/bin/python3
colours = [ "white" , "red" , "blue" , "green" , "black" ]
print (colours)
for colour in colours:
	print ("we have", colour)

print ("The second colour is: " , colours[1])
print ("the fifth element of the list is: ", colours[4]) 

#print(colours [5])

print ("Elements indexed 1 to 3: ", colours[1:4])
print ("Elements indexed 3 to the end: ", colours[3:])
print ("The last element: ", colours[-1])
print ("The last three elements:", colours[-3])
print ("The third to last and second to last elements:", colours[-3:-1])
colours[4] = 2.2
colours.append("The End")
print (colours[5])
print (colours)
if "orange" in colours:
	print("orange is in", colours)
else:
	print("orange is not in", colours)

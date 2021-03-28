#!/usr/bin/pyhton3
#imports math class
import math
#Declares constants; chlorine/m3 H2O, chlorinekg/bag, cost/bag
#Q part a
CHLORINE_RATE = 0.1
BAG_WEIGHT = 2
BAG_COST = 5.5

#asks user for input of pool dimensions
#q part b
try:
	print("Length of Pool")
	leng = input()
	print("Width of Pool")
	wid = input()
	print("Depth of Pool")
	dep = input()
except:
	print("Numbers only please")
#volume of water calc
vol = float(leng) * float(wid) * float(dep)
print ("Volume of Water:", vol, end="m3\n")
#chlorine req. in kgs
wei = vol * CHLORINE_RATE
print ("Amount of Chlorine:", wei, end="kgs\n")
#bags req, rounded up
bags = wei / BAG_WEIGHT
bags = math.ceil (bags)
print (bags, " bags required\n")
#cost of chlorine
cost = bags * BAG_COST
print ("Cost: $", cost)


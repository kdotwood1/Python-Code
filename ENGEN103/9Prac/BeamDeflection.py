#!/usr/bin/python3
#Pseudocode ---------------------------------------------------------
"""
Call Menu returning option
while option is not 2
   If option is 1 then
      Get input from user about variables needed
      For x val changing    
          Calc Beam deflection
   Else
      Display error message
   Endif
   Call Menu returning option
Endwhile
"""

#Functions ----------------------------------------------------------

def Menu():
    print("1) Run experiment\n2) Exit")
    while True:
        try:
            sel = int(input("Please enter your selection: "))
        except ValueError:
            print('Please enter 1 or 2 only')
        if sel == 1 or sel == 2:
            break
        else: 
            print('Please enter 1 or 2 only')
    return sel    

def CalcPart1(W, l, x):  
    part1 = W * x * (l-x)
    return part1

def CalcPart2(E, I, l):  
    part2 = 24 * E * I * l
    return part2

def CalcPart3(l, x):  
    part3 = l ** 2 + x * (l-x)
    return part3

def CalcBeamDefl(W, E, I, l, x):
    z = (CalcPart1(W, l, x) / CalcPart2(E, I, l)) * CalcPart3(l, x)
    return z

#Main Line ----------------------------------------------------------

sel = Menu()
while sel != 2:
    if sel == 1:
        W = int(input("Please enter;\nthe Load Weight: "))
        E = int(input("the Elasticity: "))
        I = int(input("the Inertia: "))
        l = int(input("the Beam Length: "))
        x = 0
        for x in range(0, l):
            y = CalcBeamDefl(W, E, I, l, x)
            print("At", x, "beam deflection equals", y)
            x = x + 5
    sel = Menu()



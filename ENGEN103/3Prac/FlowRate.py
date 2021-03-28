#!/usr/bin/python3
import math
print("Height of Cylinder ")
hei = input()
print("Radius of Cylinder ")
rad = input()
print("Water Flow Rate ")
flo = input()
tim = 120
vol = math.pi * (int(rad) * int(rad)) * int(hei)
vol = round(vol, 2)
print(vol , end="m3\n")
watvol = int(flo) * tim
print(watvol , end="m3\n")


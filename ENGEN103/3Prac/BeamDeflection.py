#!/usr/bin/python3
W = 2500
E = 30000000
I = 258
l = 300
x = 90

part1 = W * x * (l-x)
part2 = 24 * E * I * l
part3 = l ** 2 + x * (l-x)
y = (part1 / part2) * part3
print(y)



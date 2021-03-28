#!/usr/bin/python3
import math
#2
noteNames = ('A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab')

#3
freq = (220.00, 233.08, 246.94, 261.62, 277.18, 293.66, 311.12, 329.62, 349.22, 369.99, 391.99, 415.30)
print(freq)

#4
a = 2 ** (1/12)
f = 110.0
frequency = list ((round(f * (a ** i), 2) for i in range (0,12)))
print(frequency)

#5

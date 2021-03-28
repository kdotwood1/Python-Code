#!/usr/bin/python3
#1abcd
daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
lottoNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

#2
sunStart = [daysOfWeek [6], daysOfWeek[:-1]]
print (sunStart)

#3
print ('which month would like? (1-12)')
x = int(input()) - 1
monthArray = [monthNames[x], daysPerMonth[x]] 
print (monthArray) 
print ()

#4
monthDict = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
print ('Input the month you would like to search for')
monthIn = input()
print (monthDict.get(monthIn))

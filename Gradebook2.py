#!/usr/bin/env python
# coding: utf-8

grades = [100,87,93,45,38]
x = len(grades)
add = sum(grades)
mean = add/x

def addScore(x):
  grades.append(x)
for i in grades:
    if i > 100: print("Uh oh...Grade too large.")
    if i < 1: print("Uh oh...Grade too small.")

def calcStats():
    return(mean(grades), min(grades), max(grades))
print(calcStats)

def printStats():
   return("The average grade is " + mean + ". The highest grade is " + max + ". The lowest grade is " + min + "." ) 
print(printStats)

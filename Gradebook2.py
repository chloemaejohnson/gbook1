#!/usr/bin/env python
# coding: utf-8

grades = [10.0,24.5,17.9,54.8,75.8,99.0]
x = len(grades)
add = sum(grades)
mean = add/x
print("The average score of the grades is ", mean, ".")
print("The highest score is ", max(grades), ".")
print("The lowest score is ", min(grades), ".")

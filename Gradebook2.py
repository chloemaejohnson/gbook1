

grades = [100, 87, 93, 45, 38]
''' 
All this should be in the methods
x = len(grades)
add = sum(grades)
mean = add/x 
'''


def addScore(x):
    grades.append(x)


# You dont need a for loop. Just use if then append inside the if statement
''' 
for i in grades:
    if i > 100: print("Uh oh...Grade too large.")
    if i < 1: print("Uh oh...Grade too small.") 
'''

'''
This Method should calculate the mean
'''


def calcMean():
    return


'''
This methods calculates the average
'''


def calcAverage():
    return


'''
This method returns the min
'''


def calcMin():
    return


'''
This method returns the max
'''


def calcMax():
    return


'''
You dont need to have a return statement here.
Just have multiple print statements like
print("The average grade...."calcAverage)
print("The highest grade is ....")
'''


def printStats():
    return("The average grade is " + mean + ". The highest grade is " + max + ". The lowest grade is " + min + ".")


print(printStats)

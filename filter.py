import point
import math

# The are_positive function returns a list of all positive values in the input list.
# input : a list of float numbers, and a float number
# output: a list of output numbers that are positive
def are_positive(numbers):
    bList = []
    for positive_number in numbers:
     if positive_number > 0:
        bList.append(positive_number)
    return(bList)

# The are_greater_than function returns a list of all values in the input list that are greater than the n parameter.
# input : a list of float numbers, and a float number
# output: a list of output numbers that are greater than n
def are_greater_than(numbers,n):
    bList = []
    for greaterthan in numbers:
     if greaterthan > n:
        bList.append(greaterthan)
    return(bList)

# add and all take 2 numbers and returns a list with each element set to the sum of the parameter
# input : a list of float numbers, and a float number
# output: a list of output numbers
def are_in_positive_quadrant(points):
    bList = []
    for positive in points:
        if positive.x > 0 and positive.y > 0:
            bList.append(positive)
    return(bList)
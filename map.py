import point
import math
# this is a list function that computes and returns a list of the square of each value in the list
# input x: a list of float numbers
# output: a list of output numbers
def square_all(numbers):
    bList = []
    for x in numbers:
        bList.append(x**2)
    return(bList)

# add and all take 2 numbers and returns a list with each element set to the sum of the parameter
# input : a list of float numbers, and a float number
# output: a list of output numbers
def add_n_all(numbers, n:float):
    bList = []
    for x in numbers:
        bList.append(x+n)
    return(bList)

# add and all take 2 numbers and returns a list with each element set to the sum of the parameter
# input : a list of float numbers, and a float number
# output: a list of output numbers
def distance_all(points):
    bList = []
    for joe in points:
        my_output = math.sqrt(joe.x**2 + joe.y**2)
        bList.append(my_output)
    return(bList)




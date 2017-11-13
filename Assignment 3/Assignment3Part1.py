"""
Functions for use in the first part of Assignment 3.  Each of the
four mystery functions takes as its only parameter a list of numbers.
Each function changes its parameter list in some way but does not return a
result. None of them do anything useful; their only purpose is to serve as
examples of functions with different complexities.

STUDENTS MUST HAND IN A MODIFIED VERSION OF THIS MODULE AS SPECIFIED
IN THE INSTRUCTIONS FOR ASSIGNMENT 3.

This part of Assignment 3 was created by Margaret Lamb and is licensed
under Creative Commons Attribution-NonCommercial (CC BY-NC). 
"""

########################################################################
## Mystery Functions
########################################################################
def mystery1(numbers):
    # The complexity of this function is O(n^2)
    n = len(numbers)
    total = 0
    i = 0

    fundamentalSteps = 0 # my code

    while i < len(numbers):
        j = i
        while j < len(numbers):
            total += numbers[i]*numbers[j]
            j += 2
            fundamentalSteps += 1 # my code
        numbers[i] = total
        i += 3
        fundamentalSteps += 1 # my code

    return fundamentalSteps


def mystery2(numbers):
    # The complexity of this function is O(nlogn)
    n = len(numbers)
    size = n-1
    fundamentalStep = 0

    while size > 0:
        i = 0
        while i < n:
            if numbers[i] > numbers[size]:
                numbers[i] += 1
                numbers[size] += 1
            fundamentalStep += 1
            i = i + 1
        size = size // 2 # integer arithmetic, rounded down

    return fundamentalStep


def mystery3(numbers):
    # The complexity of this function is O(n^3)
    n = len(numbers)
    i = 0
    fundamentalStep = 0

    while i < n:
        total = 0
        j = i
        while j >= 0:
            for k in range(0, j):
                total += numbers[k]-numbers[j]
                fundamentalStep += 1
            numbers[j] = total
            j = j - 2
            fundamentalStep += 1
        i += 5
        fundamentalStep += 1
    return fundamentalStep

def mystery4(numbers):
    # The complexity of this function is O(logn)
    n = len(numbers)
    maxVal = numbers[0]
    index = n-1
    fundamentalStep = 0

    while index > 0:
        if numbers[index] > maxVal:
            maxVal = numbers[index]
        index = (int) (index / 1.5) # division truncated down
        fundamentalStep += 1
    numbers[0] = maxVal

    return fundamentalStep
        

########################################################################
## Helper Functions
########################################################################
import random
import timeit
import math

def randomList(length) :
    '''
    Creates a list of random numbers with the given size
    '''
    randList = []
    for i in range(length) :
        randList.append(random.randint(0, length))
    return randList


def runMysteryFunction(mysteryFunctionName, testList) :
    '''
    Calls the function with the given name and the given list as a parameter
    '''    
    globalElements = globals()

    if (mysteryFunctionName in globalElements.keys()) :
        return globalElements[mysteryFunctionName](testList)

    return None


def printTimingTable(mysteryFunctionName, startRange, endRange) :
    '''
    Prints a table with timing, step and input size values for a
    series of 10 calls to the function with the given name
    '''      
    increment = (endRange - startRange) // 9
    if (increment < 0) :
        return    

    functionCallToTime = 'Assignment3Part1.' + mysteryFunctionName + '(testList)'
    importStatement = 'import Assignment3Part1;'

    print("----- Testing Function", mysteryFunctionName, "-----")
    print(" -List Size- ", " -Time- ", \
          " -Steps- ", " -logN- ", \
          "  -N-  ", "   -NlogN-  ", "   -N^2-   ", "   -N^3-   ")
    for listSize in range(startRange, endRange + 1, increment):
        testList = randomList(listSize)
        fundamentalSteps = runMysteryFunction(mysteryFunctionName, testList)
        if (fundamentalSteps == None) :
            fundamentalSteps = 'None'
        
        callToRandomList = 'testList = Assignment3Part1.randomList(' \
                + str(listSize) + ')'        
        mysteryFunctionTime = timeit.Timer(functionCallToTime, \
            importStatement + ' ' + callToRandomList).timeit(1)
        
        print("{0:^13.3g} {1:^8.3f} {2:^9.3g} {3:^8.3g} {4:^9.3g} {5:^9.3g} {6:^13.3g} {7:^11.3g}".format(\
            listSize, mysteryFunctionTime, fundamentalSteps, round(math.log(listSize, 2)), \
            listSize, round(listSize * math.log(listSize, 2)), listSize**2, listSize**3))


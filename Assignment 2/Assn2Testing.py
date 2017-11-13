"""
A testing module for Assignment 2

This module contains some functions for testing a solution to Assignment 2.
If this module loads without error and the testAll() function reports no errors,
it does NOT guarantee that your solution is 100% correct.  What it does mean is:
    - You've got the structural details right: name of module,
      names of functions, and number and order of function parameters
    - Your functions work correctly for the test list used in
      this module
      
For marking your submissions, we may change or add to this testing code and we
will definitely use different test lists, including larger ones than the
example used here.  So we may uncover errors in your code that
this module didn't catch.  You would be wise to invent more test cases for
yourself.  As an example, for your sorting function you should try lists of
different sizes with elements in different orders (already sorted, reverse
order, almost correctly sorted, etc)

This program was created by Margaret Lamb and is licensed under
Creative Commons Attribution-NonCommercial (CC BY-NC).
"""

## NOTE: This import statement assumes that:
## - you have your code in a file named Assignment2.py
## - this test program is in the same directory
## You will need to alter this import statement accordingly if
## that is not the case.
from Assignment2 import *

def testIsSorted():
    nums1 = createList([1,3,5,5,7])
    if not isSorted(nums1):
        print("nums1 failed the isSorted test")
        return False

    nums2 = createList([1,5,3,7])
    if isSorted(nums2):
        print("nums2 failed the isSorted test")
        return False

    if not compareLists(nums2, createList([1,5,3,7])):
        print("ERROR: isSorted changed its parameter list")
        return False

    return True

def testNoDups():
    nums = createList([1,1,2,5,7,7,8,8,10,10,10,10,10])
    nums = noDups(nums)
    if not compareLists(nums, createList([1,2,5,7,8,10])):
        print("ERROR: noDups([1,1,2,5,7,7,8,8,10,10,10,10,10]",\
              "returned", listString(nums))
        return False
    else:
        return True

def testInsert():
    nums = createList([1,2,4,7])
    nums = insertInOrder(nums,4)
    if not compareLists(nums, createList([1,2,4,4,7])):
        print("ERROR: insertInOrder with [1,2,4,7] and 4 returned",\
              listString(nums))
        return False
    else:
        return True

def testSort():
    nums = createList([3,1,4,1,5,9])
    nums = sort(nums)
    if not compareLists(nums, createList([1,1,3,4,5,9])):
        print("ERROR: sort with [3,1,4,1,5,9] produced",\
              listString(nums))
        return False
    else:
        return True

def testAll():
    """
    Tests all four required functions
    """
    result = testIsSorted()
    temp = testNoDups()
    result = result and temp
    temp = testInsert()
    result = result and temp
    temp = testSort()
    result = result and temp

    if result:
        print("all the tests succeeded")
    else:
        print("more debugging needed....")
    
    

def compareLists(list1, list2):
    """
    Helper function for testing
    Parameters are linked lists of numbers.  Returns True if the two
    lists are exactly the same, False otherwise.
    """
    while list1 != None and list2 != None and list1['data'] == list2['data']:
        list1 = list1['next']
        list2 = list2['next']
    return list1 == None and list2 == None


def listString(linkedList):
    """
    Returns a string describing the list, suitable for printing.
    """
    result = '['
    current = linkedList
    while current != None:
        result += str(current['data'])
        current = current['next']
        if current != None:
            result += ","
    return result + ']'


def printList(linkedList):
    """
    Prints a representation of a list
    """
    print(listString(linkedList))
    

def createList(plist):
    """
    Creates and returns a linked list containing all of the elements
    of the Python-style list parameter.  A useful shortcut for testing.
    """
    result = None # empty list

    # loop through plist in reverse order and add each element to the
    # start of the result
    for index in range(len(plist)-1,-1,-1):
        result = {'data':plist[index], 'next':result}
    return result



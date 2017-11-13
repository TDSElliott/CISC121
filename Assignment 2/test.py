""""
Author: Tyler Elliott
Date: 15 Oct 17
"""

"""
ASSIGNMENT 2 SKELETON CODE
Assumes all lists contain numeric data.
This file contains skeleton versions of the required functions
for Assignment 2, as well as a few functions to help you test
your functions.

This program was created by Margaret Lamb and is licensed under
Creative Commons Attribution-NonCommercial (CC BY-NC).
"""


# Your job is to fill in the bodies of the next four methods,
# currently just "stubs"

def isSorted(nums):
    """
    Assumes nums is a linked list of numbers.
    Returns True if the values in nums are sorted in non-decreasing order,
    False otherwise.  An empty or one-element list is considered sorted.
    """
    # the first node
    current = nums
    # only run if the array isn't empty
    while current != None:
        # have to compare the previous to the next
        previous = current
        # move to the next item in the list
        current = current['next']
        # make sure you've not reached the end of the list
        if current != None:
            # see if it's less than or equal to the next value
            if previous['data'] <= current['data']:
                continue
            else:
                # it's failed the test
                return False

    return True  # it's passed the test or is an empty array


def noDups(nums):
    """
    Assumes nums is a linked list of numbers sorted in non-decreasing order.
    Modifies nums to get rid of all duplicate elements.
    Returns a pointer to the first element of the modified version
    of nums
    """
    head = nums
    temp = []

    if nums != None:
        previous = nums
        nums = nums['next']
        if nums != None:
            if nums['data'] == previous['data']:
                previous['data']
    return nums  # stub


def insertInOrder(linkedList, value):
    """
    Inserts a value into a sorted linked list.  Assumes the linkedList
    parameter is sorted in non-decreasing order.
    """
    return linkedList  # stub


def sort(nums):
    """
    Assumes nums is a list of numbers but does NOT assume nums is sorted.
    Returns a sorted copy of nums.
    """
    return None  # stub


#########################################################################################################
# The following functions are included for testing purposes, so that you can easily create and print
# linked lists.  You may not call these functions from any of your required functions.
#########################################################################################################

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
    result = None  # empty list

    # loop through plist in reverse order and add each element to the
    # start of the result
    for index in range(len(plist) - 1, -1, -1):
        result = {'data': plist[index], 'next': result}
    return result

"""
linkedList = createList([1, 2, 3, 4, 5])
print(linkedList)

ogList = linkedList
linkedList = linkedList["next"] # we are now at index 1, the second item
currNext = linkedList["next"] # this is the remainder of the list, have to hook back up
linkedList = linkedList["next"]



# temp value
value = 15
# create our node to be inserted
node = {'data':value, 'next':currNext} # currently points no where

print('node',node)

linkedList["next"] = node
print(linkedList["next"])
print(linkedList)

"""

# printList(linkedList)
# print(isSorted(linkedList))



"""

Combining nodes into a linked list

"""

node1 = {"data": 1, "next": None}
node2 = {"data": 2, "next": None}
node3 = {"data": 3, "next": None}
node4 = {"data": 4, "next": None}
node5 = {"data": 5, "next": None}

node1["next"] = node2
node2["next"] = node3
node3["next"] = node4
node4["next"] = node5

print(node1)

# now to perform the mighty insert
nodeIn = {"data": 13, "next": None}


insertPoint = node1["next"]
insertPoint = insertPoint["next"]

# link-up the second half again
nodeIn["next"] = insertPoint["next"]

insertPoint["next"] = nodeIn


print(insertPoint)
print(node1)
print()
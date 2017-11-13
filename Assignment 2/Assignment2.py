""""
Author:     Tyler Elliott
Student ID: #############
Date:       15 Oct 17
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

# WORKS
def isSorted(nums): 
    """
    Assumes nums is a linked list of numbers.  
    Returns True if the values in nums are sorted in non-decreasing order,
    False otherwise.  An empty or one-element list is considered sorted.
    """
    # the first node
    current = nums
    # run until you reach the last node which has a value of None
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

    return True # it's passed the test or is an empty array
                          

# WORKS
def noDups(nums):
    """
    Assumes nums is a linked list of numbers sorted in non-decreasing order.
    Modifies nums to get rid of all duplicate elements.
    Returns a pointer to the first element of the modified version
    of nums
    """
    # so that we don't destroy nums as we nav through the elements
    head = nums
    # initialize change, a flag which will be used to determine if previous should be advanced
    change = False
    # while there are still items in the lists
    while head != None:
        # no change has occured, no duplicate was found
        if not change:
            # copy current head to previous
            previous = head
            # advance head to the next value
            head = head['next']
            # make sure you're not comparing the end of the list, which would throw an error
        if head != None:
            # if the values are the same, we have found a duplicate
            if head['data'] == previous['data']:
                # 'jump' over the duped value, by connecting the head's 'next' value to the
                # previous 'next' value. Essentially removing the duplicate by dropping all references to it
                # I suppose Python garbage collector will handle it in memory
                # I'm sure there's a more professional way of doing this though
                previous['next'] = head['next']
                # advance head so we don't get an infinite loop
                head = head['next']
                # a change has occurred, we need to check the same previous value against the new head value
                # this affects if the above if statement runs which sets previous = head, and advances head
                change = True
            else:
                # no change has occurred, tells if that we need to move the values along
                change = False
    # due to the nature of linked lists nums is now in proper order
    # even though we never directly called its variable name when making edits
    # we simply changed the data it refers to
    return nums

# WORKS
def insertInOrder(linkedList, value):
    """
    Inserts a value into a sorted linked list.  Assumes the linkedList
    parameter is sorted in non-decreasing order.
    """

    # the first node, the list to be used during search
    insertSearch = linkedList

    # let's make the node to be inserted
    nodeIn = {"data": value, "next": None}

    # flag to make sure it's only inserted once, if there are duplicates in the list
    inserted = False

    # run until you reach the end
    while insertSearch != None:
        # have to have the previous so you can link up the new node
        previous = insertSearch
        # move to the next item in the list
        insertSearch = insertSearch['next']

        # if the value needs to be inserted at the start
        if previous['data'] >= value:
            tempNode = {'data':value, 'next':None}
            tempNode['next'] = linkedList
            linkedList = tempNode
            return linkedList

        # if the previous value is lesser or equal
        # and the next value is greater or equal we have found our insert location
        if insertSearch != None:
            if previous['data'] <= value and insertSearch['data'] >= value:
                # first assign the inserted node's next value
                nodeIn['next'] = insertSearch
                previous['next'] = nodeIn
                return linkedList
        else:
            # you've reached the end
            previous['next'] = nodeIn
            return linkedList
    # you've passed in an empty list, no need to preserve data
    # just set it equal to the one node you want to insert and away we go
    linkedList = nodeIn


    return linkedList


# WORKS
def sort(nums):
    """
    Assumes nums is a list of numbers but does NOT assume nums is sorted.
    Returns a sorted copy of nums.
    """
    # make yourself a new head to start the sorted array with
    sortedList = {'data':nums['data'], 'next': None}
    # used to hold a reference to the previous value as we move along
    previous = sortedList
    # this is the list that maintains its structure so we can return it
    ogHead = sortedList

    # a test to see if we are at the first value in the linked list
    initValue = nums['data']

    # run until the end
    while nums is not None:
        # advance nums
        nums = nums['next']
        # sortedlist gets destroyed as we constantly advance through it
        # when you break out of the below loops it is important to reset sortedList to
        # the overarching sorted list referenced by ogHead
        sortedList = ogHead

        # make sure we don't do an illegal comparison
        if nums is not None:
            # run until the end
            while sortedList is not None:
                # generate a temporary node to be slotted in properly
                tempNode = {'data':nums['data'], 'next': None}

                if sortedList['data'] > nums['data']:
                    # we have found a value that is greater than the value we want to insert
                    # we don't know if it's the first value in the list or later
                    if sortedList['data'] == initValue:
                        # if this runs we are at the first value
                        # simply attach the rest of the list
                        tempNode['next'] = sortedList
                        sortedList = tempNode
                        # because we've edited the head we have to point our 'safe' list to the new start
                        ogHead = sortedList
                        # update the initial value so we can continue comparing to the actual head of the list
                        # (not the initial head of the list)
                        initValue = sortedList['data']
                        break
                    else:
                        # it's not the first element
                        # we need to hook up the first half of the list and the second half to the new node
                        tempNode['next'] = sortedList
                        previous['next'] = tempNode
                        break
                elif sortedList['next'] is None:
                    # if this runs we've checked the final node with a value
                    # we simply have to set the tail end of the linked list equal to the value we're inserting
                    sortedList['next'] = tempNode
                    break
                else:
                    # move the values along so that we can continue checking
                    # this will happen if the value is not larger than the value we're trying to insert
                    # and if we haven't reached the end of the list where we would just attach the inserted value
                    previous = sortedList
                    sortedList = sortedList['next']


    return ogHead  # return the variable tha references the proper head of the


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
    result = None # empty list

    # loop through plist in reverse order and add each element to the
    # start of the result
    for index in range(len(plist)-1,-1,-1):
        result = {'data':plist[index], 'next':result}
    return result
        
linkedList = createList([1,2,3,5,6])
printList(linkedList)
print(isSorted(linkedList))
linkedList = createList([1, 1, 2, 2, 3, 3, 3, 4, 5])
printList(linkedList)
printList(noDups(linkedList))
linkedList = createList([1, 2, 3, 5, 6, 7])
linkedList = insertInOrder(linkedList, -5)
linkedList = insertInOrder(linkedList, 8)
linkedList = insertInOrder(linkedList, 4)
printList(linkedList)
linkedList = createList([94, 52, 33, 28, 6, 93, 97, 65, 30, 55, 48, 70, 45, 96, 23, 95, 19, 54, 57, 15])
printList(sort(linkedList))

import random


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
    result = None  # empty list

    # loop through plist in reverse order and add each element to the
    # start of the result
    for index in range(len(plist) - 1, -1, -1):
        result = {'data': plist[index], 'next': result}
    return result


def genRando(length):
    y = []
    for x in range(length):
        y.append(random.randrange(100))
    return y

# linkedList = createList([1, 2, 2, 2, 3, 7, 6])
# linkedList = createList([7, 6, 5, 3, 4, 2, 1])

linkedList = createList([3, 4, 1, 6, 2, 8, 5])
linkedList = createList([1, 1, 1, 2, 1, 1, 1, 2])
linkedList = createList([7, 6, 5, 3, 4, 2, 1])

x = genRando(20)
print(x)
print(len(x))
print(printList(sort(createList(x))))

print('Input list:')
printList(linkedList)

print('Comp sorted:')
printList(sort(linkedList))
# print('Should be:',[1, 2, 3, 4, 5, 6, 8])
print('List alive?')
printList(linkedList)
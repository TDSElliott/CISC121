def reverse(linkedList):
    """
    Returns a linkedList in reverse order
    """
    # the linked list is empty, so return None
    if linkedList is None:
        return None

    # this is our base case, the next value is None (we're at the end)
    # return the linkedList (1 element, if the next is None)
    if linkedList['next'] is None:
        return linkedList

    # seperate the list into 2 parts,
    # everything after the head is saved linked by restOfList
    restofList = linkedList['next']

    # now set the next value equal to None, because we are moving the head
    # to the end of the list, thus it needs to be reset to None
    linkedList['next'] = None

    # now for the recursive call
    # pass back through the remainder of the list (everything sans the current head)
    # this will get smaller and smaller until you've moved through the list
    # and you have a 1 element list which will trigger the base case
    listReversed = reverse(restofList)

    # re-attach the elements to the new head
    restofList['next'] = linkedList

    return listReversed
    

##########################################################################
#########################-Helper/Test Functions-##########################
##########################################################################
import random

def testReverse():
    """
    Creates a few test cases for reverse() and prints out result
    """
    for i in range(3, 33, 3):
        myList = randomList(i)
        LL = createList(myList)
        print("Original list: ")
        printList(LL)
        revLL = reverse(LL)
        print("Reversed list: ")
        printList(revLL)
        print('\n')

def randomList(length) :
    '''
    Creates a list of random numbers with the given size
    '''
    randList = []
    for i in range(length) :
        randList.append(random.randint(0, length))
    return randList


def insertValue(linkedList, index, value):
    """
    Adds a new element to a list.
    Parameters:
        value: the value for the new element
        index: the index for the new list element
    The new value does not replace the current element at
    position index; it is inserted before that element and
    the size of the list grows by 1.
    
    The return value is the head of the modified list.
    (That's usually the same as the lis parameter, unless
    we've added a new first element.)
    
    If the index is out of bounds, prints an error message and
    returns the list unchanged.
    """

    if index < 0:
        # no negative indexes allowed
        print("Error: illegal index to insertValue")
        return linkedList

    # inserting at the beginning
    elif index == 0:
        newNode = {'data':value, 'next':linkedList}
        # This node is now the first node.  The first node of
        # the original list comes right after it.
        return newNode

    elif linkedList == None:
        # Can't insert something into an empty list except at
        # the first position
            print("Error: illegal index to insertValue")
            return linkedList

    else:
        # insert the node into the tail of the list
        tail = linkedList['next']
        linkedList['next'] = insertValue(tail, index-1, value)
        return linkedList

    
def listString(linkedList):
    """
    Returns a string describing the list, suitable for printing.
    """
    return '[' + listStringHelper(linkedList) + ']'


def listStringHelper(linkedList):
    """
    Returns a string describing a list minus the enclosing brackets.
    """
    if linkedList == None:
        return ""
    else:
        # create strings describing the head and the tail and put
        # them together
        headString = str(linkedList['data'])
        tail = linkedList['next']
        if tail == None:
            return headString
        else:
            tailString = listStringHelper(tail)
            return headString + "," + tailString


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
    linkedList = None
    for index in range(len(plist)-1, -1, -1):
        linkedList = insertValue(linkedList,0, plist[index])
    return linkedList



testReverse()
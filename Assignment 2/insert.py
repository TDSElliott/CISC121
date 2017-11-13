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


linkedList = createList([-15, 2, 3, 5, 6])

# print(linkedList)
# printList(linkedList)

print(insertInOrder(linkedList, 1))
print(insertInOrder(linkedList, -20))
# linkedList = createList([])
# print(insertInOrder(linkedList, 1))
# print(insertInOrder(linkedList, 0))
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


linkedList = createList([1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6])
# linkedList = createList([2,2,3,5,5,5,5,7,7])
print(noDups(linkedList))
printList(noDups(linkedList))
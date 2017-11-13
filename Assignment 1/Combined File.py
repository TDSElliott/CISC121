##################################################
##            Superhero kitten                  ##
##################################################

'''

Author: Tyler Elliott
Student ID: #########
Date: 25-09-17

'''

# Request 0 for firstname, and > 0 for lastName (1 preferable)
def askForName(request):
    if request == 0:
        return input("What is your first name? ")
    else:
        return input("What is your last name? ")

# Loops through each character and adds to the total ASCII count
def calculateASCIITotal(name):
    totalVal = 0
    for a in name:
        totalVal += ord(a)
    return totalVal


def main():
    # Assign first and last names using askForName
    firstName = askForName(0)
    lastName = askForName(1)

    # Find ASCII value of both names using above method
    firstNameASCII = calculateASCIITotal(firstName)
    lastNameASCII = calculateASCIITotal(lastName)

    # Creating arrays for both first and last names
    listOfSuperheroPrefixes = ['Super', 'Ultra', 'Marvel', 'Mega', 'Laser', 'Lightning', 'Thunder', 'Power', 'Iron',
                               'Captain']
    listOfKittenPostfixes = ['Fuzz', 'Whiskers', 'Purr', 'Paw', 'Claw', 'Fang', 'Snuggle', 'Cuddle', 'Cute Overload']


    # Generate index by using modulo of the length of array
    firstIndex = firstNameASCII % len(listOfSuperheroPrefixes)
    lastIndex = lastNameASCII % len(listOfKittenPostfixes)

    # Print the new 'suphero-kitten' name out
    print(listOfSuperheroPrefixes[firstIndex], listOfKittenPostfixes[lastIndex])

##################################################
##            Space Junk                        ##
##################################################

'''

Author: Tyler Elliott
Student ID: #########
Date: 25-09-17

'''

# Read and split the file input into a 2d list of ints
def readBasicDigitalImageFile(fileName):
    # open read-only copy
    with open(fileName, "r") as file:
        result = [[int(x) for x in line.split()] for line in file]
    return result

# Check if the pixel is junk by comparing the adjacent positions in the 2d array
def isPixelSpaceJunk(data, j, k):
    # is it beautiful? no, but it works
    # makes sure we're not operating on the edge of the array where we may get an array out of bounds
    if data[j][k] == 1 and j != 0 and k != 0 and j != (len(data)-1) and k != (len(data)-1):
        # executes the comparison checks
        if (data[j-1][k] == 0 and data[j+1][k] == 0 and data[j][k-1] == 0
            and data[j][k+1] == 0 and data[j-1][k-1] == 0
            and data[j-1][k+1] == 0 and data[j+1][k-1] == 0 and data[j+1][k+1] == 0):
                # if this runs it means it IS space junk, it found no adjacent '1's
                return True
    else:
        # this happens if it's not space junk, nothing useful happens on the other end in the main function
        return False

# gets everybody and the stuff together
def main2():
    # get our 2d array to work with
    userFileName = input('Enter the filename, including .bdi : ')
    spaceData = readBasicDigitalImageFile(userFileName)

    # run through each index in the 2d array
    for j in range(len(spaceData)):
        for k in range(len(spaceData)):
            if isPixelSpaceJunk(spaceData, j, k):
                print(j, k)
            else:
                continue

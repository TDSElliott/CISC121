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

# Run everything to start us off
main()
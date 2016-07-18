"""
myList=[1,2,3,4,5,6]
print myList[2]
#set variables
i=0
j=1
# maps 0 to false and 1 maps to true
swap = 0

if(myList[i] > myList[j]):
    print("yahoo")
    temp=myList[i]
    myList[j]=temp
    swap=1
    i++1
    j++1
else:
    print("ja")
    print(len(myList))
    
if(j >len(myList) ):
    print("yes")
    swap=1

while (j < len(myList)):
    print("Something");
"""
# first the myList is in order let/'s set it up somewhat randomly.
myList=[69, 18, 12, 43, 59, 83, 7]
# Next let's print out the full list rather than just one element
print myList[:]
# Setting variables are fine just copying them in
i=0
j=1
global swap
# Rather than mapping 1 and 0 to the value of swap use true and False
swap = True
# You need an extra loop here to check the swap variable
while (swap == True):
    # Set swap to false once in the loop

    swap = False
    # Setting variables are fine just copying them in
    i=0
    j=1
    # I don't understand why you put the main loop at the bottom it should start here
    while (j < len(myList)):
        # No need to print something but we will do so with some information that is useful.
        print "Comparing " + str(i) + " to " + str(j)
        # Now we do the comparison
        if(myList[i] > myList[j]):
            # Don't really need to print anything but since you did we add some info.
            print "Moving " + str(myList[i]) + " behind " + str(myList[j])
            temp = myList[i]
            # You didn't swap the value into i so you weren't swapping the values properly.
            myList[i] = myList[j]
            myList[j] = temp
            # checking to see if swap is getting set to true
            swap = True
            print "Swap " + str(swap)
        else:
            # Again no reason to print other than the fact you did.
            print "Values are in order"
        # You previously were only incrementing i and J if myList[i] was greater than myList[j]
        # it has to update every time
        # ++ is not defined in the language so this has to change.
        i = i + 1
        j = j + 1
        print "Swap " + str(swap)
# this is the end of the program we print out info the sorted list and exit 
# The code before had an infinite loop that you did not terminate.
print "Swap " + str(swap)
print myList[:]

        
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
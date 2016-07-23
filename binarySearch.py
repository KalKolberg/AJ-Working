#import math library
import math
import sys

# declare array of numbers which is sorted  which will be our list
mylist= [10,20,40,60,100]

# Number to be searched
num = 40

# set variable starting point , ending point and middle
s_p=0
e_p=len(mylist)-1

while(s_p <= e_p):
	middle = int(math.ceil((e_p +s_p)/2))
    print "start =" + str(mylist[s_p]) + "  middle =" + str(mylist[middle])+ "  end =" + str(mylist[e_p])
    if(num == mylist[middle]):
        print("number found");
        sys.exit()
    if(num > mylist[middle]):
        s_p= middle +1;
    if(num < mylist[middle]):
        e_p= middle -1;    
    print("searching for number")
		
    
if(s_p > e_p):
    print("number not found");
    sys.exit()
    
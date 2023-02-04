import sys

def popAll(alist):
    print(alist)
    alist.clear()
    print(alist)

def insertEle(alist):
    for i in range(int(input("No of terms : ",end=""))):
        alist.append(int(input()))

def linearSer(alist):
    print("")

def binarySer(alist):
    print("")

while(1):
    print("\tMenu\n1 Pop All\n2 Insert\n3 Linear Search\n4 Binary Search\n5 Any key to EXIT\n Please enter you choice : ",end="")
    alist=[12,23,45,778,33,45,2,8,96,85,38]
    choice=int(input())
    if(choice==1):
        popAll(alist)
    elif(choice==2):
        insertEle(alist)
    elif(choice==3):
        linearSer(alist)
    elif(choice==4):
        binarySer(alist)
    else:
        sys.exit()
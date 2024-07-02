import numpy as np 

MAX = 5 
top = -1 

STACK = np.ndarray(shape=(MAX,) , dtype = int)

def PUSH(n):
    global top
    if(top == MAX - 1):
        print("\n\tStack is Overflow\n")
    else: 
        top = top + 1 
        STACK[top] = n 
        print("\n\t" , n , " is Pushed at Stack Top\n")

def POP():
    global top
    if(top == -1):
        print("\n\tStack is Underflow")
    else: 
        print("\n\t",STACK[top], " is Poped From Stack\n")
        top = top - 1 
        
def Show():
    global top
    if(top == -1):
        print("\tStack is Underflow")
    else:
        print("\n\tSTACK: ")
        print("\n\tIndex\tSTACK")

        for i in range(top, -1 , -1):
            print("\n\t" , i , "\t" ,  STACK[i] )
while True:
    print("\n\n\t * * * STACK MENU * * * \n")
    print("\n\t1 --> PUSH\n")
    print("\n\t2 --> POP\n")
    print("\n\t3 --> SHOW\n")

    choice = int(input("\tEnter Your Choice : "))

    match choice:
        case 1:
            val = int(input("\n\tEnter an integer value to insert : "))
            PUSH(val)
        
        case 2:
            POP()
        
        case 3:
            Show()
            
        case _:
            print("\n\tInvalid Choice\n")
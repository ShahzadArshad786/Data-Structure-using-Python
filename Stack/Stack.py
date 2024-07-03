import numpy as np 
import sys 

MAX = int(input("\nEnter Size of the Stack : "))
top = -1 

STACK = np.ndarray(shape=(MAX,) , dtype = int)

def PUSH(n):
    global top
    if(top == MAX - 1):
        print("\nStack is Full\n")
    else: 
        top = top + 1 
        STACK[top] = n 
        print("\n",n,"is Pushed at Stack Top\n")

def POP():
    global top
    if(top == -1):
        print("\nStack is Empty")
    else: 
        print("\n",STACK[top], " is Poped From Stack\n")
        top = top - 1 

def PEEK():
    global top
    if(top == -1):
        print("\nStack is Empty")
    else: 
        print("\nStack TOP : ",STACK[top] , "\n")
       
def Show():
    global top
    if(top == -1):
        print("\nStack is Empty")
    else:
        print("\n*** *** STACK DATA *** ***")
        print("\n\tIndex\tSTACK")

        for i in range(top, -1 , -1):
            print("\n\t" , i , "\t" ,  STACK[i] )


print("\n* * * STACK MENU * * *\n")
print("1 --> PUSH in STACK\n")
print("2 --> POP From STACK\n")
print("3 --> SHOW STACK\n")
print("4 --> PEEK of STACK\n")
print("5 --> EXIT")
while True:
    choice = int(input("\nEnter Your Option : "))
     
    match choice:
        case 1:
            val = int(input("\nEnter Value to be Pushed : "))
            PUSH(val)
    
        case 2:
            POP()
        
        case 3:
            Show()
            
        case 4:
            PEEK()

        case 5:
            quit()
            
        case _:
            print("\nInvalid Choice\n")
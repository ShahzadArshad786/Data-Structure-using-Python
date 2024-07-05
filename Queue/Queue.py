import numpy as np

MAX = int(input("Enter the Size of the Queue : "))
QUEUE = np.ndarray(shape = (MAX,) , dtype = int)

Front = -1
Rear  = -1

def Enqueue(x):

    global Front, Rear

    if Rear == MAX - 1:
        print("\nQueue is Full")

    elif Front == -1 and Rear == -1:
        Front = Rear = 0
        QUEUE[Rear] = x
        print("\nData Inserted :", QUEUE[Rear])
        print("------------------------------------")

    else:
        Rear = Rear + 1
        QUEUE[Rear] = x
        print("\nData Inserted :", QUEUE[Rear])
        print("------------------------------------")

def Dequeue():
    global Front, Rear

    item = None
    if Front == -1:
        print("\tQueue is Empty")
        print("----------------------------------")

    elif Front == Rear:
        item = QUEUE[Front]
        Front = Rear = -1
        print("Data Removed at Front :", item)
        print("----------------------------------")

    else:
        item = QUEUE[Front]
        Front = Front + 1
        print("Data Removed at Front :", item)
        print("----------------------------------")

def Peek():
    global Front

    if(Front == -1):
        print("\tQueue is Empty")
        print("-------------------------------")
    else:
        print("Front of Queue : ", QUEUE[Front])
        print("-------------------------------")

def display():
    global Front, Rear

    if Front == -1:
        print("\tQueue is Empty")
        print("-----------------------------")

    else:
        print("\n\tIndex | Data ")
        print("\n\tFront : " , Front)
        for i in range(Front, Rear + 1):
            print("\n\t", i, "   |", QUEUE[i])
        print("\n\tRear  : " , Rear)
        print("-----------------------------")

print("\n\n** ** QUEUE MENU ** **")
print("\n1 : ENQUEUE OPERATION")
print("\n2 : DEQUEUE OPEARTION")
print("\n3 : PEEK OPERATION")
print("\n4 : DISPLAY QUEUE")
print("\n5 : EXIT")

while True:
    choice = int(input("\nEnter Your Choice : "))

    match choice:

        case 1:
            print("------------------------------------")
            print("\tENQUEUE OPERATION")
            print("------------------------------------")
            n = int(input("\nEnter Element to be Insert in Queue : "))
            Enqueue(n)

        case 2:
            print("----------------------------------")
            print("\tDEQUEUE OPERATION")
            print("----------------------------------")
            Dequeue()
        
        case 3:
            print("-------------------------------")
            print("\tPEEK OPERATION")
            print("-------------------------------")
            Peek()

        case 4:
            print("-----------------------‐-----")
            print("\tDISPLAY QUEUE")
            print("-----------------------------")
            display()

        case 5:
            quit()

        case 6:
            print("\nInvalid Option. Try Again.")
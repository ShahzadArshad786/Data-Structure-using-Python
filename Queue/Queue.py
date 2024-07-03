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
    else:
        Rear += 1
        QUEUE[Rear] = x
        print("\nData Inserted :", QUEUE[Rear])

def Dequeue():
    global Front, Rear
    item = None
    if Front == -1:
        print("\nQueue is Empty")
    elif Front == Rear:
        item = QUEUE[Front]
        Front = Rear = -1
        print("\nData Removed at Front :", item)
    else:
        item = QUEUE[Front]
        Front += 1
        print("\nData Removed at Front :", item)

def display():
    global Front, Rear
    if Front == -1:
        print("\nQueue is Empty")
    else:
        print("\n*** *** QUEUE DATA *** ***")
        print("\n\tIndex | Data ")
        print("\n\tFront : " , Front)
        for i in range(Front, Rear + 1):
            print("\n\t", i, "   |", QUEUE[i])
        print("\n\tRear  : " , Rear)

print("\n\n** ** QUEUE MENU ** **")
print("\n1 : For EnQueue Data")
print("\n2 : For DeQueue Data")
print("\n3 : For Display Data")

while True:
    choice = int(input("\nEnter Your Choice : "))

    match choice:

        case 1:
            n = int(input("\nEnter Item  Insert in Queue : "))
            Enqueue(n)

        case 2:
            Dequeue()

        case 3:
            display()
        case 4:
            print("\nInvalid Option. Try Again.")
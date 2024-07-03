import math
import numpy as np 

MAX = int(input("\nEnter Size of the Queue : "))

QUEUE = np.ndarray(shape= (MAX,) , dtype = int)

Front = -1
Rear = -1

def Enqueue(x):
    global Front , Rear

    if (Rear + 1) % MAX == Front:
        print("\nQueue is Over Flow")

    elif Front == -1 and Rear == -1:
        Front = Rear = 0
        QUEUE[Rear] = x
        print("\nData Inserted : ", QUEUE[Rear])

    else:
        Rear = (Rear + 1) % MAX
        QUEUE[Rear] = x
        print("\nData Inserted : ", QUEUE[Rear])

def Dequeue():
    global Front , Rear

    item = 0
    if Front == -1 and Rear == -1:
        print("\nQueue is empty")

    elif Front == Rear:
        item = QUEUE[Front]
        Front = Rear = -1
        print("\nData Removed at Front :", item)

    else:
        item = QUEUE[Front]
        Front = (Front + 1) % MAX
        print("\nData Removed at Front :", item)

def display():
    global Front, Rear
    if Front == -1 and Rear == -1:
        print("\nQueue is empty")

    else:
        print("-------------------")
        print("CIRCULAR QUEUE DATA")
        print("-------------------")
        print("Index\t Data ")
        print("-------------------")
        i = Front
        while i != Rear:
            print(" ", i, "\t", QUEUE[i])
            i = (i + 1) % MAX
        print(" ", i, "\t", QUEUE[i])
        print("-------------------")

print("\n\n** ** QUEUE MENU ** **")
print("\n1 : For EnQueue")
print("\n2 : For DeQueue")
print("\n3 : For Display")

while True:
    choice = int(input("\nEnter Your Choice : "))
    match choice:
        case 1:
            n = int(input("\nEnter an Queue Element : "))
            Enqueue(n)

        case 2:
            Dequeue()

        case 3:
            display()

        case _:
            print("\nInvalid Choice. Try Again")
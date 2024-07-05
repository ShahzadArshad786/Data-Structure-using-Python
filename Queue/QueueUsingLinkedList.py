import sys

class Node:
    def __init__(self):
        self.data = 0
        self.next = None 
class Queue:
    def __init__(self):
        self.front = None
        self.rear  = None
        
    def Enqueue(self):
        x = int(input("Enter Element to be inserted into Queue : "))
        newNode = Node()
        newNode.data  = x
        if self.front is None:
            self.front = newNode
            self.rear = newNode
            print("\nElement Inserted : ", self.front.data)
            print("------------------------------------")
    
        else:
            self.rear.next = newNode 
            self.rear = newNode
            print("\nElement Inserted : ", self.rear.data)
            print("------------------------------------")
            
    def Dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            print("-------------------")
        elif self.front.next is None:
            
            print("\nPoped Element is : ",self.front.data)
            print("---------------------")
            self.front =  None
        else: 
            temp = self.front
            print("\nPoped Element is : ",self.front.data)
            print("------------------------")
            self.front = temp.next 
            temp = None 
     
            
    def Peek(self):
        if self.front is None:
            print("Queue is Empty")
            print("-------------------")
        else:
            print("FRONT OF QUEUE IS : ",self.front.data)
            print("-----------------------")
    
    
    def Display (self):
        if self.front is None:
            print("Queue is Empty")
            print("---------------‐--")
        else:
            print("ELEMENTS OF THE QUEUE ARE :")
            temp  = self.front
            while temp:
                print(temp.data,"==>",end =" ")
                temp = temp.next 
            print("NULL")
            print("\nFront of Queue is :", self.front.data)
            print("Rear  of Queue is :", self.rear.data)
            print("-----------------------------")

s = Queue()

print("\n1 : ENQUEUE OPERATION")
print("\n2 : DEQUEUE OPERATION")
print("\n3 : PEEK OPERATION")
print("\n4 : DISPLAY QUEUE")
print("\n5 : EXIT")

while 1:
    
    
    op = int(input("\nEnter Your Option : "))
    match op:
        case 1:
            print("------------------------------------")
            print("\tENQUEUE OPERATION")
            print("------------------------------------")
            s.Enqueue()
            
        case 2:
            print("------------------------")
            print("DEQUEUE OPERATION")
            print("------------------------")
            s.Dequeue()
            
        case 3:
            print("-----------------------")
            print("PEEK OPERATION")
            print("-----------------------")
            s.Peek()
            
        case 4:
            print("-----------------------‐-----")
            print("\tDISPLAY QUEUE")
            print("-----------------------------")
            s.Display()
        
        case 5:
            quit()
        case _:
            print("\nInvalid Choice. Try Again\n")
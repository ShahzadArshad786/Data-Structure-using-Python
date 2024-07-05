import sys 

class Node:
    def __init__(self):
        self.data = 0
        self.next = None 

class Stack:
    def __init__(self):
        self.top = None
        
    def Push(self):
        x = int(input("Enter Element to be inserted into Stack : "))
        newNode = Node()
        newNode.data  = x

        if self.top is None:
            self.top = newNode
            newNode.next = None
            print("\nElement Pushed : ", self.top.data)
            print("--------------------------------------------")

        else:
            newNode.next = self.top
            self.top = newNode
            print("\nElement Pushed : ", self.top.data)
            print("--------------------------------------------")
            
    def Pop(self):
        if self.top is None:
            print("Stack is Empty")
            print("------------------------------")
        elif self.top.next is None:
            
            print("Poped Element is : ",self.top.data)
            print("------------------------------")
            self.top =  None
        else: 
            temp = self.top
            print("Poped Element is : ",self.top.data)
            print("------------------------------")
            self.top = temp.next 
            temp = None 
            
    def Peek(self):
        if self.top is None:
            print("Stack is Empty...")
            print("------------------------")
        else:
            print("TOP OF STACK IS : ",self.top.data)
            print("------------------------")
    
    def Display (self):
        if self.top is None:
            print("\tStack is Empty")
            print("---------------‐----------------------")

        else:
            temp  = self.top
            while temp:
                print(temp.data,"==>", end = " ")
                temp = temp.next 
            print("NULL")
            print("---------------‐----------------------")

s = Stack()

print("\n1 : PUSH OPERATION")
print("\n2 : POP OPERATION")
print("\n3 : PEEK OPERATION")
print("\n4 : DISPLAY STACK DATA")
print("\n5 : EXIT")

while 1:
    
    op = int(input("\nEnter Your Option : "))
    match op:
        case 1:
            print("--------------------------------------------")
            print("\t\tPUSH OPERATION")
            print("--------------------------------------------")
            s.Push()
            
        case 2:
            print("------------------------------")
            print("\tPOP OPERATION")
            print("------------------------------")
            s.Pop()
            
        case 3: 
            print("------------------------")
            print("PEEK OPERATION")
            print("------------------------")
            s.Peek()

        case 4:
            print("---------------‐----------------------")
            print("\tDISPLAY STACK DATA")
            print("---------------‐----------------------")
            s.Display()

        case 5:
            quit()

        case 6:
            print("\nInvalid Choice. Try Again\n")
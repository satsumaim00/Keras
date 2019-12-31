class Node:
    def __init__(self, item, next):
        self.item=item
        self.next=next

def enQue(item):
    global front
    global rear
    global size
    new=Node(item,None)
    if size==0:
        front=rear=new
    else:
        rear.next=new
        rear=new
    size+=1

def deQue():
    global front
    global rear
    global size
    if size != 0:
        res=front.item
        front=front.next
        size-=1
        if size == 0:
            rear=None
    else:
        print("unflow!! 츌력불가!")

    return res

def printQ():
    if size == 0:
        print("Queen is Empty")
    else:
        print("front <-\t", end='')
        p = front
        while p:

            if p.next != None:
                print(p.item, "<=", end="")
            else:
                print(p.item, '<=rear')
                p = p.next




front=rear=Node
size=0
enQue('aaa')
enQue('bbb')
enQue('ccc')
printQ()
deQue()
print('deQue data=',res)
printQ()
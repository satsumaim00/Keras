class Node:
    def __init__(self, item, link):
        self.item=item
        self.link=link

def push(item):
    global top #아래꺼랑 밑에꺼랑 별개의 함수가된다네요
    global size
    # if max<=size:     언급x
    #     print("overflow!")
    #     return
    top=Node(item, top)
    size+=1

def pop():
    global top
    global size
    if size!=0:
        top_item=top.item
        top=top.link
        size -=1
        return top_item
    else:
        print("underflow발생, 츨력불가")
def peak():
    global top
    if size!=0:
        return top.item
    else:
        print("underflow발생, 츨력불가")
        return None;
def printStack():
    print("Top ->\t", end='')
    p=top
    while p:
        if p.link!=None:
            print(p.item, "=>", end="")
        else:
            print(p.item)
            p=p.link
    #\t 텍문자
#max=10
top=None
size=0
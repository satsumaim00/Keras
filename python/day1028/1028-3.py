class Node:
    def __init__(self, name, left=None, right=None):
        self.name=name
        self.left=left
        self.right=right

def map():
    n1=Node("A")
    n2=Node("B")
    n3=Node("C")
    n4=Node("D")
    n5=Node("E")
    n6=Node("F")
    n7=Node("G")
    n8=Node("H")
    n9=Node("I")
    n10=Node("J")
    n11=Node("K")
    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5
    n3.left=n6
    n3.right=n7
    n4.left=n8
    n4.right=n9
    n5.left=n10
    n5.right=n11
    return n1

def preOrder(n):
    if n!=None:
        print(n.name + '=>', end="")
        preOrder(n.left)
        preOrder(n.right)

def postOrder(n):
    if n!=None:
        postOrder(n.left)
        postOrder(n.right)
        print(n.name + '=>', end="")


def inOrder(n):
    if n!=None:
        inOrder(n.left)
        print(n.name + '=>', end="")
        inOrder(n.right)


start=map()
print("inOrder :\t", end='')
inOrder(start)
print()
print("preOrder :\t", end='')
preOrder(start)
print()
print("postOrder :\t", end='')
postOrder(start)
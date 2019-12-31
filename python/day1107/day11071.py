from day1107.binTree import Node, BinaryTree

t=BinaryTree()
n1=Node("A")
n2=Node("B")
n3=Node("C")
n4=Node("D")
n5=Node("E")
n6=Node("F")
n7=Node("G")
n8=Node("H")
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=5
n3.left=6
n4.right=7
n4.left=8
t.root=n1

print("tree의 높이:", t.height(t.root))
print("tree의 노드개수:", t.size(t.root))

u=BinaryTree
g.root=t.copyTree(t.root)
print('t와 u를 비교:', t.isEqual(t.root, u.root))
print('프리오더:',end='')
t.preOrder(t.root)
print()
print('인오더:',end='')
t.inOrder(t.root)
print()
print('포스트오더:',end='')
t.postOrder(t.root)
print()
print('레벨오더:',end='')
t.levelOder(t.root)
print()
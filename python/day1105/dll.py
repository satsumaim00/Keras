class DLList:
    class Node:
        def __init__(self, name, age, pre, next):
            self.name=name
            self.age=age
            self.pre=pre
            self.next=next

    def __init__(self):
        #self.head=self.Node(None, None, None, None)
        self.head=None
        self.size=0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def searchNode(self, pos):
        p=self.head
        if pos=="":
            return None
        while p!=None:
            if p.name==pos:
                return p
            p=p.next

    def printDLL(self):
        p = self.head

        print('haed=', self.head)
        while True:
            if self.isEmpty():
                print("isEmpty")
                break
            elif p.next != None:
                print("[",p.name, p.age, "]<=> ", end='')
                break
            else:
                print("[",p.name, p.age,"]")
                break
            p = p.next

    def insert(self, nm, age, pos=""):#p다음에 삽입
        #최초삽입
        p=self.searchNode(pos)
        if self.head==None:
            #new=self.Node(nm, age, self.head, self.head)
            new=self.Node(nm, age, None, None)
            self.head=new
            self.size+=1
        #첫노드 삽입
        elif self.head!=None and p==None:
            new=self.Node(nm, age, None, self.head)
            self.head.pre=new
            self.head=new
            self.size += 1
        #중간노드 삽입
        elif p!=None:
            if p.next!=None:
                new = self.Node(nm, age, p, p.next)
                p.next.pre=new
                p.next=new

            else:#마지막 노드 주소 찾기
                new = self.Node(nm, age, p, None)
                p.next = new
            self.size += 1

    def delete(self, pos):
        p=self.searchNode(pos)
        if p.pre==None and p.next==None: #앞,뒤 노드 다없음
            self.head=None
        elif p.pre==None:
            self.head=p.next
            p.next.pre=p.pre #p.next.pre=None
        elif p.next == None:
            p.pre.next=p.next #p.pre.next=None
        #elif not(p.pre==None or p.next==None):
        else:
            p.pre.next=p.next
            p.next.pre=p.pre
        self.size=-1


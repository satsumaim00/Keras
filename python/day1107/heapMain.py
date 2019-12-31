# heapMain.py
from d1107.binheap import *
def menu():
    print('-----menu-----')
    print('1.insert node')
    print('2.delete node')
    print('3.print node')
    print('0.exit')
    print('--------------')
    print('select menu :',end='')

if __name__=='__main__':
    a = [None]*1 # a=[[]]
    a.append([90,'수박'])
    a.append([80, '배'])
    a.append([70, '멜론'])
    a.append([50, '라임'])
    a.append([60, '망고'])
    a.append([20,'체리'])
    a.append([30, '포도'])
    a.append([35, '오렌지'])
    a.append([10, '귤'])
    a.append([15,'바나나'])
    a.append([45,'레몬'])
    a.append([40,'키위'])
    bh=BinHeap(a)
    # print('힙 구성 전의 트리 확인')
    # bh.printHeap()
    bh.create_Heap()

    # print('최소힙')
    # bh.printHeap()
    # print('최소값[root]삭제: ')
    # print('삭제된 루트: ',bh.delete_min())
    # bh.printHeap()
    # bh.insert([8,'사과'])
    # bh.printHeap()

    while True:
        menu()
        sel=int(input())
        if sel==1:
            key=int(input("키입력"))
            fruit=input('삽입할 과일')
            hlist=[key,fruit]
            bh.insert(hlist)
        elif sel==2:
            print('root삭제')
            print(bh.delete_min())
        elif sel==3:
            print('힙출력:')
            bh.printHeap()
        elif sel==0:
            print('고생')
            break
        else:
            print('보고 선택하십셔')
            continue
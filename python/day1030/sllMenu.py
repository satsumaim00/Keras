from d1030.SLList import SLList


def menu():
    print('==== MENU ====')
    print('1.앞에 삽입')
    print('2.뒤에 삽입')
    print('3.처음 삭제')
    print('4.선택 삭제')
    print('5.검색')
    print('6.리스트 출력')
    print('0.종료')

if __name__=='__main__':
    s = SLList()
    while True: #무조건 반복
        menu()
        sel=int(input('menu select:'))
        if sel==1:
            data=input('삽입할 데이터 입력')
            s.insertFront(data)
        elif sel==2:
            data = input('삽입할 데이터 입력:')
            pos = input('삽입할 위치 입력:')
            p = s.searchNode(pos)
            s.inserRear(data, p)
        elif sel==3:
            s.deleteFront()
        elif sel==4:
            pos = input('삽입할 앞위치 입력:')
            p = s.searchNode(pos)
            s.deleteRear(p)
        elif sel==5:
            data = input('검색할 데이터 입력')
            pos = s.search(data)
            print(data+'는 '+str(pos+1)+'번째에 있다')
        elif sel==6:
            print('결과: ', end='')
            s.printsll()
        elif sel==0:
            print('사용을 완료하셨습니다 안녕')
            break

        else:
            print('선택실패 다시 선택하시오.')


from day1031.cll import cll

if __name__=='__main__':
    s=cll()
    s.insertFront('둘리')
    s.insertFront('도우너')
    s.insertFront('공실이')
    s.insertFront('고길동')
    s.printsll()
    p = s.searchNode('공실이')
    s.inserRear('마이콜', p)
    s.printsll()
    p = s.searchNode('고길동')
    s.deleteRear(p)
    s.printsll()
    #한개일때 삭제
    s.deleteRear(None)
    s.printsll()


# def menu():
#     print('==== MENU ====')
#     print('1.앞에 삽입')
#     print('2.뒤에 삽입')
#     print('3.처음 삭제')
#     print('4.선택 삭제')
#     print('5.검색')
#     print('6.리스트 출력')
#     print('0.종료')

# if __name__=='__main__':
#     s = cll()
#     while True: #무조건 반복
#         menu()
#         sel=int(input('menu select:'))
#         if sel==1:
#             data=input('삽입할 데이터 입력')
#             s.insertFront(data)
#         elif sel==2:
#             data = input('삽입할 데이터 입력:')
#             pos = input('삽입할 위치 입력:')
#             p = s.searchNode(pos)
#             s.inserRear(data, p)
#         elif sel==3:
#             s.deleteFront()
#         elif sel==4:
#             pos = input('삽입할 앞위치 입력:')
#             p = s.searchNode(pos)
#             s.deleteRear(p)
#         elif sel==5:
#             data = input('검색할 데이터 입력')
#             pos = s.search(data)
#             print(data+'는 '+str(pos+1)+'번째에 있다')
#         elif sel==6:
#             print('결과: ', end='')
#             s.printsll()
#         elif sel==0:
#             print('사용을 완료하셨습니다 안녕')
#             break
#
#         else:
#             print('선택실패 다시 선택하시오.')

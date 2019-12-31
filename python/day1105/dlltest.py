from day1105.dll import DLList

dl=DLList()
print(dl.head)
dl.insert("철수", 12)
dl.printDLL()
dl.insert("영희", 11)
dl.printDLL()
dl.insert("길동",40,"철수")
dl.printDLL()
dl.insert("둘리",7,"영희")
dl.printDLL()
print(dl.size)

#삭제
dl.delete("영희")
dl.printDLL()
dl.delete("철수")
dl.printDLL()
dl.delete("둘리")
dl.printDLL()
dl.delete("길동")
dl.printDLL()
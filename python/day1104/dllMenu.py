from day1104.dll import DLList

dl=DLList()
print(dl.head)
dl.insert("철수", 12)
dl.printDLL()
dl.insert("영희", 11)
dl.printDLL()
dl.insert("길동",40,"점수")
dl.printDLL()
dl.insert("둘리",7,"영희")
dl.printDLL()

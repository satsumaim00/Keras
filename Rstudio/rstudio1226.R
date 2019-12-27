setwd("c:/r_data") #작업 디렉토리 설정
getwd()
print(1+2)
1+2
data1=1
data1='1' #''문자
data1=2.1

class(data1)

print(1,2,3)  #print는 하나만 출력 문자열은 처리도 안됨
cat(1,2,3,4)
cat('a','b','c')

4/2   #나누기 값 (실수)
5/2
4%%2  #나머지
5%%2
4%/%2   # 정수 / 몫

3^2
3**2
10000
100000
1e2
1e2
32-1
3e-1
1+'2'
as.numeric('2')
1+as.numeric('2')  #강제 형변환 : as.~ (그 형 타입으로 바뀌어라)
as.numeric('2')+as.numeric('1')
'data2'

# &,| 같다 

#NA, NULL
#NA:잘못된 값이 들어온 경우
#NULL : 값이 없을 경우 
cat(1,NA,2)
sum(1,2,NA, na.rm = T)
sum(1,2,NULL)
#Facter형 : 여러번 중복되어 나오는 데이터들을 각 값으로 모아서 대표값을 출력
txt1=read.csv("factor_test.txt")
txt2=factor(txt1$blood)
txt2
txt1
summary(txt2)
sex1=factor(txt1$sex)
summary(sex1)

#날짜시간 
Sys.Date()
Sys.time()
class(date())
as.Date("2019-12-26")
as.Date("26-12-2019")
as.Date("26-12-2019",format="%d-%m-%Y") 
as.Date("26-12-2019",format="%d-%m-%y")# 2020 20이 두번 출력
as.Date("2019년 12월 26일",format="%Y년 %m월 %d일")
as.Date("26122019",format="%d%m%Y") 
as.Date(100, origin="2019-12-26") 
"2019-12-26"-"2019-09-17"
as.Date("2019-12-26")-as.Date("2019-09-17")
as.Date("2019-12-26")+100
#posIxlt : 날짜를 년,월,일
#POSIXct : 년,월,시,분,초
as.date("2019-12-26 18:20:00")-as.Date("2019-12-26 13:20:00")
as.POSIXct("2019-12-26 18:20:00")-as.POSIXct("2019-12-26 13:20:00")
install.packages("lubridate")
library(lubridate)

date=now()
date
year(date)
month(date)
wday(date, label = T)
date=date+days(10)
date
seq(as.Date("2020-01-01"),as.Date("2020-12-31"), 1)
seq(as.Date("2020-01-01"),as.Date("2020-12-31"), "month")
seq(as.Date("2020-01-01"),as.Date("2200-12-31"), "year")
#a1=1,2,3,4,5,6
a1=1:10 #문자는 안됨
a1
a1=10; b1=20
a1+b1
objects()
rm(list=ls())
objects()

#데이터처리 객체
#동일 데이터타입
#스칼라 : 단일 데이터 처리
#벡터 : 1차원배열(스칼라를 여러개 합친것)
#Matrix : 2차원배열(벡터를 여러개 합친것)
#배열(array) : 3차원배열(matrix를 여러개 쌓아놓은것)
#다른데이터타입
#list : 벡터와 비슷(키, 값)형태로 저장
#데이터프레임 : 엑셀의 표,db의 테이블과 비슷

c(1,2,3,4,5)
c('a','b','c')
c(1,2,3,'a')#숫자 문자화됨
#1. c()함수로 작성
#2. 인덱스는 1로 시작
#3. 하나의 자료형만 사용
#4. 결측값은 'NA'로 사용
#5. NULLn은 어떤 형식도 취하지 않는 특별한 객체
v1=c(11,22,33,44,55)
v1
v1[3]
v1[-3]
v1[1:4]
v1[-2:-4]
v1[2]=6
v1
v1=c(v1,7)
v1
v1[9]=9
v1
v1=append(v1,10,after=33)
v1=append(v1,10,after=3)
v1=append(v1, c(100,110), after=4)
v1
c(1,2,3)+c(2,3,4)
v1=c(1,2,3)
v2=c(2,3)
v1+v2
v1=c(1,2,3)
v2=c("2","3","4")
v1+v2
union(v1,v2)
v1=c(1,2,3)
v2=c(3,4,5)
setdiff(v1,v2) #차집합
intersect(v1,v2) #교집합
#벡터에 걸럼이름 지정
fruits=c(10,20,30)
fruits
names(fruits)=c('apple','banana','peach')
fruits
v3=seq(1,5)
v3
v4=seq(-1,-10)
v4
v5=rep(1:3,2)
v5
v5=rep(1:3,each=3)
v5
length(v1)
v1
NROW(v1)
v6=c(1,3,5,7,9)
3 %in% v6#특정문자 있는지 찾는거
4 %in% v6
#행렬 : matrix
#1. 벡터를 여러개 합친것
#2. 모든 컬럼과 행은 데이터형이 동일
#3. 기본적으로 열로 생성
#4. 다른 데이터타입의 데이터를 저장할 경우 데이터 프레임을 사용
m1=matrix(c(1,2,3,4),nrow = 2, byrow = T) #byrow행우선(가로입력)
m1
m1[ ,1] # 모든행에서 1열
m1[1, ]
m2=matrix(c(1,2,3,4,5,6,7,8,9), nrow=3, byrow = T)
m2
m2[,2]
m2[3,]
#행추가 : rbind()
#열추가 : cbind()
m3 = rbind(m2,c(11,22,33))
m3 = cbind(m3,c(111,222,333,444))
m3 = cbind(m3,c(1111,2222,3333,)) #리컬시브되서 1111이 4번째에 들어감
m3
colnames(m3)=c('1st','2nd','3rd','4th','5th')
m3
arrl=array(c(1:12),dim=c(2,2,3))
arrl[1,1,2]
#list : 서로 다른 데이터 유형
li=list(name='홍길동',addr='서울',tel='010-',pay=500)
li
li$tel
li[1:3]
li$birth='2000-01-01'
li
li$name=c('김유신, 이순신')#그냥 이대로 하면 위에 덮어씌어짐
li
li$name[length(li$name)+1]='홍길동'
li
li$birth=NULL
li
li$name[length(li$name)-1]=NULL
li
#데이터프레임 생성
#1. 백터로 부터 데이터프레임 생성 : 각 컬럼별로 먼저 생성한 후 data.frame멍령어로 모든 컬럽을 합친다.
np=c(1,2,3,4)
name=c('apple','banana','peach','grape')
price=c(500,200,100,50)
qty=c(6,2,4,7)
sales=data.frame(NO=no, NAME=name, PRICE=price, QTY=qty)
sales
#행렬로부터 데이터프레임 생성
sales=matrix(c('apple',500,5,2,'peach',200,2,3,'banana',50,7,20),nrow=4,byrow=T)
sales
df1=data.frame(sales,stringsAsFactors = F)
df1
names(df1)=c('NO','NAME','PRICE','QTY')
df1
class(sales)
class(df1)
str(sales)
str(df1)

df1$NAME
sales[c(1,2),]
sales[,c(1:3)]

subset(sales, qty >= 5)

#데이터프레임 합치기 : rbind(),cbind(),merge()
no = c(1,2,3)
name=c('apple','banana','peach')
price=c(100,200,300)
df1=data.frame(NO=no,NAME=name,PRICE=price)
df1
no=c(10,20,30)
name=c('train','car','ship')
price=c(1000,2000,3000)
df2=data.frame(NO=no,NAME=name,PRICE=price)
df2
df3=cbind(df1,df2)
df3
df4=rbind(df1,df2)
df4

df1=data.frame(name=c('apple','banana','peach'), price=c(300,200,100))
df2=data.frame(name=c('apple','cherry','berry'), qty=c(10,20,30))
df1
df2

merge(df1,df2) #이름이 공통된 컬럼만 표시됨
merge(df1,df2,all = T) # 이건 그냥 다 보여줌
df1
new=data.frame(name='mango', price=400)
df2=rbind(df1.new)
df1
df2
df3=rbind(df2, data.frame(name='berry', price=500))
df4=cbind(df3, data.frame(qty=c(10,20,30,40,50)))
df4

#데이터프레임에서 특정 걸럼만 골라내서 새로운 형태 만들기
no=c(1,2,3,4,5)
name=c('홍길동','이순신','유관순','김유신','윤동주')
addr=c('서울','경기','부산','광주','제주')
tel=c(1111,2222,3333,4444,5555)
hobby=c('놀기','먹기','자기','놀먹','자먹')
member=data.frame(NO=no,NAME=name,ADDR=addr,TEL=tel,HOBBY=hobby)
member
mem1=subset(member, select = c(NO, NAME, ADDR))
mem1
mem2=subset(member,select=-TEL)
mem2
colnames(mem2)=c('번호','이름','주소','취미')
mem2
#nrow,ncol,names,rownames()==row.names(),colnames()==col.names()
#데이터 수정하기 : 변수명바꾸기
#install.packages("dplyr")
#library(dplyr)

df1=data.frame(varl=c(1,2,3), var2=c(2,3,2))
df1
df2=df1
df2=rename(df1,v2=var2)
df2
#파생변수
df3=data.frame(var1=c(4,3,8), var2=c(2,6,11))
df3
df3$sum=df3$var1+df3$var2
df3
df3$mean=df3$sum/2
df3
#install.packages("ggplot2")
#library(ggplot2)
mpg
mpg1=mpg
mpg1=rename(mpg1,city=cty)
mpg1=rename(mpg1,highay=hwy)
mpg1
head(mpg1,5)#기본값은 6개 가져옴 아래것도
tail(mpg1)

list.files(recursive = T) #()속성은 하위디렉토리도 다 출력
list.files(all.files = T) #숨겨진 파일 표시시
sc1=scan("scan_1.txt") # 텍스트파일을 읽어서 배열에 저장
sc1
sc2=scan("scan_2.txt",what="")
sc2
sc3=scan("scan_3.txt",what="")
sc3
sc3=scan("scan_4.txt",what="")
sc3
sc4=scan()
sc4
sc5=scan(what = "")
sc5
#readline() : 한 줄 읽들이기
in1=readline()
in1
in2=readline("R U ok?")
in2
#readlines() : 파일을 배열에 저장
in3=readLines("scan_4.txt")
in3
fruits=read.table("fruits.txt",header = T) #header속성해야 제대로나옴
#read.table을 통해 데이터를 불러들여 데이터 프레임에 넣는다
fruits
fruits=read.table("fruits_2.txt",header = F) #안쓸대도 있습니다
#read.table을 통해 데이터를 불러들여 데이터 프레임에 넣는다
fruits
fruits=read.table("fruits_2.txt",header = F,skip=3) #공백과 주석범위도 포함
fruits
fruits4=read.csv("fruits_4.csv",header = F)
fruits4
label=c('NO','NAME','PRICE','QTY')
fruits4=read.csv("fruits_4.csv",header = F,col.names = label)
fruits4

install.packages("googleVis")
library(googleVis)
install.packages("sqldf")
library(sqldf)
Fruits
write.csv(Fruits,"Fruits_sql.csv",quote=F, row.names = F)
f2=read.csv.sql("Fruits_sql.csv",sql="select * from file where Year=2008")
f2

txt1=readLines("write_test.txt")
txt1
write(txt1,"write_test2.txt")

txt1=read.table("table_test.txt",header =  T)
txt1
write.table(txt1,"table_test2.txt")

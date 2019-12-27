
#2일차 20191227
#agreegate():다양한 함수를 사용하여 계산결과를 출력
#apply()
#cor():상관함수
#comsum():누적합
#cumprom():누적곱
#diff() : 차이나는 부분을 찾아냄
#length() : 길이
#max()
#min()
#mean()
#median()
#order()
#pord() : 누적곱
#range() : 범위값
#rank() 
#rev() : 요소 역순
#sd() : 표준편차
#sort() : 정렬
#sum()
#summary()
#sweep():일괄적으로 중진 데이터를 뺴기
#tapply:()백터엣 중진 함수 연산
#var(): 분산
v1=c(1,2,3,4,5)
v2=c('a,','b','c','d','e')
max(v2)
mean(v1)
mean(v2)
sd(v1)
sd(v2)
sum(v1)
var(v1)
#aggregate():데이터프레임 삼대로 중진 함수값 구한다
#aggregate(계산될컬럼~기준될컬럼, 데이터, 함수)
library(googleVis)
Fruits
aggregate(Sales~Year,Fruits,sum)
aggregate(Sales~Fruit,Fruits,sum)#과일별로 판매된 수량을 sum한 결과
aggregate(Sales~Year,Fruits,max)#과일별로 판매수량이 가장많은것
aggregate(Sales~Fruit+Year,Fruits,max)#과일별로 연도별 최대판매량을 출력

#apply():matrix에서 유용하게 사용(행, 열을 대상으로 작업)
#apply(대상, 행/열, 적용함수)
m1=matrix(c(1,2,3,4,5,6), nrow=2, byrow=T)
m1
apply(m1,1,sum) #행
apply(m1,2,sum) #열
apply(m1[,c(2,3)],2,sum)
#lapply(), sapply() : list 처리
#lapplt/sapply(대상, 적용함수)
l1=list(Fruits$Sales)
l1
l2=list(Fruits$Profit)
l2
lapply(c(l1,l2),max)
sapply(c(l1,l2),max)
lapply(Fruits[,c(4,5)],max)
sapply(Fruits[,c(4,6)],max)
#apply()/mapply():데이터셋의 특정요소(factor)를 처리
#tapply(츨력값, 기준컬럼, 적용함수)
#mapply(함수,벡터1,벡터2,...):백터나 리스트를 데이터프레임처럼처리
Fruits
tapply(Sales,Fruits,sum)
#attach:변수를 직접 사용하기 위한 함수
attach(Fruits)
tapply(Sales,Fruit,sum)
tapply(Sales,Year,sum)#년도별 합계 판매량
#mapply():
#만약 데이터프레임이 아닌 벡터나 리스트형태로 데이터들이 있을때 마치 데이터 프레임처럼 연산을 해주는 함수.단, 벡터들의 요소개수가 동일해야한다.
v1=c(1,2,3,4,5)
v2=c(10,20,30,40,50)
v3=c(100,200,300,400,500)
mapply(sum,v1,v2,v3)
#sweep():한꺼번에 차이 구하기->여러 데이터들에게 일괄적으로 기준을 적용
#벡터, 메트릭스,배열,데이터프레임으로 구성된 여러 데이터들에 동일한 기준 적 용 시켜 차이 나는 부분을 일목요연하게 보여주는 함수
m1
a=c(1,1,1)
sweep(m1,2,a)#apply 2가 열   sweep 1이 열
#ceiling():버림함수->주어진 수보다 큰수중 가장 작은 수
v1=c(1.2,1.9,2.1)
ceiling(v1)
choose(5,3)
floor(v1)#주어진 수보다 작은 수중에 가장 큰 정수
trunc(v1)#0과 주이전 수 사이의 가장 큰 정수
#사용자 정의 함수
#함수명 = function(인수 또는 입력값){
#계산식1
#계산식2
#return(계산 결과 반환값)
#}
#


f1=function(a,b){
  b=a^b
  return(b)
}
f1 #식 반환
f1(3,2) # 값 출력
  
s1 =Fruits$Sales
s1
sort(s1,decreasing = T)
#plyr():언본데이터를 분석하기 쉬운 형태로 나누어서 다시 새로운 형태로 만들어주는 패키지
#ply() \앞에 2글자: 첫글자 -> 입력될 데이터 유형, 두 번째 글자-> 출력될 데이터 유형
#d: dataframe. a: array(matrix 포함), l:list
#ddply(데이터,기준컬럼,함수또는 결과들), alply()
setwd("c:/r_data")
install.packages("plyr")
library(plyr)
fruits=read.csv("fruits_10.csv",header = T)
fruits
#summarise():기준컬럼의 데이터끼리 모은후 함수를 적용해서 출력(group by유사)
ddply(fruits,'name',summarise,sum_qty=sum(qty), sum_price=sum(price))
ddply(fruits,'name',summarise, max_qty=max(qty), min_price=min(price))
ddply(fruits,c('year','name'), summarise, max_qty=max(qty),sum_price=sum(price))
#tranform : 동일한 값의 합계가 아닌 각 항별로 연산을 수행해서 해당 값을 함께 출력
ddply(fruits, 'name',transform, sum_qty=sum(qty),pct_qty=round(qty/sum(qty)*100,2))
#dplyr() 패키지 
#특징 
#1.filter : 조건을 주어서 필터링 한다
#2. select : 여러 컬럼이 있는 데이터셋에서 특정 컬럼만 선택해서 사용
#3. arrange : 데이터들을 오름, 내림차순으로 정렬
#4. mutate : 기존에 변수를 활용해서 새로운 변수 생성
#5. summarise : 주어진 데티어를 집계(min,max,mean,count)
library(dplyr)
data1=read.csv("2013년_프로야구선수_성적.csv")
data1
data2=filter(data1, 경기>=120 & 득점 >= 80)
data2
data3=filter(data1, 포지션%in%c('1루수','3루수'))#c=conbine 함수
data3

select(data1,선수명,포지션)
select(data1,순위:타수)
select(data1,-홈런,-타점)
#여러문장을 조합해서 사용하는 명령어  %>% ctrl+shift+m    arrnage 정령
data1 %>% select(선수명,팀,경기,타수) %>% filter(타수>=400)
data1 %>% select(선수명,팀,경기,타수) %>% filter(타수>=400) %>%  arrange(desc(타수))
data1 %>% select(선수명,팀,경기,타수) %>%  mutate(경기x타수=경기*타수) %>% arrange(경기x타수)
data1 %>% select(선수명,팀,경기,안타,타수) %>%  mutate(안타율=round(안타/타수,3)) 

data1 %>% group_by(팀) %>% summarise(avarage=mean(경기), na.rm=T) 
                                                          #na제거 속성
data1 %>% group_by(팀) %>% summarise_each(list(mean=mean),경기,타수)
data1 %>% group_by(팀) %>% summarise_each(funs(mean,sum),경기,타수)#과거

#결축지
#누락된 값, 비어이는 값
#함수 적용 불가 븐석 결과 예측
#제거 후 분석 실시

df = data.frame(sex=c('M','F',NA,'M','F'), score=c(5,4,3,4,NA))
df
is.na(df)
table(is.na(df$sex))
table(is.na(df$score))

mean(df$sex)

df1=df %>% filter(!is.na(score)&!is.na(sex))
df %>% filter(!is.na(sex))
mean(df1$score)
df1
df1 =df %>% filter(!is.na(score)&!is.na(sex))
df2= na.omit(df)
df2

mean(df$score, na.rm = T)
exam=read.csv("csv_exam.csv")
exam
exam[c(3,8,15),'math']=NA
exam

exam %>% summarise(mean_math=mean(math, na.rm = T),
                   sum_math=sum(math, na.rm = T),
                   medain_math=median(math, na.rm = T),)
#결측치 대체
#다른값으로 채워넣기
#대체법 : 대표값(평균, 최빈값)으로 일괄 대체
#적용 : 통계분석기법, 예측값 추정
mean(exam$math, na.rm = T)
exam$math=ifelse(is.na(exam$math),55,exam$math)
exam
table(is.na(exam$math))

#이상치 : 정상범주에서 크게 벗어난 값
#이상치 포함시 분석결과 왜곡
#이상치를 결축 처리 후 제외하고 분석
df=data.frame(sex=c(1,2,1,3,2,1),score=c(5,4,3,4,2,6))
df
table(df$sex)
table(df$score)
boxplot(df$sex)
df1=df$sex=ifelse(df$sex==3,NA,df$sex)
df1 =df$score=ifelse(df$score>5,NA,df$score)
df
df1 %>% filter(!is.na(sex)&!is.na(score)) %>% group_by(sex) %>%  summarise(mean_score=mean(score))
df %>% filter(!is.na(sex)&!is.na(score)) %>% group_by(sex) %>%  summarise_each(funs(mean),score)

library(ggplot2)
boxplot(df$score)

#데이터 분석
#1.패키지 준비
#2.데이터 준비
#3.데이터 검토
#4.변수명 바꾸기
#5.데이터 분석
# 1단계:변수검토및 전처리
# 2단계:변수간 관계분석
#6.시각화


install.packages("foreign")
library(foreign)
install.packages("readxl")
library(readxl)

wf=read.spss(file="Koweps_hpc10_2015_beta1.sav",to.data.frame = T)
wf1=wf
wf1
head(wf1)
dim(wf1)
str(wf1)
summary(wf1)
wf1=rename(wf1, sex=h10_g3,
           birth=h10_g4,
           marriage=h10_g10,
           religion=h10_g11,
           income=p1002_8aq1,
           code_job=h10_eco9,
           code_region=h10_reg7)
class(wf1$sex)
table(wf1$sex)
table(is.na(wf1$sex))

wf1$sex=ifelse(wf1$sex==9,NA,wf1$sex)
table(is.na(wf1$sex))
wf1$sex=ifelse(wf1$sex==1,'male','female')
table(wf1$sex)
qplot(wf1$sex)
class(wf1$income)
summary(wf1$income)
hist(wf1$income)
qplot(wf1$income)
qplot(wf1$income)+xlim(0,1000)
wf1$income=(ifelse(wf1$income %in% c(0,9999),NA,wf1$income))
table(is.na(wf1$income))
sex_in=wf1 %>% filter(!is.na(income)) %>% group_by(sex) %>% summarise(mean_income=mean(income))
sex_in
ggplot(data=sex_in,aes(x=sex,y=mean_income))+geom_col()
class(wf1$birth)
summary(wf1$birth)
qplot(wf1$birth)
table(is.na(wf1$birth))
wf1$birth=ifelse(wf1$birth==9999, NA, wf1$birth)
table(is.na(wf1$birth))
wf1$age=2019-wf1$birth+1
summary(wf1$age)
qplot(wf1$age)
age_in=wf1 %>% filter(!is.na(income)) %>%  group_by(age) %>% summarise(mean_income=mean(income))
age_in
head(age_in,20)
ggplot(data=age_in,aes(x=age,y=mean_income))+geom_line()
melt(fruits, id='year') 

install.packages("reshape2")
library(reshape2)
fruits
melt(fruits, id=c('year','name')) #wide->long
melt(fruits, id=c('year','name'), variable.name = 'var_name', value.name = 'val_name')

mtest=melt(fruits, id=c('year','name'), variable.name = 'var_name',value.name = 'val_name')
mtest
dcast(mtest, year+name~var_name)
#string(패키지:작업할 대상 데이터가 문자일 경우)
install.packages("stringr")
library(stringr)
#str_detect()
fruits=c('apple','Apple','banana','pineapple')
str_detect(fruits,'A')
str_detect(fruits, '^a')
str_detect(fruits, 'e$')
str_detect(fruits, '^[a^]')
#ignore.case()
str_detect(fruits,ignore.case('a'))#아래처럼 바꿔서 써야함 (바뀜)
aa='a'
str_detect(fruits,fixed(aa,ignore_case = T))

p='a.b'
s=c('abb','a.b')
str_detect(s,p)
str_detect(s,fixed(p))
str_detect(s,coll(p))

fruits
str_count(fruits,fixed('A',ignore_case = T))
str_count(fruits,'a')
str_c('apple','pen')
str_c("FRUIT :  ", fruits)
str_c(fruits, " is name ", fruits)
str_c(fruits, collapse = ",")
str_dup(fruits,3)
str_length(fruits)
str_locate(fruits,'a')
str_replace('apple','p','*')
str_replace_all('apple','p','*')
fruits=str_c('apple','/','banana','/','cherry')
fruits
str_split(fruits,"/")
str_sub(fruits, start=1,end=3)
str_trim('       apppp   baabafa  acrdsed')#앞뒤 공백만 제거 가운데 있는건 제거 안됨
library(sqldf)
library(googleVis)
Fruits
sqldf('select * from Fruits')
#fruits 값이 apple인 모든정보
sqldf('select * from Fruits where Fruit = "Apples"')

sqldf('select * from Fruits limit 5')


f1=function(x){
  if (x<0){
    return (-x)
  }
  else if(x==0){
    return(x)
  }
  else{
    x=x*2
    return(x)
  }
}
f1(-2)
f1(2)
f1(0)

no=scan()
ifelse(no%%2==0,'짝수','홀수')

no=0
while(no<5){
  no=no+1
  if (no==3) {
    break
  }
  print(no)
}

f2=function(x){
  i=0
  for (j in 1:x){
    i=i+j
    print(i)
  }
}
f2(10)

f3=function(x,y){
  if ((x>1)&&(y>1)) {
    z=x*y
    return(z)
   }else{
    z=x+y
    return(z)
  }
}
f3(2,4)
f3(-1,3)

c1=c('apple','Apple','APPLE','banana','grape')
c2=c('apple','Apple')
grep(paste(c2,collapse = '|'),c1,value = T)#value = T 값으로 가져와라
grep('pp',c1)
grep('pp',c1,value=T)
grep('e$',c1,value=T)
grep('^A',c1)

c1=c('apple','Apple','APPLE','banana','grape')
c2=c('apple1','Apple2','orange','cherry')
grep('[[:upper:]]',c2,value = T)
nchar(c1) #문자열 길이
nchar('홍길동')
paste('a','b','c',sep='/') # sep='' 괄호안에 있는거 공백에서 그문자로 대체

substr('abc123',3,5)
strsplit("2019/12/27",split = '/')
regexpr('-','010-1111-2222')

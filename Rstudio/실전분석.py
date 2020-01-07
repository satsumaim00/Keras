setwd("c:/r_data") #작업 디렉터리 설정
getwd()

# 1. csv불러오기 - 전국문화축제표준데이터.csv 
df = read.csv("전국문화축제표준데이터.csv")

# 2. 데이터재구성 - 축제명,축제시작일자,축제종료일자,소재지도로명주소,경도,위도
df = data.frame(df[1],df[3:4],df[12],df[14:15])
head(df)

# 3. 마지막 경도 위도값의 이름을 각각 LON, LAT으로 변경하기 위하여 열의 갯수확인
cnt = length(df)
cnt
names(df)[cnt]
names(df)[cnt] = "LAT"
names(df)[cnt-1]
names(df)[cnt-1] = "LON"
names(df)[cnt-1]
head(df)

# 4. 위도 경도에 있는 NA값 확인 후 행 삭제
summary(df)  # LON,LAT의 NA: 65
nrow(df)
df = df[complete.cases(df), ] # NA 삭제
nrow(df)
summary(df)

# 5. 빈값 있는 자료 확인 - table로 집계
cnt=4
head(table(df[cnt]))
tail(table(df[cnt]))

# 6. 빈값 있는 자료 확인 - order
head(df[order(df[cnt]), ])
length(df$소재지도로명주소[df$소재지도로명주소 == ""])

# 7. 빈값을 NA로 변경 후 삭제 - 예) 소재지도로명주소 등 삭제
df[df==""] = NA
df[df=="없음"] = NA
df[df=="-"] = NA
summary(df)
df = df[complete.cases(df),]
nrow(df)

# 전체 컬럼에 대해 빈값 등 결측치 처리
cnt=1
head(df[order(df[cnt]), ])
length(df$축제명[df$축제명 == ""])
df[df==""] = NA
df[df=="없음"] = NA
df[df=="-"] = NA
summary(df)
df = df[complete.cases(df),]
nrow(df)

cnt=2
head(df[order(df[cnt]), ])
length(df$축제시작일자[df$축제시작일자 == ""])
df[df==""] = NA
df[df=="없음"] = NA
df[df=="-"] = NA
summary(df)
df = df[complete.cases(df),]
nrow(df)

cnt=3
head(df[order(df[cnt]), ])
length(df$축제종료일자[df$축제종료일자 == ""])
df[df==""] = NA
df[df=="없음"] = NA
df[df=="-"] = NA
summary(df)
df = df[complete.cases(df),]
nrow(df)

cnt=5
head(df[order(df[cnt]), ])
length(df$LON[df$LON == ""])
df[df==""] = NA
df[df=="없음"] = NA
df[df=="-"] = NA
summary(df)
df = df[complete.cases(df),]
nrow(df)

cnt=6
head(df[order(df[cnt]), ])
length(df$LAT[df$LAT == ""])
df[df==""] = NA
df[df=="없음"] = NA
df[df=="-"] = NA
summary(df)
df = df[complete.cases(df),]
nrow(df)

# 8. 축제기간 (일수) 구하기
attach(df)
str(df)  
# 축제시작일자, 종료일자는 계산을 위해서 형변환
df$축제시작일자 = as.Date(df$축제시작일자)
df$축제종료일자 = as.Date(df$축제종료일자)
str(df)
df$gigan = df$축제종료일자 - df$축제시작일자 + 1
df = cbind(df,gigan) # 위와 동일. ~~.1 로 컬럼명이 복사됨
length(df)

df = df[, !(names(df) %in% "gigan.1")]
# df = df[,-c(0, 7)]  # 컬럼 삭제
head(df)

# 9. 축제시작일자가 축제종료일보다 큼 이상치 데이터 있음(-값 나옴)
table(gigan)  # 전체 통계 확인

# 10. gigan이 0보다 큰 값을 df로 재구성 - subset
subset(df, df$축제시작일자 > df$축제종료일자)
subset(df, df$gigan < 0)
df = subset(df, df$gigan >=0)
table(df$gigan)

# 11. if를 이용한 자료 분류
bigo = ifelse(df$gigan > 365, "1년 이상", ifelse(df$gigan >= 50, "50일 이상", ifelse(df$gigan==1, "1일", "50일 미만")))
df = cbind(df, bigo)
head(df)
subset(df, df$gigan >300)

# 12. 패키지를 이용한 년도별, 월별 추출
library(lubridate)
df$mm = month(df$축제시작일자)
table(df$mm)
hist(df$mm)
df$yy = year(df$축제시작일자)
table(df$yy)
hist(df$yy)
df$day_week = wday(df$축제시작일자, label=T)  # label=T : 월~일 문자로 입력됨
table(df$day_week)
plot(df$day_week)
head(df)
dev.new()
plot(df$day_week)
savePlot("day_week_chart", type="png")

# 13. 패키지를 이용한 문자 나누기
library(stringr)
주소 = str_split_fixed(df$소재지도로명주소, " ", 2)
head(주소)
주소 = 주소[,1]
head(주소)
df[4] = 주소
head(df)
colnames(df)[4] = "주소"
head(df)
summary(df$주소)
table(df$주소)  # 요소, 대표 값으로 출력
df$주소 = as.factor(df$주소)  # 요소, 대표 값으로 정리
table(df$gigan)

# 14. 자료 저장 - 축제.csv
write.csv(df, "축제.csv")
df = read.csv("축제.csv")
head(df)

# 12. plot 함수로 선형 그래프 그리기
plot(table(df$yy), type="b", lty=3, col=2, pch=10, lwd=3, cex=3, main="년간 축제 분석", sub="전국(2011~2020", xlab="년도", ylab="횟수", ylim=c(0,800), xlim=c(2017,2020))

# 13. 그래프 배치 재 조정하기
par(mfrow=c(1,3))
plot(table(df$yy), type="b", lty=3, col=2, pch=10, lwd=3, cex=3, main="년간 축제 분석", sub="전국(2011~2020", xlab="년도", ylab="횟수", ylim=c(0,800), xlim=c(2017,2020))
plot(table(df$mm), type = "b", )
plot(df$주소, type="h")
table(df$주소)
par(mfrow=c(1,1))
plot(df$주소, type="h")
abline(h=mean(df$gigan), col="green", lty=2)
table(df$주소)
mean(df$gigan)
boxplot(df$gigan)

# ==========================================================================================================

# 1. csv불러오기 - 등록공연장현황.csv 
df = read.csv("등록공연장현황_2019_0.csv", header=T)

# 2. 데이터재구성 - 시도별, 시군구, 시설명, 개관일자, 공연장면적, 객석수
df = data.frame(df[2:4],df[6],df[8],df[10])
head(df)
names(df)[5] = "공연장면적"
head(df)
str(df)
nrow(df)

# . 과 숫자를 제외한 나머지는 빈문자열로 반환
convNA = function(strings) {
  if (str_detect(strings,'[^.0-9]')) {
    return("")
  } else {
    return(strings)
  }
}

# 개관일자 변환
# .- 등으로 통일되지 않은 날짜 포맷 맞추기
conv0date = function(strings,ptrn) {
  if (str_detect(strings,ptrn)) {
    temp = str_split(strings,ptrn)
    if (nchar(temp[[1]][2]) < 2) {
      # str_split 으로 패턴을 이용해 리스트로 만들수 있으며, 반환되는 리스트의 접근은 [[1]][1] 이 첫번째 인덱스임.
      temp[[1]][2] = paste("0", temp[[1]][2], sep="")
    } else if (nchar(temp[[1]][2]) >= 4) {
      temp2 = paste(temp[[1]][1], temp[[1]][2], sep="")
      return(temp2)
    }
    if (length(temp) > 2) {
      if (nchar(temp[[1]][3]) < 2) {
        temp[[1]][3] = paste("0", temp[[1]][3], sep="")
      }
      temp1 = paste(temp[[1]][2], temp[[1]][3], sep="")  
    } else {
      # 일자가 없고 년월 포맷일 경우 일 부분에 01이 들어가도록 함.
      temp1 = paste(temp[[1]][2], "01", sep="")  
    }
    temp2 = paste(temp[[1]][1], temp1, sep="")
    return(temp2)
  } else {
    return(strings)
  }
}

i=1
nrow(df)
df$개관일자 = as.character(df$개관일자)
for (i in 1:nrow(df)) {
  df$개관일자[i] = conv0date(df$개관일자[i],"[:punct:]")
}
df$개관일자 = str_replace_all(df$개관일자, "\n","")
df$개관일자 = str_replace_all(df$개관일자, " ","")
df$개관일자 = as.Date(df$개관일자, "%Y%m%d")
str(df)
table(df$개관일자)

# 공연장면적
df$공연장면적 = str_replace_all(df$공연장면적,"\\,","")  # , 삭제
df$공연장면적 = str_replace_all(df$공연장면적,"[a-Z가-힣]","") # 알파벳, 한글 삭제
df$공연장면적 = str_replace_all(df$공연장면적,"[\\.][\\S]*","")  # . 이하 삭제
df$공연장면적 = str_replace_all(df$공연장면적,"[\n(][\\S]*","")  # 줄바꿈 및 ( 이후 모든 문자 삭제
df$공연장면적 = str_replace_all(df$공연장면적," ","")
i=1
for (i in 1:nrow(df)) {
  df$공연장면적[i] = convNA(df$공연장면적[i])
}
df$공연장면적 = as.numeric(df$공연장면적)
table(df$공연장면적)
summary(df$공연장면적)

# 객석수
df$객석수 = str_replace_all(df$객석수,"\\,","")  # , 삭제
df$객석수 = str_replace_all(df$객석수,"[a-zA-Z가-힣]","") # 알파벳, 한글 삭제
df$객석수 = str_replace_all(df$객석수,"[\\.][\\S]*","")  # . 이하 삭제
df$객석수 = str_replace_all(df$객석수,"[\n(][\\S]*","")  # 줄바꿈 및 ( 이후 모든 문자 삭제
df$객석수 = str_replace_all(df$객석수," ","")
i=1
for (i in 1:nrow(df)) {
  df$객석수[i] = convNA(df$객석수[i])
}
df$객석수 = as.numeric(df$객석수)
table(df$객석수)
summary(df$객석수)

# 3. 객석수에 있는 NA값 확인 후 행 삭제
length(df$객석수[df$객석수 == ""])

# 4. 빈 값 있는 자료 확인 - table로 집계
# 5. 빈 값을 NA로 변경 후 삭제 - 잘못입력된 날짜, 객석수, 공연장 면적 등 삭제
df[df==" "] = NA
df[df==""] = NA
df[df=="없음"] = NA
df[df=="-"] = NA
summary(df)
df$공연장면적[df$공연장면적=="0"] = NA
df$객석수[df$객석수=="-"] = NA
df = df[complete.cases(df),]
nrow(df)
head(df[order(df[5]), ])


# 6. 공연장 면적별 객석수로 1인당 사용면적량 계산 - 변수명 : person
df$공연장면적 = as.numeric(gsub(",","",df$공연장면적))
df$객석수 = as.numeric(gsub(",","",df$객석수))
person = round(df$공연장면적 / df$객석수, 2)
person
df = cbind(df, person)
df = df[complete.cases(df),]
table(df$person)

# 7. if를 이용한 자료 분류 - 1인당 사용면적량이 큰 순서로 A~D등급 - 변수명 : grade
grade = ifelse(df$person > 10, "A",
               ifelse(df$person > 5, "B",
                      ifelse(df$person > 2, "C", "D")))
df = cbind(df, grade)
head(df)

# 8. 패키지를 이용하여 주소 합치기
주소 = paste(df$시도별, df$시군구, sep=" ")
df = cbind(주소,df)
df$시도별 = NULL
df$시군구 = NULL
head(df)

# 9. 자료 저장 - 공연장.csv
write.csv(df, "공연장현황_변환_2019.csv")

# 10. plot 함수로 선형 그래프 그리기 
boxplot(df$person)
barplot(df$공연장면적, xlim=c(150,1200))

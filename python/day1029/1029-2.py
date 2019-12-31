def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2) #2=> fibo(1)+fibo(0) = 1
    # fibo(4)\fibo(3)[=fibo(2)[=fibo(1)+fibo(0]+fibo(1)]+fibo(2)[=fibo(1)+fibo(0)]
    #= 1+0+1+1+0 = 3

indata = int(input("숫자입력:"))
print("fibo(%d)=>"%(indata), end='')  # 5*4*3*2*1
for i in range(indata): # indata = 5 => 0~4[5번]
    if i==indata-1:
        print('f(%d)' % i + '=' + str(fibo(i)))
    else:
        print('f(%d)'% i+'='+ str(fibo(i))+',', end='')

#위에꺼 함수로하면
#함수를 통한 피보나치 수열 생성
f = []
def fibo(n):
    for i in range(n):
        if i == 0:
            f.append(0)
        elif i == 1:
            f.append(1)
        else:
            f.append(f[i-1]+[i-2])
indata = int(input("숫자입력:"))
print("fibo(%d)=>"%(indata), end='') # 5*4*3*2*1
fibo(indata)
print(f)
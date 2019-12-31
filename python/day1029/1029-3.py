#10진수 입력 받아서 2진수 출력
def dec2bin(n):
    if n==0:
        return
    else:
        dec2bin(n//2)
        print(n%2, end='')
        return

indata= int(input("숫자입력:"))
print("dec(%d)=>bin("%(indata), end='')
dec2bin(indata)
print(')')
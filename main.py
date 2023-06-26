print("Hello World")

num = 100
if (num>100):
    print('100보다 크다')
elif(num<100):
    print('100보다 작다')
else :
    print('100이다.')

hap = 0
for i in range(1,101,1): # i가 1부터 100까지 1씩 증가
    hap +=i
print(hap)

#퀴즈 : while 문으로 바꾸기
hap = 0
i = 1
while(i<101):
    hap +=i
    i +=1
print(hap)
##함수 선언부
def addNumber(i,n):
    sum = 0
    while (i < (n+1)):
        sum += i
        i += 1
    return sum
##전역 변수부
hap = 0
i = 1

## 메인 코드뷰
hap = addNumber(1,100)
print(hap)

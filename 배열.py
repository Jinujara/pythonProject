import random

#함수

#변수
ary1 = []
ary2 = []
#메인
for i in range(0,10,1): # 0부터 10까지 1씩
    ary1.append(0) # ary1 배열에 0 추가
print(ary1)

# 배열에 값 대입, 2부터 짝수를 대입하자.
#num = 2
for i in range(1, 10, 1):
    ary1[i] = random.randint(0,1000)
    #num+= 2
print(ary1)

# for i in range(1,10,1): # 0부터 10까지 1씩
#     ary2.append(2*i) # ary1 배열에 0 추가
# print(ary2)


#배열 처리
sum = 0
# 1. 배열의 값의 합계
for i in range(0,10,1):
    sum += ary1[i]
print("배열의 합 : ",sum)
# 2. 배열 중 홀수만 합계
sum = 0
for i in range(0,10,1):
    if((ary1[i]%2)==1):
        sum +=ary1[i]
print("배열 중 홀수만 합계 : ",sum)


# a += ary1[i] # a = a + ary1[i]

# 사진이 어두우면, 밝기를 높이면되요! 함수가 따로있어요!









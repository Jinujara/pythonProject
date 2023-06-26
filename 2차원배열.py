import random
import os
## 함수

def display():
    ##디스플레이 (화면 출력)
    for i in range(row):
        for j in range(col):
            print("%3d " % image[i][j], end='')
        print()
    print()

def display1():
    ##디스플레이 (화면 출력)
    for i in range(row):
        for j in range(col):
            print("%3d " % image[j+j*i], end='')
        print()
    print()
def getmean():
    hap = 0
    for i in range(row):
        for j in range(col):
            hap += image[i][j]
    return hap/(row*col)
def GetMiddleNum():
    max = 0
    min = 255
    for i in range(row):
        for j in range(col):
            if(image[i][j]>max):
                max =  image[i][j]
            elif(image[i][j]<min):
                min = image[i][j]
    return int((max+min)/2)

def imageto1array():
    image = []
    for i in range(row):
        for j in range(col):
            image.append(image[i][j])


def imageto2array(image):
    image2 = []
    tmp2Ary = []
    for i in range(row):
        for j in range(col):
            image2[j].append(image[j+j*i])
        tmp2Ary.append(image2[j])
        image2 = []
    return tmp2Ary



## 변수
# image = [[0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0]]
row, col = 5,5
image = None

## 메인

## 메모리 할당
image = [ ]
tmpAry = []
for i in range(row):
    for j in range(col):
        tmpAry.append(0) #1차원 배열 tmpAry = [0,0,0,0,0]
    image.append(tmpAry) #tmpAry를 5개 붙임. 즉, 5x5크기의 2차원이 됨.
    tmpAry = []
## 파일 --> 메모리로 로딩(Loading)
for i in range(row):
    for j in range(col):
        pixel = random.randint(0,255) # GaryScale
        image[i][j]= pixel
display()


## 영상 처리



#(1) 영상을 50밝게 처리하자.
for i in range(row):
    for j in range(col):
        if(image[i][j] + 50 > 255) :
            image[i][j] = 255
        else :
            image[i][j] += 50
display()

# 퀴즈 : 100pixel 어둡게
for i in range(row):
    for j in range(col):
        pixel = random.randint(0,255) # GaryScale
        image[i][j]= pixel
display()
for i in range(row):
    for j in range(col):
        if (image[i][j] - 100 <0):
            image[i][j] = 0
        else:
            image[i][j] -= 100
display()


# 퀴즈 : 완전 흑백 처리
for i in range(row):
    for j in range(col):
        pixel = random.randint(0,255) # GaryScale
        image[i][j]= pixel
display()

for i in range(row):
    for j in range(col):
        if (image[i][j] > getmean()):
            image[i][j] = 255
        else:
            image[i][j] = 0
display()

# 퀴즈 : 반전하기
for i in range(row):
    for j in range(col):
        pixel = random.randint(0,255) # GaryScale
        image[i][j]= pixel
display()
for i in range(row):
    for j in range(col):
        image[i][j] = 255-image[i][j]
display()


#중앙값
for i in range(row):
    for j in range(col):
        pixel = random.randint(0,255) # GaryScale
        image[i][j]= pixel

for i in range(row):
    for j in range(col):
        if (image[i][j] > GetMiddleNum()):
            image[i][j] = 255
        else:
            image[i][j] = 0
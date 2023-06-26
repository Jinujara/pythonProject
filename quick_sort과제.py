import random
## 함수
def display(): ##2차원 배열 출력
    ##디스플레이 (화면 출력)
    for i in range(row):
        for j in range(col):
            print("%3d " % image[i][j], end='')
        print()
    print()

def display1(): # 1차원 배열 출력
    ##디스플레이 (화면 출력)
    for i in range(row):
        for j in range(col):
            print("%3d " % image[j+row*i], end='')
        print()
    print()

def imageto1array(image):
    image1 = []
    for i in range(row):
        for j in range(col):
            image1.append(image[i][j])
    return image1

def quick_sort(array, start, end):
    if start >= end: return  # 원소가 1개인 경우
    pivot = start  # 피벗은 첫 요소
    left, right = start + 1, end

    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈린 경우
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않은 경우
            array[right], array[left] = array[left], array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
## 변수
row, col = 5,5
image = None

## 메인
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
image1 = imageto1array(image) #1차원으로 변경
print(image1)
quick_sort(image1,0,24)
print(image1)
image2 = []
tmp2Ary = []
for i in range(row):
    for j in range(col):
        image2.append(image1[j+i*row])
    tmp2Ary.append(image2)
    image2 = [] # 초기화
image = tmp2Ary
display()




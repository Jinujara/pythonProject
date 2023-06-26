##파일을 2가지
#텍스트 파일
#바이너리 파일
import os.path
import math

#함수
def display():
    ##디스플레이 (화면 출력)
    for i in range(100,105,1):
        for j in range(100,105,1):
            print("%3d " % image[i][j], end='')
        print()
    print()


#메인
filename = 'Etc_Raw(squre)\LENA256.RAW'

fSize = os.path.getsize(filename)
height = width = int(math.sqrt(fSize))
print(height,'x',width)

image = [ [0 for _ in range(width)] for _ in range(height)]
#파일 --> 메모리 로딩
rfp = open(filename, 'rb') # read, binary
for i in range(height):
    for j in range(width):
        image[i][j] = ord(rfp.read(1)) #1바이트를 숫자로 바꿔주는 명령어 ord

rfp.close()
display()
#바이너리 파일은 특정 소프트웨어가 필요하다.
#바이너리 코드는 회사 기밀이다...
# 화면 제대로 출력하는거

#반전처리

#문서암호 big@python
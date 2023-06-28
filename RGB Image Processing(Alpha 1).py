## 영상처리 알고리즘 분류
## - 화소점 처리(Pixel Processing)
## 동일영상, 반전, 흑백, 감마, 파라볼라...
# -기하학 처리 ( Geometry Processing)
#     이동,회전,확대,축소, 워핑
# - *화소 영역 처리(Area Processing)
#   블러링, 샤프닝, 경계선 처리, 지문 인식
# 히스토그램 처리(historgram Processing -> 화소점 처리의 일부
#   흑백(평균값, 중앙값), 평활화(Equalization)

import os
import math
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image # 필로우 라이브러리 Image 객체만 사용
import sys
sys.setrecursionlimit(262144)
##함수 부분


##공통함수
def displayImage() :
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    if canvas is not None:
        canvas.destroy()
    checkpixel()
    window.geometry(str(outW+100) + 'x' + str(outH +100))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')

    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for k in range(outW):
            r,g,b = outImage[0][i][k], outImage[1][i][k], outImage[2][i][k]
            tmpString +='#%02x%02x%02x ' %(r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)
    canvas.pack()

def checkpixel():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                if(outImage[rgb][i][k] <0):
                    outImage[rgb][i][k]=0
                elif(outImage[rgb][i][k]>255):
                    outImage[rgb][i][k] =255

def loadImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW

    filename = askopenfilename(parent=window, filetypes=(("그림파일","*.png;*.jpg;*.bmp;*.gif"),("모든 파일","*.*")))
    # 파일 크기 알아내기
    pillow = Image.open(filename)
    inH = pillow.height
    inW = pillow.width

    # 메모리 확보 (영상 크기)
    inImage = [[ [0 for _ in range(inW)] for _ in range(inH)] for _ in range(3)]
    # 파일 --> 메모리 로딩
    pillowRGB = pillow.convert('RGB') #RGB모델로 변경
    for i in range(inH) :
        for k in range(inW) :
            r,g,b = pillowRGB.getpixel((k,i))
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b

    equalImage()

def saveImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.jpg', filetypes=(("JPG파일","*.jpg;*.jpeg"),("모든 파일", "*.*")))

    # 저장할 RGB 이미지 생성
    image = Image.new("RGB", (outW, outH))
    pixel_data = []
    for i in range(outH):
        row_data = []
        for k in range(outW):
            # outImage[i][k]에서 RGB 값을 추출합니다.
            r, g, b = outImage[0][i][k],outImage[1][i][k],outImage[2][i][k]
            pixel_value = (r, g, b)
            row_data.append(pixel_value)
        pixel_data.extend(row_data)
    image.putdata(pixel_data)
    if saveFp:
        image.save(saveFp, format="JPEG")
        saveFp.close()
    messagebox.showinfo('성공', saveFp.name + '으로 저장')

def func_exit():
    exit()
##영상처리 함수 부분
def equalImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    #중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH,outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    # ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][i][k]
        ##################################
    displayImage()

def grayImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    #중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH,outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    # ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(2):
        for i in range(inH):
            for k in range(inW):
                hap = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k]
                outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = hap//3
        ##################################
    displayImage()

def reverseImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    #중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH,outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    # ** 찐 영상처리 알고리즘 ** ##
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = 255-inImage[rgb][i][k]
    ##################################
    displayImage()

def addImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    #중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH,outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    # ** 찐 영상처리 알고리즘 ** ##
    value = askinteger("밝게할 값","기본 0",minvalue =-255, maxvalue= 255)
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if(inImage[rgb][i][k]+value >255):
                    outImage[rgb][i][k] = 255
                elif(inImage[rgb][i][k]+value < 0):
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = inImage[rgb][i][k] + value
    ##################################
    displayImage()

def AvgImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    outH, outW = inH, inW
    for rgb in range(3):
        hap = 0
        for i in range(inH):
            for k in range(inW):
                hap +=inImage[rgb][i][k]
        avg = hap/(inH*inW)
        for i in range(inH):
            for k in range(inW):
                if (inImage[rgb][i][k] > avg):
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = 0
    ##################################
    displayImage()

def StaticImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    outH, outW = inH, inW
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (inImage[rgb][i][k] > 127):
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = 0
    ##################################
    displayImage()

def imageto1array():
    global inImage,inH,inW
    temparray = []
    array = []
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                array.append(inImage[rgb][i][k])
        temparray.append(array)
        array = []
    return temparray # array는 [r,g,b]가 됨. ex) [[255,255,255,255,...],[255,255,255,255,...],[255,255,255,255,...]]

#흑백3-2 : 퀵정렬
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)

#흑백3-3 : 중앙값 반환
def findmedian():
    global inImage,inH,inW
    image3 = []
    image2 = imageto1array()
    print(image2)
    image3.append(quick_sort(image2[0])) # r
    image3.append(quick_sort(image2[1])) # g
    image3.append(quick_sort(image2[2])) # b
    rlength = len(image3[0])
    glength = len(image3[1])
    blength = len(image3[2])
    mid = []
    midnum = 0
    for rgb in range(3):
        length = len(image3[rgb])
        if length % 2 == 1:
            median = image3[length // 2]
        else:
            mid1 = image3[rgb][length // 2]
            mid2 = image3[rgb][length // 2 - 1]
            midnum = (mid1 + mid2) / 2
        mid.append(midnum)
    return mid

def mediumImage():
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    median = findmedian()
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (inImage[rgb][i][k] > median[rgb]):
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = 0
    ##################################
    displayImage()
def gammaImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    outH, outW = inH, inW
    value = askfloat("감마값을 입력하세요.","",minvalue =0.0)
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = int(255 * pow(float(inImage[rgb][i][k]) / 255, value))
     ##################################
    displayImage()

def capparabolaImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    outH, outW = inH, inW
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = int(255*pow(float(inImage[rgb][i][k])/127,2))
    ##################################
    displayImage()

def cupparabolaImage():
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    outH, outW = inH, inW
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = 255- int(255 * pow(float(inImage[rgb][i][k]) / 127, 2))
    ##################################
    displayImage()

def moveImage():
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    # ** 찐 영상처리 알고리즘 ** ##
    xVal = askinteger("X값", "")
    yVal = askinteger("Y값", "")
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if(0<=i+xVal<outH and 0<= k+yVal<outW):
                    outImage[rgb][i+xVal][k+yVal] = inImage[rgb][i][k]
    ##################################
    displayImage()

def zoomOutImage():
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    scale = askinteger("축소배율", "")
    outH, outW = inH//scale, inW//scale
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                    outImage[rgb][i][k] = inImage[rgb][i*scale][k*scale]
    ##################################
    displayImage()
def zoomInImage():
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    scale = askinteger("확대배율", "")
    outH, outW = inH*scale, inW*scale
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                    outImage[rgb][i][k] = inImage[rgb][i//scale][k//scale]
    ##################################
    displayImage()

def rotateImage():
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW

    angle = askinteger("각도", "")
    outH, outW = inH, inW
    # 메모리 할당
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]

    radian = angle * math.pi /180.0 # 세타로 변환 45' * 파이/180
    cX , cY = inH//2, inW//2
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                oldI = int(math.cos(radian)*(i-cX) - math.sin(radian)*(k-cY)) + cX
                oldK = int(math.sin(radian)*(i-cX) + math.cos(radian)*(k-cY)) + cY
                if( 0<=oldI < inH) and (0<=oldK < inW) :
                    outImage[rgb][i][k] = inImage[rgb][oldI][oldK]

    displayImage()

##전역변수 변수선언이 가장중요!
window, canvas, paper = None, None, None
filename = ""
inImage, outImage = None,None
inH, inW, outH, outW = 0,0,0,0

##메인

window = Tk()
window.geometry('300x300')
window.title('영상처리 GrayScale Image Processing (Alpha 1)')

#메뉴 만들기
mainMenu = Menu(window) #메뉴의 틀을 만들기
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label = '열기',command=loadImage)
fileMenu.add_command(label = '저장',command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label = '종료',command=func_exit)

Image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu= Image1Menu)
Image1Menu.add_command(label='동일영상', command=equalImage)
Image1Menu.add_command(label='그레이스케일영상', command=grayImage)
Image1Menu.add_command(label='반전',command=reverseImage)
Image1Menu.add_command(label='밝게/어둡게',command=addImage)
Image1Menu.add_command(label='avg기준 이진화', command = AvgImage)
Image1Menu.add_command(label='127기준 이진화', command = StaticImage)
Image1Menu.add_command(label='중앙값 기준 이진화', command = mediumImage)
Image1Menu.add_command(label='감마 조정', command = gammaImage)
Image1Menu.add_command(label='캡 파라볼라 연산', command = capparabolaImage)
Image1Menu.add_command(label='컵 파라볼라 연산', command = cupparabolaImage)

Image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label = '기하학처리', menu = Image2Menu)
Image2Menu.add_command(label='이동',command=moveImage)
Image2Menu.add_command(label='축소',command=zoomOutImage)
Image2Menu.add_command(label='확대', command = zoomInImage)
Image2Menu.add_command(label='회전', command = rotateImage)

window.mainloop()





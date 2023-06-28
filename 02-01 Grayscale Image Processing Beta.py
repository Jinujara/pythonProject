import os
import math
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
import sys
sys.setrecursionlimit(262144)
##함수 부분


##공통함수
def displayImage() :
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    if canvas is not None:
        canvas.destroy()
    checkpixel()
    window.geometry(str(outH+100) + 'x' + str(outW +100))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outW, width=outW)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')
    # for i in range(outH) :
    #     for k in range(outW) :
    #         r = g = b = outImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for k in range(outW):
            r = g = b = outImage[i][k]
            tmpString +='#%02x%02x%02x ' %(r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)
    canvas.pack()




def checkpixel():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    for i in range(outH):
        for k in range(outH):
            if(outImage[i][k] <0):
                outImage[i][k]=0
            elif(outImage[i][k]>255):
                outImage[i][k] =255

def loadImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW

    filename = askopenfilename(parent=window, filetypes=(("RAW파일","*.RAW"),("모든 파일","*.*")))
    # 파일 크기 알아내기
    fSize = os.path.getsize(filename) # Byte 단위
    inH = inW = int(math.sqrt(fSize))
    # 메모리 확보 (영상 크기)
    inImage = [ [0 for _ in range(inW)] for _ in range(inH)]
    # 파일 --> 메모리 로딩
    rfp = open(filename, 'rb')
    for i in range(inH) :
        for k in range(inW) :
            inImage[i][k] = ord(rfp.read(1))
    rfp.close()
    equalImage()

def saveImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.raw', filetypes=(("RAW파일","*.raw"),("모든 파일", "*.*")))
    import struct
    for i in range(outH):
        for k in range(outW):
            saveFp.write(struct.pack('B',outImage[i][k]))
    saveFp.close()
    messagebox.showinfo('성공', saveFp.name + '으로 저장')

##영상처리 함수 부분
def equalImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    #중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH,outW = inH, inW
    # 메모리 할당
    outImage = [[0 for _ in range(outH)] for _ in range(outW)]
    # ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = inImage[i][k]
    ##################################
    displayImage()

def reverseImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    #중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH,outW = inH, inW
    # 메모리 할당
    outImage = [[0 for _ in range(outH)] for _ in range(outW)]
    # ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255-inImage[i][k]
    ##################################
    displayImage()

def addImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    #중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH,outW = inH, inW
    # 메모리 할당
    outImage = [[0 for _ in range(outH)] for _ in range(outW)]
    # ** 찐 영상처리 알고리즘 ** ##
    value = askinteger("밝게할 값","기본 0",minvalue =-255, maxvalue= 255)
    for i in range(inH):
        for k in range(inW):
            if(inImage[i][k]+value >255):
                outImage[i][k] = 255
            elif(inImage[i][k]+value < 0):
                outImage[i][k] = 0
            else:
                outImage[i][k] = inImage[i][k] + value
    ##################################
    displayImage()
def AvgImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    hap = 0
    outH, outW = inH, inW
    for i in range(inH):
        for j in range(inW):
            hap +=inImage[inH][inW]
    avg = hap/(inH*inW)
    for i in range(inH):
        for k in range(inW):
            if (inImage[i][k] > avg):
                outImage[i][k] = 255
            else:
                outImage[i][k] = 0
    ##################################
    displayImage()
def StaticImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    outH, outW = inH, inW
    for i in range(inH):
        for k in range(inW):
            if (inImage[i][k] > 127):
                outImage[i][k] = 255
            else:
                outImage[i][k] = 0
    ##################################
    displayImage()

def imageto1array(image):
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    outH, outW = inH, inW
    image1 = [ 0 for _ in range(outH*outW)]
    for i in range(inH):
        for k in range(inW):
            image1.append(inImage[i][k])
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

def mediumImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    outH, outW = inH, inW
    image2 = imageto1array(inImage)
    quick_sort(image2, 0, inH * inW - 1)
    mediumNum = image2[int(inH / 2) * int(inW / 2)]
    for i in range(inH):
        for k in range(inW):
            if(inImage[i][k] >mediumNum):
                outImage[i][k] = 255
            else:
                outImage[i][k] = 0
    print(mediumNum)
    ##################################
    displayImage()

def gammaImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    outH, outW = inH, inW
    value = askfloat("감마값을 입력하세요.","0.0~2.0",minvalue =0.0, maxvalue= 2.0)
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = int(255 * pow(float(inImage[i][k]) / 255, value))
     ##################################
    displayImage()

def capparabolaImage():
    global window, canvas, paper, filename, inImage,outImage,inH,inW,outH,outW
    outH, outW = inH, inW
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = int(255*pow(float(inImage[i][k])/127,2))
    ##################################
    displayImage()

def cupparabolaImage():
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    outH, outW = inH, inW
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255- int(255 * pow(float(inImage[i][k]) / 127, 2))
    ##################################
    displayImage()
##전역변수 변수선언이 가장중요!
window, canvas, paper = None, None, None
filename = ""
inImage, outImage = None,None
inH, inW, outH, outW = 0,0,0,0

##메인

window = Tk()
window.geometry('300x300')
window.title('영상처리 GrayScale Image Processing (Beta 1)')

#메뉴 만들기
mainMenu = Menu(window) #메뉴의 틀을 만들기
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label = '열기',command=loadImage)
fileMenu.add_command(label = '저장',command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label = '종료',command=None)

Image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu= Image1Menu)
Image1Menu.add_command(label='동일영상', command=equalImage)
Image1Menu.add_command(label='반전',command=reverseImage)
Image1Menu.add_command(label='밝게/어둡게',command=addImage)
Image1Menu.add_command(label='avg기준 이진화', command = AvgImage)
Image1Menu.add_command(label='127기준 이진화', command = StaticImage)
Image1Menu.add_command(label='중앙값 기준 이진화', command = mediumImage)
Image1Menu.add_command(label='감마 조정', command = gammaImage)
Image1Menu.add_command(label='캡 파라볼라 연산', command = capparabolaImage)
Image1Menu.add_command(label='컵 파라볼라 연산', command = cupparabolaImage)






#displayImage()

window.mainloop()




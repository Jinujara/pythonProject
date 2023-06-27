#빅리더 아카데미 파이썬 기초 A반 과제
#그중에서 심화과제만 합친것.
#감마연산, 파라볼라 연산(cap,cup따로)


import os
from tkinter import *
import math
import sys
sys.setrecursionlimit(262144)

## 함수
def displayImage():
    global window,canvas,paper,height,width,filename
    if canvas is not None:
        canvas.destroy()

    canvas = Canvas(window, height=512, width=512)
    paper = PhotoImage(height=512, width=512)
    canvas.create_image((512 / 2, 512 / 2), image=paper, state='normal')
    checkpixel()
    for i in range(height) :
        for k in range(width) :
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    canvas.pack()

def checkpixel():
    for i in range(height):
        for k in range(width):
            if(image[i][k] <0):
                image[i][k]=0
            elif(image[i][k]>255):
                image[i][k] =255

def gammabtn():
    a = float(input("입력할 감마 값 : "))
    for i in range(height) :
        for k in range(width) :
            image[i][k] = int(255*pow(float(image[i][k])/255,a))
    displayImage()

#캡 파라볼라 연산
def capparabolabtn():
    for i in range(height) :
        for k in range(width) :
            image[i][k] = int(255*pow(float(image[i][k])/127,2))
    displayImage()

#컵 파라볼라 연산
def cupparabolabtn():
    for i in range(height) :
        for k in range(width) :
            image[i][k] = int(255-255*pow(float(image[i][k])/127,2))
    displayImage()

## 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []

## 메인
window = Tk()
window.geometry('700x900')
window.title('영상처리 Alpha')

#버튼 구현
gammabtn = Button(window,text='감마 보정',command=gammabtn)
gammabtn.pack()
capparabolabtn = Button(window,text='캡 파라볼라',command=capparabolabtn)
capparabolabtn.pack()
cupparabolabtn = Button(window,text='컵 파라볼라',command=cupparabolabtn)
cupparabolabtn.pack()

#파일 불러오기
filename = 'newjeans.RAW'
# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
print("파일크기 : " ,height,width)

image = [ [0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1))

rfp.close()
displayImage()



window.mainloop()
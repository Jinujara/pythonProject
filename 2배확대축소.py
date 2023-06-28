#2배 확대

import os
from tkinter import *
import math
import sys
sys.setrecursionlimit(262144)


def displayImage(image,height, width):
    global window,canvas,paper,filename

    window.geometry(str(width+200)+'x'+str(height+200))
    if canvas is not None:
        canvas.destroy()

    canvas = Canvas(window, height=height, width=width)
    paper = PhotoImage(height=height, width=width)
    canvas.create_image((width / 2, height / 2), image=paper, state='normal')
    checkpixel()
    for i in range(height) :
        for k in range(width) :
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i)) # 02x : 16진수 2자리로 표현
    canvas.pack()
def imageto2array(h,y):
    image2 = []
    tmp2Ary = []
    for i in range(y):
        for j in range(h):
            image2.append(0)
        tmp2Ary.append(image2)
        image2 = []
    return tmp2Ary

def checkpixel():
    for i in range(height):
        for k in range(width):
            if(image[i][k] <0):
                image[i][k]=0
            elif(image[i][k]>255):
                image[i][k] =255

def mul2btn():
    global image
    newH = int(height*2)
    newW = int(width*2)
    tempImage = imageto2array(newH,newW)
    for i in range(newH) :
        for k in range(newW) :
            tempImage[i][k] = image[int(i/2)][int(k/2)]

    displayImage(tempImage,newH,newW)


def div2btn():
    global image
    newH = int(height/2)
    newW = int(width/2)
    tempImage = imageto2array(newH,newW)
    for i in range(newH) :
        for k in range(newW) :
            tempImage[i][k] = image[i*2][k*2]

    displayImage(tempImage,newH,newW)

#변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []

#메인
window = Tk()
window.geometry('700x900')
window.title('영상처리 Alpha')

mul2btn = Button(window,text='2배 확대',command=mul2btn)
mul2btn.pack()

div2btn = Button(window,text='2배 축소',command=div2btn)
div2btn.pack()

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
displayImage(image,height,width)

window.mainloop()


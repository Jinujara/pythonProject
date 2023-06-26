import math
import os
from tkinter import *
from tkinter import messagebox
## 함수
def displayImage() :
    global window,canvas,paper,height,width,filename
    if canvas is not None:
        canvas.destroy()

    canvas = Canvas(window, height=256, width=256)
    paper = PhotoImage(height=256, width=256)
    canvas.create_image((256 / 2, 256 / 2), image=paper, state='normal')

    for i in range(height) :
        for k in range(width) :
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    canvas.pack()
def  reverseImage() :
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]

    displayImage()
## 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []

## 메인
window = Tk()
window.geometry('300x300')
window.title('영상처리 Alpha')


#button1 = Button(window, text='밝게',command = brighter)
#button2 = Button(window, text='어둡게',command = darker)

btmReverse = Button(window, text = '반전', command = reverseImage)
btmReverse.pack()



filename = 'Etc_Raw(squre)\LENA256.RAW'
# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1))

rfp.close()

displayImage()


window.mainloop()


#밝게하기 버튼
#어둡게 하기 버튼
#흑백(127기준)
#흑백(평균)

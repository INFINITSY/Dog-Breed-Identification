# -*- coding: utf-8 -*-
"""
Created on Sun Fib 25 20:13:24 2018

@author: Liu Jiguang
"""
from PIL import Image, ImageTk
from test_model import compute_and_return
import tkinter as tk
import tkinter.filedialog

#GUI整体框架
pathVariable = 'person.jpg'
g_path = 'person.jpg'
window = tk.Tk()
window.title("行人重识别系统")
window.geometry('1110x580')

#选择本地图片的函数
def SelectPath():
	
		#获得图片地址
    global g_path
    g_path = tk.filedialog.askopenfilename()
    path.set(g_path)

		#替换目标图片
    global pathVariable
    pathVariable = g_path
    global g_img1
    g_img1 = Image.open(pathVariable)
    g_img1 = g_img1.resize((120, 240), Image.ANTIALIAS)
    global g_photo1
    g_photo1 = ImageTk.PhotoImage(g_img1)
    g_imgLabel1.configure(image=g_photo1)  

#计算的函数
def Compute():

		#传入本地图片地址并获取计算结果
    global result
    result = compute_and_return(g_path)

		#替换目标图片
    global g_img2
    g_img2 = Image.open(result[0])
    g_img2 = g_img2.resize((120, 240), Image.ANTIALIAS)
    global g_photo2
    g_photo2 = ImageTk.PhotoImage(g_img2)
    g_imgLabel2.configure(image=g_photo2)

    global g_img3
    g_img3 = Image.open(result[1])
    g_img3 = g_img3.resize((120, 240), Image.ANTIALIAS)
    global g_photo3
    g_photo3 = ImageTk.PhotoImage(g_img3)
    g_imgLabel3.configure(image=g_photo3)

    global g_img4
    g_img4 = Image.open(result[2])
    g_img4 = g_img4.resize((120, 240), Image.ANTIALIAS)
    global g_photo4
    g_photo4 = ImageTk.PhotoImage(g_img4)
    g_imgLabel4.configure(image=g_photo4)

    global g_img5
    g_img5 = Image.open(result[3])
    g_img5 = g_img2.resize((120, 240), Image.ANTIALIAS)
    global g_photo5
    g_photo5 = ImageTk.PhotoImage(g_img5)
    g_imgLabel5.configure(image=g_photo5)

    global g_img6
    g_img6 = Image.open(result[4])
    g_img6 = g_img6.resize((120, 240), Image.ANTIALIAS)
    global g_photo6
    g_photo6 = ImageTk.PhotoImage(g_img6)
    g_imgLabel6.configure(image=g_photo6)

    global g_img7
    g_img7 = Image.open(result[5])
    g_img7 = g_img7.resize((120, 240), Image.ANTIALIAS)
    global g_photo7
    g_photo7 = ImageTk.PhotoImage(g_img7)
    g_imgLabel7.configure(image=g_photo7)

    global g_img8
    g_img8 = Image.open(result[6])
    g_img8 = g_img8.resize((120, 240), Image.ANTIALIAS)
    global g_photo8
    g_photo8 = ImageTk.PhotoImage(g_img8)
    g_imgLabel8.configure(image=g_photo8)

    global g_img9
    g_img9 = Image.open(result[7])
    g_img9 = g_img9.resize((120, 240), Image.ANTIALIAS)
    global g_photo9
    g_photo9 = ImageTk.PhotoImage(g_img9)
    g_imgLabel9.configure(image=g_photo9)

    global g_img10
    g_img10 = Image.open(result[8])
    g_img10 = g_img10.resize((120, 240), Image.ANTIALIAS)
    global g_photo10
    g_photo10 = ImageTk.PhotoImage(g_img10)
    g_imgLabel10.configure(image=g_photo10)

    global g_img11
    g_img11 = Image.open(result[9])
    g_img11 = g_img11.resize((120, 240), Image.ANTIALIAS)
    global g_photo11
    g_photo11 = ImageTk.PhotoImage(g_img11)
    g_imgLabel11.configure(image=g_photo11)

    global g_img12
    g_img12 = Image.open(result[10])
    g_img12 = g_img12.resize((120, 240), Image.ANTIALIAS)
    global g_photo12
    g_photo12 = ImageTk.PhotoImage(g_img12)
    g_imgLabel12.configure(image=g_photo12)

    global g_img13
    g_img13 = Image.open(result[11])
    g_img13 = g_img13.resize((120, 240), Image.ANTIALIAS)
    global g_photo13
    g_photo13 = ImageTk.PhotoImage(g_img13)
    g_imgLabel13.configure(image=g_photo13)

    global g_img14
    g_img14 = Image.open(result[12])
    g_img14 = g_img14.resize((120, 240), Image.ANTIALIAS)
    global g_photo14
    g_photo14 = ImageTk.PhotoImage(g_img14)
    g_imgLabel14.configure(image=g_photo14)

    global g_img15
    g_img15 = Image.open(result[13])
    g_img15 = g_img15.resize((120, 240), Image.ANTIALIAS)
    global g_photo15
    g_photo15 = ImageTk.PhotoImage(g_img15)
    g_imgLabel15.configure(image=g_photo15)

    global g_img16
    g_img16 = Image.open(result[14])
    g_img16 = g_img16.resize((120, 240), Image.ANTIALIAS)
    global g_photo16
    g_photo16 = ImageTk.PhotoImage(g_img16)
    g_imgLabel16.configure(image=g_photo16)


path = tk.StringVar()

#声明GUI各部件并排好位置
l1 = tk.Label(window, text="目标路径:", width=10, height=2).grid(row=0, column=0)
e = tk.Entry(window, textvariable=path, width=80).grid(row=0, column=1, columnspan=5)
b1 = tk.Button(window, text="路径选择", command=SelectPath).grid(row=0, column=6)
b2 = tk.Button(window, text="Compute", command=Compute).grid(row=0, column=7)

g_img1 = Image.open('qiep_01.jpg')
g_img1 = g_img1.resize((120, 240), Image.ANTIALIAS)

# 用PIL模块的PhotoImage打开
g_photo1 = ImageTk.PhotoImage(g_img1)
g_imgLabel1 = tk.Label(window, image=g_photo1, width=120, height=240)
g_imgLabel1.grid(row=1, column=0)
acc1 = tk.Label(window, text=
"搜索目标")
acc1.grid(row=2, column=0)

g_img2 = Image.open('qiep_02.jpg')
g_img2 = g_img2.resize((120, 240), Image.ANTIALIAS)
g_photo2 = ImageTk.PhotoImage(g_img2)
g_imgLabel2 = tk.Label(window, image=g_photo2, width=120, height=240)
g_imgLabel2.grid(row=1, column=1)

g_img3 = Image.open('qiep_03.jpg')
g_img3 = g_img3.resize((120, 240), Image.ANTIALIAS)
g_photo3 = ImageTk.PhotoImage(g_img3)
g_imgLabel3 = tk.Label(window, image=g_photo3, width=120, height=240)
g_imgLabel3.grid(row=1, column=2)

g_img4 = Image.open('qiep_04.jpg')
g_img4 = g_img4.resize((120, 240), Image.ANTIALIAS)
g_photo4 = ImageTk.PhotoImage(g_img4)
g_imgLabel4 = tk.Label(window, image=g_photo4, width=120, height=240)
g_imgLabel4.grid(row=1, column=3)

g_img5 = Image.open('qiep_05.jpg')
g_img5 = g_img5.resize((120, 240), Image.ANTIALIAS)
g_photo5 = ImageTk.PhotoImage(g_img5)
g_imgLabel5 = tk.Label(window, image=g_photo5, width=120, height=240)
g_imgLabel5.grid(row=1, column=4)

g_img6 = Image.open('qiep_06.jpg')
g_img6 = g_img6.resize((120, 240), Image.ANTIALIAS)
g_photo6 = ImageTk.PhotoImage(g_img6)
g_imgLabel6 = tk.Label(window, image=g_photo6, width=120, height=240)
g_imgLabel6.grid(row=1, column=5)

g_img7 = Image.open('qiep_07.jpg')
g_img7 = g_img7.resize((120, 240), Image.ANTIALIAS)
g_photo7 = ImageTk.PhotoImage(g_img7)
g_imgLabel7 = tk.Label(window, image=g_photo7, width=120, height=240)
g_imgLabel7.grid(row=1, column=6)

g_img8 = Image.open('qiep_08.jpg')
g_img8 = g_img8.resize((120, 240), Image.ANTIALIAS)
g_photo8 = ImageTk.PhotoImage(g_img8)
g_imgLabel8 = tk.Label(window, image=g_photo8, width=120, height=240)
g_imgLabel8.grid(row=1, column=7)

g_img9 = Image.open('qiep_09.jpg')
g_img9 = g_img9.resize((120, 240), Image.ANTIALIAS)
g_photo9 = ImageTk.PhotoImage(g_img9)
g_imgLabel9 = tk.Label(window, image=g_photo9, width=120, height=240)
g_imgLabel9.grid(row=3, column=0)

g_img10 = Image.open('qiep_10.jpg')
g_img10 = g_img10.resize((120, 240), Image.ANTIALIAS)
g_photo10 = ImageTk.PhotoImage(g_img10)
g_imgLabel10 = tk.Label(window, image=g_photo10, width=120, height=240)
g_imgLabel10.grid(row=3, column=1)

g_img11 = Image.open('qiep_11.jpg')
g_img11 = g_img11.resize((120, 240), Image.ANTIALIAS)
g_photo11 = ImageTk.PhotoImage(g_img11)
g_imgLabel11 = tk.Label(window, image=g_photo11, width=120, height=240)
g_imgLabel11.grid(row=3, column=2)

g_img12 = Image.open('qiep_12.jpg')
g_img12 = g_img12.resize((120, 240), Image.ANTIALIAS)
g_photo12 = ImageTk.PhotoImage(g_img12)
g_imgLabel12 = tk.Label(window, image=g_photo12, width=120, height=240)
g_imgLabel12.grid(row=3, column=3)

g_img13 = Image.open('qiep_13.jpg')
g_img13 = g_img13.resize((120, 240), Image.ANTIALIAS)
g_photo13 = ImageTk.PhotoImage(g_img13)
g_imgLabel13 = tk.Label(window, image=g_photo13, width=120, height=240)
g_imgLabel13.grid(row=3, column=4)

g_img14 = Image.open('qiep_14.jpg')
g_img14 = g_img14.resize((120, 240), Image.ANTIALIAS)
g_photo14 = ImageTk.PhotoImage(g_img14)
g_imgLabel14 = tk.Label(window, image=g_photo14, width=120, height=240)
g_imgLabel14.grid(row=3, column=5)

g_img15 = Image.open('qiep_15.jpg')
g_img15 = g_img15.resize((120, 240), Image.ANTIALIAS)
g_photo15 = ImageTk.PhotoImage(g_img15)
g_imgLabel15 = tk.Label(window, image=g_photo15, width=120, height=240)
g_imgLabel15.grid(row=3, column=6)

g_img16 = Image.open('qiep_16.jpg')
g_img16 = g_img16.resize((120, 240), Image.ANTIALIAS)
g_photo16 = ImageTk.PhotoImage(g_img16)
g_imgLabel16 = tk.Label(window, image=g_photo16, width=120, height=240)
g_imgLabel16.grid(row=3, column=7)

window.mainloop()

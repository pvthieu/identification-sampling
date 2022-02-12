import os 
import cv2
import time
import tkinter
import datetime
import PIL.Image, PIL.ImageTk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from time import sleep
# from threading import Thread

window = Tk()    
window.title("Lay mau")
window.geometry("900x500")
# read camera
webcam_0 = cv2.VideoCapture(0)  
canvas_w = webcam_0.get(cv2.CAP_PROP_FRAME_WIDTH)//2
canvas_h = webcam_0.get(cv2.CAP_PROP_FRAME_HEIGHT)//2
canvas = Canvas(window, width = canvas_w, height= canvas_h)
canvas.pack()
lbl = tkinter.Label(window, text="  *** HELLO! XIN MỜI BẠN NHẬP THÔNG TIN TẠI ĐÂY ***", fg="green", font=("Arial", 20))
lbl.pack()
bw = 0
photo = None
# show camera để cân chỉnh chân dung
def show(): 
    global canvas, photo, bw
    ret_0, image_0 = webcam_0.read()
    frame = cv2.resize(image_0, dsize=None, fx=0.5, fy=0.5)
    bw=0
    if bw==0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    # Show

    canvas.create_image(0,0, image = photo, anchor=tkinter.NW)
    window.after(1, show)
show()
def chup_hinh():
    name = txt_name.get()
    id_nv = txt_id.get()
    time_sleep = 1
    if len(name) and len(id_nv) !=0:
        os.mkdir('{}_{}'.format(name,id_nv))
        webcam_1 = cv2.VideoCapture(1)
        webcam_2 = cv2.VideoCapture(2)
        # set webcam 1        
        webcam_1.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        webcam_1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        webcam_1.set(cv2.CAP_PROP_FPS, 50)
        # set webcam 2
        webcam_2.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        webcam_2.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        webcam_2.set(cv2.CAP_PROP_FPS, 50)
        for i in range(10):
            ret_1, image_1 = webcam_1.read()
            ret_2, image_2 = webcam_2.read()
            path = './{}_{}'.format(name,id_nv)
            cv2.imwrite(os.path.join(path ,'Cam1_{}_{}_{}.jpg'.format(name,id_nv,str(i))), image_1)
            time.sleep(time_sleep)
            cv2.imwrite(os.path.join(path ,'Cam2_{}_{}_{}.jpg'.format(name,id_nv,str(i))), image_2)
        load1 = tkinter.Label(window, text="CHỤP XONG__CẢM ƠN ",fg="red", font=("Arial", 20))
        load1.pack()
    else:
        error = tkinter.Label(window, text="NHẬP SAI XIN MỜI NHẬP LẠI!",fg="red", font=("Arial", 20))
        error.pack()
# kích thước của ô điền thông tin
Button_name = tkinter.Label(window, text="TEN CUA BAN")
Button_name.pack()
txt_name = Entry(window, width=50)
txt_name.pack()
Button_id = tkinter.Label(window, text="ID CUA BAN")
Button_id.pack()
txt_id = Entry(window, width=20)
txt_id.pack()
Button = Button(window, text="CHỤP", command=chup_hinh)
Button.pack()
window.mainloop()

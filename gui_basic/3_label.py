from email.mime import image
from re import T
from stat import FILE_ATTRIBUTE_ARCHIVE
from tkinter import *

root = Tk()
root.title("Suha GUI")

label1= Label(root,text="안녕하세요")
label1.pack()

root.geometry("640x480+400+150")

photo =PhotoImage(file ="gui_basic/image.png")
label2 = Label(root,image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요 ")
    # 전역변수 선언 유의 
    global photo2
    photo2= PhotoImage(file ="gui_basic/image2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭",command=change)
btn.pack()

root.mainloop()

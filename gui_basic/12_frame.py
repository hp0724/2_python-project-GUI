from cgitb import text
import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()
root.title("Suha GUI")
#root.geometry("640x480")#가로 *세로
root.geometry("640x480+400+150")#가로 *세로 +x좌표 +y좌표

Label(root, text="메뉴를 선택해 주세요 ").pack(side="top")

Button(root,text="주문하기").pack(side="botto")

#버거프레임 
frame_burger=Frame(root, relief="solid",bd=1)
frame_burger.pack(side="left",fill="both",expand=True)

Button(frame_burger,text="햄버거").pack()
Button(frame_burger,text="치즈햄버거").pack()
Button(frame_burger,text="불고기햄버거").pack()

# 음료 프레임 
frame_drink=LabelFrame(root,text="음료")

frame_drink.pack(side="right",fill="both",expand=True)
Button(frame_drink,text="콜라").pack()
Button(frame_drink,text="사이다").pack()

 
 
root.mainloop()
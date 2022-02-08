from msilib.schema import CheckBox
from tkinter import *

from numpy import insert

root = Tk()
root.title("Suha GUI")
#root.geometry("640x480")#가로 *세로
root.geometry("640x480+400+150")#가로 *세로 +x좌표 +y좌표

Label(root,text="메뉴를 선택하세요 ").pack()

burger_var = IntVar()# 여기에 int 형으로 값을 저장 
btn_burger1=Radiobutton(root,text="햄버거",value=1,variable=burger_var)
btn_burger1.select()
btn_burger2=Radiobutton(root,text="치즈버거",value=2,variable=burger_var)
btn_burger3=Radiobutton(root,text="치킨버거",value=3,variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root,text="음료를 선택하세요 ").pack()


drink_var=StringVar() #여기에 string 형으로 값을 저장 
btn_drink1 =Radiobutton(root,text="콜라",value="콜라",variable=drink_var)
btn_drink1.select()
btn_drink2 =Radiobutton(root,text="사이다",value="사이다",variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())# 햄버거 중 선택된   항목 반환 
    print(drink_var.get())# 음료 중 선택된   항목 반환 




btn=Button(root, text="주문",command=btncmd)
btn.pack()

 
root.mainloop()
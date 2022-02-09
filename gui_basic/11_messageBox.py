import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()
root.title("Suha GUI")
#root.geometry("640x480")#가로 *세로
root.geometry("640x480+400+150")#가로 *세로 +x좌표 +y좌표

# 기차 예매 시스템 
def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다 .")

def error():
    msgbox.showerror("에러","결제 오류가 발생했습니다.")

def okCancel():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아 동반석입니다 예매하시겠습니까?")

def retryCancel():
    response =msgbox.askretrycancel("재시도 / 취소","일시적인 오류 입니다")

    if response == 1 : #재시도 ok
        print("재시도")
    
    else : #취소 
        print("취소 ")
def yesno():
    msgbox.askyesno("예 / 아니오","해당 좌석은 역방향입니다 , 예매하시겠습니까?")

def yesnoCancel():
    response=msgbox.askyesnocancel(title=None,message="예매 내역이 저장되지 않았습니다. \n저장후 프로그램을 종료 하시겠습니까?")
    #네 :저장 후 종료
    #아니오 : 저장 하지 않고 종료 
    #취소 : 프로그램 종료 취소
    print("응답:",response) #True,False ,None  -> 예 1 아니오 0, 그외
    if response == 1 : #네 ok
        print("예")
    elif response==0 : #아니오 
        print("아니오 ")
    else : 
        print("취소 ")

Button(root, command=info,text="알림").pack()
Button(root, command=warn,text="경고").pack()
Button(root, command=error,text="에러").pack()
Button(root, command=okCancel,text="확인 취소").pack()
Button(root, command=retryCancel,text="재시도 취소").pack()
Button(root, command=yesno,text="예 아니오").pack()
Button(root, command=yesnoCancel,text="예 아니오 취소" ).pack()


 
 
root.mainloop()
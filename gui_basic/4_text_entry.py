from tkinter import *

root = Tk()
root.title("Suha GUI")
#root.geometry("640x480")#가로 *세로
root.geometry("640x480+400+150")#가로 *세로 +x좌표 +y좌표

txt =Text(root,width=30,height=5)
txt.pack()

txt.insert(END,"글자를 입력하세요")
# 한줄 입력받기 
e =Entry(root,width=30)
e.pack()
e.insert(0,"한 줄만 입력해요 ")

def btncmd():
    #내용 출력 
    print(txt.get("1.0",END)) # 1은 첫번쨰라인 , 0: 0번쨰 COLUMN 위치
    print(e.get())
    
    #내용 삭제 
    txt.delete("1.0",END)
    e.delete(0,END)


btn=Button(root, text="클릭",command=btncmd)
btn.pack()

 
root.mainloop()
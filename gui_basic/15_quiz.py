# 메뉴 :파일 편집 서식 보기 도움말 
# 실제 메뉴 : 메뉴 내에서 열기 ,저장 ,끝내기 
# 열기: mynote.txt 파일 내용 열어서 보여주기 
# 저장: mynote.txt 파일에 현재 내용 저장 
# 끝내기 프로그램 종료 
from fileinput import filename
import os 
from cmath import exp
from tkinter import *

root = Tk()
root.title("제목 없음 -windows 메모장")
#root.geometry("640x480")#가로 *세로
root.geometry("640x480+400+150")#가로 *세로 +x좌표 +y좌표

fileName= "mynote.txt"

def open_file():
    if os.path.isfile(fileName): # 파일 있으면 true 없으면 false 
        with open(fileName,"r",encoding="utf8") as file:
            txt.delete("1.0",END)#텍스트 위젯 본문 삭제
            txt.insert(END,file.read()) # 파일내용을 본문에 입력 
    

def save_file():
    with open(fileName,"w",encoding="utf8")as file:
        file.write(txt.get("1.0",END))#모든 내용을 가져와서 저장 
menu =Menu(root)

menu_file =Menu(menu,tearoff=0)
menu_file.add_command(label="열기",command=open_file)
menu_file.add_command(label="저장",command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기",command=root.quit)
menu.add_cascade(label="파일",menu=menu_file)

#편집 서식 보기 도움말 
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바 
scrollBar= Scrollbar(root)
scrollBar.pack(side="right",fill="y")



# 본문 영역 
txt =Text(root,yscrollcommand=scrollBar.set)
txt.pack(side="left",fill="both",expand=True)

scrollBar.config(command=txt.yview)
root.config(menu=menu)
# 창이 닫히지 않게 하는것 
root.mainloop()

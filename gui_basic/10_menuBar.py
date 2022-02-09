 
from tkinter import *


root = Tk()
root.title("Suha GUI")
#root.geometry("640x480")#가로 *세로
root.geometry("640x480+400+150")#가로 *세로 +x좌표 +y좌표

def create_new_file():
    print("새 파일을 만듭니다.")
menu =Menu(root)

# File 메뉴 
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New File",command=create_new_file)
menu_file.add_command(label="New Window",command=create_new_file)
menu_file.add_separator() # 줄 긋는 구분자 
menu_file.add_command(labe="Open File..")
menu_file.add_separator() 
menu_file.add_command(labe="Save All",state="disable") #비활성화 
menu_file.add_separator()
menu_file.add_command(labe="Exit",command=root.quit) # 
menu.add_cascade(label="File",menu=menu_file)

# edit 메뉴 (빈 값 )
menu .add_cascade(label="Edit")

# language 메뉴 추가 (radio 버튼을 통해서 택 1)
menu_lang = Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="java")
menu_lang.add_radiobutton(label="c++")
menu.add_cascade(label="Language",menu=menu_lang)


#view 메뉴 
menu_view =Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="view",menu=menu_view)

root.config(menu=menu) 
root.mainloop()
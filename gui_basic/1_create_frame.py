from tkinter import *

root = Tk()
root.title("Suha GUI")
#root.geometry("640x480")#가로 *세로
root.geometry("640x480+400+150")#가로 *세로 +x좌표 +y좌표

root.resizable(False,FALSE)# X(너비) Y(높이) 변경불가 
 

# 창이 닫히지 않게 하는것 
root.mainloop()

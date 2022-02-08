import time 
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("Suha GUI")
#root.geometry("640x480")#가로 *세로
root.geometry("640x480+400+150")#가로 *세로 +x좌표 +y좌표

#progressBar=ttk.Progressbar(root,maximum=100,mode="indeterminate")
# progressBar=ttk.Progressbar(root,maximum=100,mode="determinate")
# progressBar.start(10) # 10 ms 마다 움직임 
# progressBar.pack()
 
# def btncmd():
#     progressBar.stop() #작동 중지 
     

# btn=Button(root, text="중지",command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 소수점 까지 간으 
progressBar2=ttk.Progressbar(root,maximum=100,length=150,variable=p_var2)
progressBar2.pack()



def btncmd2():
    for i in range(1,101): # 1 부터 100 까지  
        time.sleep(0.01) # 0.01 초 대기 

        p_var2.set(i) # progress bar 의 값 설정 
        progressBar2.update() # ui update 
        print(p_var2.get())

btn=Button(root, text="시작",command=btncmd2)
btn.pack()
 
root.mainloop()
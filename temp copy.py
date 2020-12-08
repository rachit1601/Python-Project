from tkinter import *

t=0

def set_timer():
    global t 
    if t > 0 :
        L1.config(text=t)
        t=t-1
        L1.after(1000,countdown)
    elif t==0:
        print("end")
        L1.config(text="Times up!")
        
root = Tk()
root.geometry("200x150")
L1 = Label(root , font="ariel")
L1.grid(row=1,column=2)

times=StringVar()
entry1=Entry(root,textvariable=times)
entry1.grid(row=3,column=2)

b1=Button(root,text="SET" , width=20 , command=set_timer)
b1.grid(row=4,column=2,padx=20)

b2=Button(root,text="START" , width=20 , command=countdown)
b2.grid(row=6,column=2,padx=20)

root.mainloop()

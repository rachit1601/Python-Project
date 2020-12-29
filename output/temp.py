from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as tmsg
import json
import urllib.request
import random
url = 'https://opentdb.com/api.php?amount=15&category=18&type=multiple'
data = urllib.request.urlopen(url).read().decode()
obj = json.loads(data)
score=0
count = 1
def raise_frame(frame):
    frame.tkraise()

def score_calc():
    global score
    global count
    global response
    
    coranswer=obj["results"][count-1]['correct_answer'].replace('&#039;', '\'').replace('&quot;', '\"')
    if answerlist[count-1].get() == obj["results"][count-1]['correct_answer']:
        score = score+1
        print(score)
        tmsg.showinfo("Response", " Correct")
    else:
      print("score not increased")
      tmsg.showinfo("Response", f'Wrong \n The correct answer was {coranswer}')
    c=-1
    for i in (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
        if c < count:            
            raise_frame(i)
            c=c+1
    
    count=count+1 
    response = StringVar()
    progress['value'] += 6.6666
def change_theme():
    home.config(theme="equilux")

home = ThemedTk(theme="equilux")
#positionRight = int(home.winfo_screenwidth()/2 - 733/2)
#positionDown = int(home.winfo_screenheight()/2 - 434/2)
#home.geometry("733x434+{}+{}".format(positionRight, positionDown))
home.iconbitmap("logo.ico")
#home.resizable(False, False)

#frames
intro= ttk.Frame(home)
q1=ttk.Frame(home)
q2=ttk.Frame(home)
q3=ttk.Frame(home)
q4=ttk.Frame(home)
q5=ttk.Frame(home)
q6=ttk.Frame(home)
q7=ttk.Frame(home)
q8=ttk.Frame(home)
q9=ttk.Frame(home)
q10=ttk.Frame(home)
q11=ttk.Frame(home)
q12=ttk.Frame(home)
q13=ttk.Frame(home)
q14=ttk.Frame(home)
q15=ttk.Frame(home)

#frame assignment
for frame in (intro, q1, q2, q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
    frame.grid(row=0, column=0, sticky='news', padx=195)

status=ttk.Label(home,text='Hello',relief=SUNKEN)
status.grid(row=1, column=0, sticky='news')

progress=ttk.Progressbar(home, orient=HORIZONTAL, length=300, mode = 'determinate')
progress.grid(row=3, column=0, sticky='news')
#home page
photo=PhotoImage(file="quiz.png")
pic=Label(intro, image=photo, borderwidth=0).pack()
start_img=PhotoImage(file='start.png')
Button(intro, image=start_img,command=lambda:raise_frame(q1) ,borderwidth=0 ).pack(side='bottom')
Button(intro, text='Change Theme',command=lambda:change_theme ).pack(side='bottom')



#question list maker
questions_list=[]
for i in range (15):
    qtemp=obj["results"][i]['question']
    qnew=qtemp.replace('&#039;', '\'').replace('&quot;', '\"')
    questions_list.append('Q'+str(i+1)+' '+qnew)


#question labels in diff. frames
j=0
for i in (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
    question=ttk.Label(i, text=questions_list[j], font='lucida 20 bold' , wraplength=400).pack()
    j=j+1


 
#options list 
new_list=[]
for i in range(15):
    opt_list=[]
    opt_list.append(obj["results"][i]['correct_answer'])
    opt_list.extend(obj["results"][i]['incorrect_answers'])
    random.shuffle(opt_list)
    new_list.append(opt_list)
response = StringVar()


#variables of answers
ans1 = StringVar()
ans2 = StringVar()
ans3 = StringVar()
ans4 = StringVar()
ans5 = StringVar()
ans6 = StringVar()
ans7 = StringVar()
ans8 = StringVar()
ans9 = StringVar()
ans10 = StringVar()
ans11 = StringVar()
ans12 = StringVar()
ans13 = StringVar()
ans14 = StringVar()
ans15 = StringVar()
#answer variable list
answerlist=[ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10,ans11,ans12,ans13,ans14,ans15]



#option radio buttons
noq=0
for q in (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
    options= ttk.Radiobutton(q, text= new_list[noq][0].replace('&#039;', '\'').replace('&quot;', '\"'),variable=answerlist[noq],value=new_list[noq][0]).pack(pady=10)
    options= ttk.Radiobutton(q, text= new_list[noq][1].replace('&#039;', '\'').replace('&quot;', '\"'),variable=answerlist[noq],value=new_list[noq][1]).pack(pady=10)
    options= ttk.Radiobutton(q, text= new_list[noq][2].replace('&#039;', '\'').replace('&quot;', '\"'),variable=answerlist[noq],value=new_list[noq][2]).pack(pady=10)
    options= ttk.Radiobutton(q, text= new_list[noq][3].replace('&#039;', '\'').replace('&quot;', '\"'),variable=answerlist[noq],value=new_list[noq][3]).pack(pady=10)
    noq=noq+1
    
#Submit Buttom
for j in (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
    Button(j, image=start_img, bg='grey',activebackground='grey' ,command=lambda:score_calc() ,borderwidth=0 ).pack(side='bottom', pady=10)
    
        
#print(questions_list)
raise_frame(intro)
#home.config(theme='equilux')
home.mainloop()
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as tmsg
import json
import urllib.request
import random
import pygame
import html
import math

pygame.mixer.init()

print ('Loading....')
themetxt= open('theme.txt','r')
home = ThemedTk(theme=f'{themetxt.read()}')
home.title('Quiz')




url_list=['https://opentdb.com/api.php?amount=15&type=multiple','https://opentdb.com/api.php?amount=15&category=18&type=multiple','https://opentdb.com/api.php?amount=15&category=9&type=multiple','https://opentdb.com/api.php?amount=15&category=10&type=multiple','https://opentdb.com/api.php?amount=15&category=12&type=multiple','https://opentdb.com/api.php?amount=15&category=21&type=multiple']
url_list_names=['All category','Computers','GK','Books','Music','Sports']
datat=[]
for i in range (6):
    datat.append(urllib.request.urlopen(url_list[i]).read().decode())

obj0 = json.loads(datat[0])
obj1 = json.loads(datat[1])
obj2 = json.loads(datat[2])
obj3 = json.loads(datat[3])
obj4 = json.loads(datat[4])
obj5 = json.loads(datat[5])


obj_list=(obj0,obj1,obj2)
#some used variables
score=0
count = 1
timer_status=0
selected=""


def stats_update(sclt):
    file=open('stats','r')
    content=file.read()
    data=json.loads(content)
    file.close()
    file=open('stats','w')
    data["scores"].append(sclt)
    json.dump(data,file)

def themeset(tn):
    '''
    This function sets the theme that user requested by writing it in a text file.
    '''
    global sett_window
    file=open('theme.txt','w')
    file.write(tn)
    tmsg.showinfo("Theme Set", " The new theme will apply automatically when you reopen the program")
    raise_frame(intro)
    
def raise_frame(frame):
    frame.tkraise()

def timer_start():
    '''
    This funtion starts/stops the timer
    '''
    global selected
    global timer_status
    while timer_status == 0:
        if timerlabel['value'] > 0 :
            timerlabel.after(100,timer_start)
            timerlabel['value'] -= 100/150
        else :
            score_calc(1 ,selected )
        break

def start(category):
    '''
    This function starts the quiz from the category page
    '''
    global timer_status
    global timerlabel
    global selected
    selected = category
    raise_frame(q1)
    timerlabel.pack()
    timer_status=0
    timer_start()
    q_a_main(category)

def score_calc(o , category):
    '''
    This is the main function that checks the answer and calculates the score
    '''
    global score
    global count
    global timer_status
    global timerlabel
    timerlabel.pack()
    timer_status=1
    coranswer=html.unescape(category["results"][count-1]['correct_answer'])
    if count<15:
        if o == 0:        
            if answerlist[count-1].get() == category["results"][count-1]['correct_answer']:
                score = score+1
                #print(score)
                tmsg.showinfo("Response", " Correct")
            else:
                #print("score not increased")
                tmsg.showinfo("Response", f'Wrong \n The correct answer was \n \"{coranswer}\""')
            
        elif o==1:
            tmsg.showinfo("Response", f'Time UP \n The correct answer was \n \"{coranswer}\""')
        c=-1
        for i in (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
            if c < count:            
                raise_frame(i)
                c=c+1
        count=count+1 
        c=-1
        timerlabel['value']=100
        timer_status=0
        timer_start()
    else:
        if o == 0:        
            if answerlist[count-1].get() == category["results"][count-1]['correct_answer']:
                score = score+1
                #print(score)
                tmsg.showinfo("Response", " Correct")
            else:
                #print("score not increased")
                tmsg.showinfo("Response", f'Wrong \n The correct answer was \n \"{coranswer}\""')
            
        elif o==1:
            tmsg.showinfo("Response", f'Time UP \n The correct answer was \n \"{coranswer}\""')
        #final score
        file=open('stats','r')
        content=file.read()
        data=json.loads(content)
        nme=data["name"]
        ttk.Label(final,text=f"{nme}, you scored {score} out of 15", font='lucida 20 bold'  , wraplength=400).pack(pady=20)
        timerlabel.forget()
        raise_frame(final)
        stats_update(score)


def restart():
    global score
    global count
    global timer_status
    global question
    score=0
    count = 1
    timer_status=0
    raise_frame(intro)

def name_check():
    '''This function checks whether the user had entered the name before or not. If yes then the enter name frame will not get displayed
    '''
    file=open('stats','r')
    content=file.read()
    data=json.loads(content)
    if data["name"]!= "":
        raise_frame(cate)
    else:
        raise_frame(enter_name)

def name_set():
    print(name_entry.get())
    file=open('stats','r')
    content=file.read()
    data=json.loads(content)
    file.close
    file=open('stats','w')
    data["name"]=name_entry.get()
    json.dump(data,file)
    raise_frame(cate)

pygame.mixer.music.load("rtwi.mp3")
pygame.mixer.music.play()
musicio=IntVar(value=1)

def music_toggle():
    global musicio
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()

    else:
        pygame.mixer.music.unpause()


#frames declaration
intro= ttk.Frame(home)
cate=ttk.Frame(home)
sett_window=ttk.Frame(home)
stats=ttk.Frame(home)
theme_window=ttk.Frame(home)
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
final=ttk.Frame(home)
enter_name=ttk.Frame(home)
#frames declaration end -->


#positionRight = int(home.winfo_screenwidth()/2 - 733/2)
#positionDown = int(home.winfo_screenheight()/2 - 434/2)
#home.geometry("733x434+{}+{}".format(positionRight, positionDown))
home.iconbitmap("logo.ico")
home.resizable(False, False)

#<--timer frame
timerframe=ttk.Frame(home)
timerframe.grid(row=1, column=0, sticky='news')
#timer frame End-->

#<--Timer label
timerlabel=ttk.Progressbar(timerframe, orient=HORIZONTAL,length=700 ,mode = 'determinate')
timerlabel['value'] = 100
#timer label -->

#<-- Category frame
ttk.Label(cate, text='Please Select Your Trivia Category', font= 'lucida 20 bold').pack(pady=5)
ttk.Button(cate, text=f'{url_list_names[0]}' , command =lambda:start(obj0)).pack(pady=20)
ttk.Button(cate, text=f'{url_list_names[1]}' , command =lambda:start(obj1)).pack(pady=20)
ttk.Button(cate, text=f'{url_list_names[2]}' , command =lambda:start(obj2)).pack(pady=20)
ttk.Button(cate, text=f'{url_list_names[3]}' , command =lambda:start(obj3)).pack(pady=20)
ttk.Button(cate, text=f'{url_list_names[4]}' , command =lambda:start(obj4)).pack(pady=20)
ttk.Button(cate, text=f'{url_list_names[5]}' , command =lambda:start(obj5)).pack(pady=20)
ttk.Label(cate,text='Questions provided by Open Trivia Database', font='lucida 8').pack()
#Category Frame --> 

#<--Final window
#ttk.Button(final,text='Back to Mainmenu', command=restart).pack(side=BOTTOM)
ttk.Button(final,text='Exit', command=lambda:home.destroy()).pack(side=BOTTOM)
#Final Window-->
def stats_window():
    file=open('stats','r')
    content=file.read()
    data=json.loads(content)
    name=data['name']
    no_of_games=len(data['scores'])
    ttk.Label(stats,text=f'Hello {name}',font='lucida 20 bold').pack(pady=20)
    ttk.Label(stats,text=f'You have played {no_of_games} games',font='lucida 20').pack(pady=3)
    if no_of_games !=0:
        avg_score=sum(data['scores'])/len(data['scores'])
        max_score=max(data['scores'])
        min_score=min(data['scores'])
        
        ttk.Label(stats,text=f'{round(avg_score,2)} is your average score',font='lucida 20').pack(pady=3)
        ttk.Label(stats,text=f'{max_score} is your maximum score',font='lucida 20').pack(pady=3)
        ttk.Label(stats,text=f'{min_score} is your minimum score',font='lucida 20').pack(pady=3)
    else:
        ttk.Label(stats,text="Please start playing to see your stats",font='lucida 20').pack(pady=3)
    ttk.Button(stats,text='Back To Mainmenu',command=lambda:raise_frame(intro)).pack(side=BOTTOM)
stats_window()


#Enter your name frame
ttk.Label(enter_name,text="Please enter your name" ,justify=CENTER, font='lucida 20').pack(pady=5)
name_entry = ttk.Entry(enter_name,justify=CENTER, font='lucida 20')
name_entry.pack(pady=20)
ttk.Button(enter_name,text='Continue',command=name_set).pack(pady=10)
#enter your name frame --> 


def volume_set(value):
    pygame.mixer.music.set_volume((int(float(value)))/ 100)

#sett_window
ttk.Label(sett_window, text="Settings" , font="helvitica 20 bold").pack()
ttk.Checkbutton(sett_window, text="Music", command=music_toggle,variable=musicio).pack(pady=5)
volume = ttk.Scale(sett_window, from_=0, to=100, orient=HORIZONTAL, command=volume_set)
volume.set(100)
volume.pack(pady=5)
ttk.Button(sett_window,text='Change Theme', command=lambda:raise_frame(theme_window)).pack(pady=5)
#sett_window


def themes_buttons():
    
    ttk.Label(theme_window,text='Select your theme').pack(pady=10)
    ttk.Button(theme_window,text='Equilux',command=lambda:themeset('equilux')).pack(pady=10)
    ttk.Button(theme_window,text='Yaru',command=lambda:themeset('yaru')).pack(pady=10)
    ttk.Button(theme_window,text='Radiance',command=lambda:themeset('radiance')).pack(pady=10)
    ttk.Button(theme_window,text='Black',command=lambda:themeset('black')).pack(pady=10)
    ttk.Button(theme_window,text='Default',command=lambda:themeset('default')).pack(pady=10)
    ttk.Button(theme_window,text='Breeze',command=lambda:themeset('breeze')).pack(pady=10)
    ttk.Button(theme_window,text='ITFT1',command=lambda:themeset('itft1')).pack(pady=10)
    ttk.Button(theme_window,text='Return to Mainmenu',command=lambda:raise_frame(intro)).pack(pady=10)


themes_buttons()

#frame assignment
#intro.grid(row=0, column=0, sticky='news')
for frame in (intro,cate,sett_window,stats,theme_window, q1, q2, q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,final,enter_name):
    frame.grid(row=0, column=0, sticky='news')

#home page
#ttk.Button(intro,text='Exit',command=lambda:home.destroy()).pack()
#home.overrideredirect(True)
temporary_frame=ttk.Frame(intro)
temporary_frame.grid(row= 0 , column = 0 ,sticky='nw')
settings_img=PhotoImage(file='settings.png')
ttk.Button(temporary_frame, image=settings_img,command=lambda:raise_frame(sett_window)).pack(padx=(10,0) ,side='left')
photo=PhotoImage(file="quiz_trans.png")
pic=ttk.Label(intro, image=photo, borderwidth=0).grid(padx=(45 , 0), pady = 5, row= 1 , column = 0)

start_img=PhotoImage(file='start.png')
ttk.Button(intro, image=start_img ,command=name_check).grid(row= 2 , column = 0 , pady=(40,0))



ttk.Button(temporary_frame,text="Your Stats",command=lambda:raise_frame(stats)).pack(padx=(500, 10),pady=5, side='right')

answerlist=[]
def q_a_main(category):
    global answerlist
    #question list maker
    questions_list=[]
    for i in range (15):
        qtemp=category["results"][i]['question']
        qnew=html.unescape(qtemp)
        questions_list.append('Q'+str(i+1)+' '+qnew)

    #options list 
    new_list=[]
    for i in range(15):
        opt_list=[]
        opt_list.append(category["results"][i]['correct_answer'])
        opt_list.extend(category["results"][i]['incorrect_answers'])
        random.shuffle(opt_list)
        new_list.append(opt_list)

    #question labels in diff. frames
    j=0
    for i in (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
        question=ttk.Label(i, text=questions_list[j], font='lucida 20 bold'  , wraplength=400).pack(pady=20)
        j=j+1

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
        options= ttk.Radiobutton(q, text= html.unescape(new_list[noq][0]),variable=answerlist[noq],value=new_list[noq][0]).pack(pady=10)
        options= ttk.Radiobutton(q, text= html.unescape(new_list[noq][1]),variable=answerlist[noq],value=new_list[noq][1]).pack(pady=10)
        options= ttk.Radiobutton(q, text= html.unescape(new_list[noq][2]),variable=answerlist[noq],value=new_list[noq][2]).pack(pady=10)
        options= ttk.Radiobutton(q, text= html.unescape(new_list[noq][3]),variable=answerlist[noq],value=new_list[noq][3]).pack(pady=10)
        noq=noq+1
    
    
    #Submit Buttom
    for j in (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
        ttk.Button(j, text="Submit" ,command=lambda:score_calc(0 , category)).pack(side='bottom', pady=10)

    
raise_frame(intro)
home.mainloop()
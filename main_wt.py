from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as tmsg
import json
import urllib.request
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import html
import math
import threading
import pickle
from time import sleep


print("Welcome to Trivia Quiz")

pygame.mixer.init()
song_no=1
pygame.mixer.music.load("oth.mp3")
pygame.mixer.music.play(-1)    
try:
    file=open('stats','rb')
    x=pickle.load(file)
    file.close()

except:
    x={"name": "", "scores": []}
    pickle.dump(x,open('stats','wb'))
    file.close()

def change_music():
    global song_no
    if song_no==1:
        pygame.mixer.music.load("rtwi.mp3")
        pygame.mixer.music.play(-1)
        song_no=2
    else:
        pygame.mixer.music.load("oth.mp3")
        pygame.mixer.music.play(-1)
        song_no=1


def on_closing():
    if tmsg.askokcancel("Quit", "Do you want to quit?"):
        quit()



while True :
    

    #print ('Loading....')
    themetxt= open('theme.txt','r')
    home = ThemedTk(theme=f'{themetxt.read()}')
    home.title('Quiz')
    status=0
    def loading_print():
        global status
        while status==0:
            delay=.5
            print('Loading',end='')
            n_dots = 0

            while status==0:
                if n_dots == 3:
                    print(end='\b\b\b', flush=True)
                    print(end='   ',    flush=True)
                    print(end='\b\b\b', flush=True)
                    n_dots = 0
                else:
                    print(end='.', flush=True)
                    n_dots += 1
                sleep(delay)
        while status==1:
            print(end='\b\b\b\b\b\b\b\b\b\b\b', flush=True)
            print(end='           ',    flush=True)
            print(end='\b\b\b\b\b\b\b\b\b\b\b', flush=True)
            print('Loaded Successfully', flush=True)
            break
    #loading_print(0)
    t1=threading.Thread(target=loading_print)
    t1.start()
    
    url_list=['https://opentdb.com/api.php?amount=15&type=multiple','https://opentdb.com/api.php?amount=15&category=18&type=multiple','https://opentdb.com/api.php?amount=15&category=9&type=multiple','https://opentdb.com/api.php?amount=15&category=10&type=multiple','https://opentdb.com/api.php?amount=15&category=12&type=multiple','https://opentdb.com/api.php?amount=15&category=21&type=multiple']
    url_list_names=['All category','Computers','GK','Books','Music','Sports']
    datat=[]
    try:
        for i in range(6):
            datat.append(urllib.request.urlopen(url_list[i]).read().decode())

        obj0 = json.loads(datat[0])
        obj1 = json.loads(datat[1])
        obj2 = json.loads(datat[2])
        obj3 = json.loads(datat[3])
        obj4 = json.loads(datat[4])
        obj5 = json.loads(datat[5])
    except:
        obj0={"response_code":502,"results":[{"category":"Entertainment: Film","type":"multiple","difficulty":"easy","question":"Which animated movie was first to feature a celebrity as a voice actor?","correct_answer":"Aladdin","incorrect_answers":["Toy Story","James and the Giant Peach","The Hunchback of Notre Dame"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What word represents the letter &#039;T&#039; in the NATO phonetic alphabet?","correct_answer":"Tango","incorrect_answers":["Target","Taxi","Turkey"]},{"category":"Entertainment: Television","type":"multiple","difficulty":"hard","question":"What&#039;s Dr. Doofenshmirtz first name?","correct_answer":"Heinz","incorrect_answers":["Hans","Hank","Heidi"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"What animal is featured on the cover of English electronic music group The Prodigy&#039;s album, &quot;The Fat of the Land&quot;?","correct_answer":"Crab","incorrect_answers":["Fox","Elephant","Tiger"]},{"category":"Science & Nature","type":"multiple","difficulty":"medium","question":"Which of these elements on the Periodic Table is a Noble Gas?","correct_answer":"Neon","incorrect_answers":["Potassium","Iodine","Colbalt"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"hard","question":"Who designed the album cover for True Romance, an album by Estelle?","correct_answer":"Rebecca Sugar","incorrect_answers":["Matt Burnett","Ian Jones Quartey","Ben Leven"]},{"category":"Politics","type":"multiple","difficulty":"medium","question":"Which of these is NOT one of Donald Trump&#039;s children?","correct_answer":"Julius","incorrect_answers":["Donald Jr.","Ivanka","Eric"]},{"category":"Science: Computers","type":"multiple","difficulty":"hard","question":"Dutch computer scientist Mark Overmars is known for creating which game development engine?","correct_answer":"Game Maker","incorrect_answers":["Stencyl","Construct","Torque 2D"]},{"category":"Entertainment: Film","type":"multiple","difficulty":"medium","question":"What character in the Winnie the Pooh films was added by Disney and does not appear in the original books?","correct_answer":"Gopher","incorrect_answers":["Tigger","Heffalumps","Rabbit"]},{"category":"Entertainment: Video Games","type":"multiple","difficulty":"medium","question":"What are the names of the Ice Climbers in the video game Ice Climber?","correct_answer":"Popo and Nana","incorrect_answers":["Popo and Nina","Papi and Nana","Papi and Nina"]},{"category":"Entertainment: Video Games","type":"multiple","difficulty":"easy","question":"In the Halo series, which era of SPARTAN is Master Chief? ","correct_answer":"SPARTAN-II","incorrect_answers":["SPARTAN-I","SPARTAN-III","SPARTAN-IV"]},{"category":"Sports","type":"multiple","difficulty":"hard","question":"Which city features all of their professional sports teams&#039; jersey&#039;s with the same color scheme?","correct_answer":"Pittsburgh","incorrect_answers":["New York","Seattle","Tampa Bay"]},{"category":"Entertainment: Film","type":"multiple","difficulty":"medium","question":"Brendan Fraser starred in the following movies, except which one?","correct_answer":"Titanic","incorrect_answers":["Monkeybone","Encino Man","Mrs. Winterbourne"]},{"category":"Entertainment: Television","type":"multiple","difficulty":"medium","question":"What actor portrays Hogan &quot;Wash&quot; Washburne in the TV Show Firefly?","correct_answer":"Alan Tudyk","incorrect_answers":["Adam Baldwin","Nathan Fillion","Sean Maher"]},{"category":"Entertainment: Cartoon & Animations","type":"multiple","difficulty":"medium","question":"Which singer provided the voice of Metroid&#039;s Mother Brain in the animated series &quot;Captain N: The Game Master&quot;?","correct_answer":"Levi Stubbs","incorrect_answers":["Freddie Mercury","Janet Jackson","Joan Jett"]}]}
        obj1={"response_code":502,"results":[{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":"What five letter word is the motto of the IBM Computer company?","correct_answer":"Think","incorrect_answers":["Click","Logic","Pixel"]},{"category":"Science: Computers","type":"multiple","difficulty":"hard","question":"How many Hz does the video standard PAL support?","correct_answer":"50","incorrect_answers":["59","60","25"]},{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":"Which of these is the name for the failed key escrow device introduced by the National Security Agency in 1993?","correct_answer":"Clipper Chip","incorrect_answers":["Enigma Machine","Skipjack","Nautilus"]},{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":"In HTML, which non-standard tag used to be be used to make elements scroll across the viewport?","correct_answer":"&lt;marquee&gt;&lt;\/marquee&gt;","incorrect_answers":["&lt;scroll&gt;&lt;\/scroll&gt;","&lt;move&gt;&lt;\/move&gt;","&lt;slide&gt;&lt;\/slide&gt;"]},{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":"What is the correct term for the metal object in between the CPU and the CPU fan within a computer system?","correct_answer":"Heat Sink","incorrect_answers":["CPU Vent","Temperature Decipator","Heat Vent"]},{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":"What does &quot;LCD&quot; stand for?","correct_answer":"Liquid Crystal Display","incorrect_answers":["Language Control Design","Last Common Difference","Long Continuous Design"]},{"category":"Science: Computers","type":"multiple","difficulty":"hard","question":"Who is the original author of the realtime physics engine called PhysX?","correct_answer":"NovodeX","incorrect_answers":["Ageia","Nvidia","AMD"]},{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":".rs is the top-level domain for what country?","correct_answer":"Serbia","incorrect_answers":["Romania","Russia","Rwanda"]},{"category":"Science: Computers","type":"multiple","difficulty":"hard","question":"What is the name of the process that sends one qubit of information using two bits of classical information?","correct_answer":"Quantum Teleportation","incorrect_answers":["Super Dense Coding","Quantum Entanglement","Quantum Programming"]},{"category":"Science: Computers","type":"multiple","difficulty":"hard","question":"What was the first company to use the term &quot;Golden Master&quot;?","correct_answer":"Apple","incorrect_answers":["IBM","Microsoft","Google"]},{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":"The name of technology company HP stands for what?","correct_answer":"Hewlett-Packard","incorrect_answers":["Howard Packmann","Husker-Pollosk","Hellman-Pohl"]},{"category":"Science: Computers","type":"multiple","difficulty":"hard","question":"Who invented the &quot;Spanning Tree Protocol&quot;?","correct_answer":"Radia Perlman","incorrect_answers":["Paul Vixie","Vint Cerf","Michael Roberts"]},{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":"Approximately how many Apple I personal computers were created?","correct_answer":"200","incorrect_answers":["100","500","1000"]},{"category":"Science: Computers","type":"multiple","difficulty":"easy","question":"Which programming language shares its name with an island in Indonesia?","correct_answer":"Java","incorrect_answers":["Python","C","Jakarta"]},{"category":"Science: Computers","type":"multiple","difficulty":"hard","question":"Lenovo acquired IBM&#039;s personal computer division, including the ThinkPad line of laptops and tablets, in what year?","correct_answer":"2005","incorrect_answers":["1999","2002","2008"]}]}
        obj2={"response_code":502,"results":[{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Which company did Valve cooperate with in the creation of the Vive?","correct_answer":"HTC","incorrect_answers":["Oculus","Google","Razer"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"In the video-game franchise Kingdom Hearts, the main protagonist, carries a weapon with what shape?","correct_answer":"Key","incorrect_answers":["Sword","Pen","Cellphone"]},{"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"What is the name of the very first video uploaded to YouTube?","correct_answer":"Me at the zoo","incorrect_answers":["tribute","carrie rides a truck","Her new puppy from great grandpa vern."]},{"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"What is the romanized Arabic word for &quot;moon&quot;?","correct_answer":"Qamar","incorrect_answers":["Najma","Kawkab","Shams"]},{"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"Amsterdam Centraal station is twinned with what station?","correct_answer":"London Liverpool Street","incorrect_answers":["Frankfurt (Main) Hauptbahnhof","Paris Gare du Nord","Brussels Midi"]},{"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"Which of the General Mills Corporation&#039;s monster cereals was the last to be released in the 1970&#039;s?","correct_answer":"Fruit Brute","incorrect_answers":["Count Chocula","Franken Berry","Boo-Berry"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What color is the &quot;Ex&quot; in FedEx Ground?","correct_answer":"Green","incorrect_answers":["Red","Light Blue","Orange"]},{"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"Apple co-founder Steve Jobs died from complications of which form of cancer?","correct_answer":"Pancreatic","incorrect_answers":["Bone","Liver","Stomach"]},{"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"Virtual reality company Oculus VR lost which of it&#039;s co-founders in a freak car accident in 2013?","correct_answer":"Andrew Scott Reisse","incorrect_answers":["Nate Mitchell","Jack McCauley","Palmer Luckey"]},{"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"Who founded the Khan Academy?","correct_answer":"Sal Khan","incorrect_answers":["Ben Khan","Kitt Khan","Adel Khan"]},{"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"Which of these words means &quot;idle spectator&quot;?","correct_answer":"Gongoozler","incorrect_answers":["Gossypiboma","Jentacular","Meupareunia"]},{"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"Which country drives on the left side of the road?","correct_answer":"Japan","incorrect_answers":["Germany","Russia","China"]},{"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"Nephelococcygia is the practice of doing what?","correct_answer":"Finding shapes in clouds","incorrect_answers":["Sleeping with your eyes open","Breaking glass with your voice","Swimming in freezing water"]},{"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"What is the currency of Poland?","correct_answer":"Z\u0142oty","incorrect_answers":["Ruble","Euro","Krone"]},{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"When one is &quot;envious&quot;, they are said to be what color?","correct_answer":"Green","incorrect_answers":["Red","Blue","Yellow"]}]}
        obj3={"response_code":502,"results":[{"category":"Entertainment: Books","type":"multiple","difficulty":"hard","question":"In the book &quot;The Martian&quot;, how long was Mark Watney trapped on Mars (in Sols)?","correct_answer":"549 Days","incorrect_answers":["765 Days","401 Days","324 Days"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"hard","question":"In the Harry Potter universe, who does Draco Malfoy end up marrying?","correct_answer":"Astoria Greengrass","incorrect_answers":["Pansy Parkinson","Millicent Bulstrode","Hermione Granger"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"medium","question":"What was the pen name of novelist, Mary Ann Evans?","correct_answer":"George Eliot","incorrect_answers":["George Orwell","George Bernard Shaw","George Saunders"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"medium","question":"In the &quot;The Hobbit&quot;, who kills Smaug?","correct_answer":"Bard","incorrect_answers":["Bilbo Baggins","Gandalf the Grey","Frodo"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"medium","question":"The novel &quot;Of Mice And Men&quot; was written by what author? ","correct_answer":"John Steinbeck ","incorrect_answers":["George Orwell","Mark Twain ","Harper Lee"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"easy","question":"Who was the author of the 1954 novel, &quot;Lord of the Flies&quot;?","correct_answer":"William Golding","incorrect_answers":["Stephen King","F. Scott Fitzgerald","Hunter Fox"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"easy","question":"What is the name of the protagonist of J.D. Salinger&#039;s novel Catcher in the Rye?","correct_answer":"Holden Caulfield","incorrect_answers":["Fletcher Christian","Jay Gatsby","Randall Flagg"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"medium","question":"Which of these book series is by James Patterson?","correct_answer":"Maximum Ride","incorrect_answers":["Harry Potter","The Legend of Xanth","The Bartemaeus Trilogy"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"medium","question":"In the novel &quot;Lord of the Rings&quot;, how many rings of power were given to the race of man?","correct_answer":"9","incorrect_answers":["5","11","13"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"medium","question":"Which of the following was the author of &quot;Username Evie&quot;?","correct_answer":"Joe Sugg","incorrect_answers":["Zoe Sugg","Joe Weller","Alfie Deyes"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"easy","question":"What was the first ever entry written for the SCP Foundation collaborative writing project?","correct_answer":"SCP-173","incorrect_answers":["SCP-001","SCP-999","SCP-1459"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"medium","question":"Which novel by John Grisham was conceived on a road trip to Florida while thinking about stolen books with his wife?","correct_answer":"Camino Island","incorrect_answers":["Rogue Lawyer","Gray Mountain","The Litigators"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"medium","question":"Who is the author of the series &quot;Malazan Book of the Fallen&quot;?","correct_answer":"Steven Erikson","incorrect_answers":["Ian Cameron Esslemont","George R. R. Martin","J. R. R. Tolkien"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"easy","question":"Who wrote &quot;A Tale of Two Cities&quot;?","correct_answer":"Charles Dickens","incorrect_answers":["Charles Darwin","Mark Twain","Roald Dahl"]},{"category":"Entertainment: Books","type":"multiple","difficulty":"medium","question":"Which Russian author wrote the epic novel War and Peace?","correct_answer":"Leo Tolstoy","incorrect_answers":["Fyodor Dostoyevsky","Alexander Pushkin","Vladimir Nabokov"]}]}
        obj4={"response_code":502,"results":[{"category":"Entertainment: Music","type":"multiple","difficulty":"easy","question":"What is the best selling album of all time from 1976 to 2018?","correct_answer":"Thriller","incorrect_answers":["Back in Black","Abbey Road","The Dark Side of the Moon"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"easy","question":"Which artist released the 2012 single &quot;Harlem Shake&quot;, which was used in numerous YouTube videos in 2013?","correct_answer":"Baauer","incorrect_answers":["RL Grime","NGHTMRE","Flosstradamus"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"easy","question":"The &quot;K&quot; in &quot;K-Pop&quot; stands for which word?","correct_answer":"Korean","incorrect_answers":["Kenyan","Kazakhstan","Kuwaiti"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"easy","question":"What was Rage Against the Machine&#039;s debut album?","correct_answer":"Rage Against the Machine","incorrect_answers":["Evil Empire","Bombtrack","The Battle Of Los Angeles"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"easy","question":"Which of these is the name of a song by Tears for Fears?","correct_answer":"Shout","incorrect_answers":["Scream","Yell","Shriek"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"easy","question":"Kanye West at 2009 VMA&#039;s interrupted which celebrity?","correct_answer":"Taylor Swift","incorrect_answers":["MF DOOM","Beyonce","Beck"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"Who is the frontman of Muse?","correct_answer":"Matt Bellamy","incorrect_answers":["Dominic Howard","Thom Yorke","Jonny Greenwood"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"Which of these bands is the oldest?","correct_answer":"Pink Floyd","incorrect_answers":["AC\/DC","Metallica","Red Hot Chili Peppers"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"Cryoshell, known for &quot;Creeping in My Soul&quot; did the advertising music for what Lego Theme?","correct_answer":"Bionicle","incorrect_answers":["Hero Factory","Ben 10 Alien Force","Star Wars"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"Who is the vocalist and frontman of rock band &quot;Guns N&#039; Roses&quot;?","correct_answer":"Axl Rose","incorrect_answers":["Kurt Cobain","Slash","Bono"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"What was David Bowie&#039;s real surname?","correct_answer":"Jones","incorrect_answers":["Johnson","Edwards","Carter"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"hard","question":"What song originally performed by The Bee Gees in 1978 had a cover version by Steps 20 years later?","correct_answer":"Tragedy","incorrect_answers":["Night Fever","Stayin&#039; Alive","You Should Be Dancing"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"Which song made by MAN WITH A MISSION was used as the opening for the anime &quot;Log Horizon&quot;?","correct_answer":"&quot;Database&quot;","incorrect_answers":["&quot;Dead End in Tokyo&quot;","&quot;Raise Your Flag&quot;","&quot;Out of Control&quot;"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"Which of these albums is a Wu-Tang Clan album?","correct_answer":"Iron Flag","incorrect_answers":["Perfect Hair","The Low End Theory","Licensed to Ill"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"easy","question":"What is the name of Rivers Cuomo&#039;s wife?","correct_answer":"Kyoko Ito","incorrect_answers":["Yoko Ono","Kyary Pamyu Pamyu","LiSA"]}]}
        obj5={"response_code":502,"results":[{"category":"Sports","type":"multiple","difficulty":"medium","question":"What is the nickname of Northampton town&#039;s rugby union club?","correct_answer":"Saints","incorrect_answers":["Harlequins","Saracens","Wasps"]},{"category":"Sports","type":"multiple","difficulty":"easy","question":"How many soccer players should be on the field at the same time?","correct_answer":"22","incorrect_answers":["20","24","26"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"Which Formula One driver was nicknamed &#039;The Professor&#039;?","correct_answer":"Alain Prost","incorrect_answers":["Ayrton Senna","Niki Lauda","Emerson Fittipaldi"]},{"category":"Sports","type":"multiple","difficulty":"easy","question":"What was the final score of the Germany vs. Brazil 2014 FIFA World Cup match?","correct_answer":"7 - 1","incorrect_answers":["0 - 1","3 - 4","16 - 0"]},{"category":"Sports","type":"multiple","difficulty":"hard","question":"Which car company is the only Japanese company which won the 24 Hours of Le Mans?","correct_answer":"Mazda","incorrect_answers":["Toyota","Subaru","Nissan"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"What national team won the 2016 edition of UEFA European Championship?","correct_answer":"Portugal","incorrect_answers":["France","Germany","England"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"Who won the 2015 College Football Playoff (CFP) National Championship? ","correct_answer":"Ohio State Buckeyes","incorrect_answers":["Alabama Crimson Tide","Clemson Tigers","Wisconsin Badgers"]},{"category":"Sports","type":"multiple","difficulty":"easy","question":"The Los Angeles Dodgers were originally from what U.S. city?","correct_answer":"Brooklyn","incorrect_answers":["Las Vegas","Boston","Seattle"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"Which professional wrestler fell from the rafters to his death during a live Pay-Per-View event in 1999?","correct_answer":"Owen Hart","incorrect_answers":["Chris Benoit","Lex Luger","Al Snow"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"Who was the topscorer for England national football team?","correct_answer":"Wayne Rooney","incorrect_answers":["David Beckham","Steven Gerrard","Michael Owen"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"What is Tiger Woods&#039; all-time best career golf-score?","correct_answer":"61","incorrect_answers":["65","63","67"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"What country hosted the 2014 Winter Olympics?","correct_answer":"Russia","incorrect_answers":["Canada","United States","Germany"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"Which basketball team has attended the most NBA grand finals?","correct_answer":"Los Angeles Lakers","incorrect_answers":["Boston Celtics","Philadelphia 76ers","Golden State Warriors"]},{"category":"Sports","type":"multiple","difficulty":"hard","question":"Which of these Russian cities did NOT contain a stadium that was used in the 2018 FIFA World Cup?","correct_answer":"Vladivostok","incorrect_answers":["Rostov-on-Don","Yekaterinburg","Kaliningrad"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"Who won the 2018 Monaco Grand Prix?","correct_answer":"Daniel Ricciardo","incorrect_answers":["Sebastian Vettel","Kimi Raikkonen","Lewis Hamilton"]}]}



    obj_list=(obj0,obj1,obj2)
    #some used variables
    score=0
    count = 1
    timer_status=0
    selected=""
    status=0

    home.protocol("WM_DELETE_WINDOW", on_closing)

    def stats_update(sclt):
        if selected['response_code'] == 0 :
            file=open('stats','rb')
            data=pickle.load(file)
            file.close()
            file=open('stats','wb')
            data["scores"].append(sclt)
            pickle.dump(data,file)
            file.close()
        else:
            tmsg.showerror("No Internet",'Since you were playing offine, the current score won\'t be added to your stats')


    def themeset(tn):
        '''
        This function sets the theme that user requested by writing it in a text file.
        '''
        global sett_window
        file=open('theme.txt','w')
        file.write(tn)
        file.close()
        tmsg.showinfo("Theme Set", " Please wait a few seconds while the program reloads.")
        home.destroy()
        
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
            file=open('stats','rb')
            data=pickle.load(file)
            file.close()
            nme=data["name"]
            ttk.Label(final,text=f"{nme}, you scored {score} out of 15", font='lucida 20 bold'  , wraplength=550).pack(pady=20)
            timerlabel.forget()
            raise_frame(final)
            stats_update(score)


    def restart():
        tmsg.showinfo("Returning to homescreen", " Please wait a few seconds while the program reloads.")
        home.destroy()

    def exit():
        quit()


    def name_check():
        '''This function checks whether the user had entered the name before or not. If yes then the enter name frame will not get displayed
        '''
        file=open('stats','rb')
        data=pickle.load(file)
        file.close()
        if data["name"]!= "":
            raise_frame(cate)
        else:
            raise_frame(enter_name)

    def name_set():
        file=open('stats','rb')
        data=pickle.load(file)
        file.close
        file=open('stats','wb')
        data["name"]=name_entry.get()
        pickle.dump(data,file)
        file.close()
        raise_frame(cate)

    
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
    info=ttk.Frame(home)
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
    #home.geometry('700x503')
    home.iconbitmap("logo.ico")
    home.resizable(False, False)

    #<--timer frame
    timerframe=ttk.Frame(home)
    timerframe.grid(row=1, column=0, sticky='news')
    #timer frame End-->

    #info frame
    ttk.Label(info,text="Trivia Quiz",font="helveta 40 bold").pack(pady=10)
    ttk.Label(info,text="Version: 0.9 Beta",font="helveta 8 bold").pack()
    
    ttk.Button(info,text='Return to Mainmenu',command=lambda:raise_frame(intro)).pack(side=BOTTOM, pady=10)
    ttk.Label(info,text="Made in INDIA",font="helveta 30 bold").pack(side=BOTTOM, pady=10)
    #info frame-->

    #<--Timer label
    timerlabel=ttk.Progressbar(timerframe, orient=HORIZONTAL,length=700 ,mode = 'determinate')
    timerlabel['value'] = 100
    #timer label -->

    #<-- Category frame
    ttk.Label(cate, text='Please Select Your Trivia Category', font= 'lucida 20 bold').pack(pady=5)
    ttk.Button(cate, text=f'{url_list_names[0]}' , command =lambda:start(obj0)).pack(pady=10)
    ttk.Button(cate, text=f'{url_list_names[1]}' , command =lambda:start(obj1)).pack(pady=10)
    ttk.Button(cate, text=f'{url_list_names[2]}' , command =lambda:start(obj2)).pack(pady=10)
    ttk.Button(cate, text=f'{url_list_names[3]}' , command =lambda:start(obj3)).pack(pady=10)
    ttk.Button(cate, text=f'{url_list_names[4]}' , command =lambda:start(obj4)).pack(pady=10)
    ttk.Button(cate, text=f'{url_list_names[5]}' , command =lambda:start(obj5)).pack(pady=10)
    ttk.Label(cate,text='Questions provided by Open Trivia Database', font='lucida 8').pack(side=BOTTOM)
    ttk.Button(cate,text='Return to homescreen', command=lambda:raise_frame(intro)).pack(side=BOTTOM,pady=10)
    
    #Category Frame --> 

    #<--Final window
    
    
    ttk.Button(final,text='Exit', command=exit).pack(side=BOTTOM,pady=10)
    ttk.Button(final,text='Return to homescreen', command=restart).pack(side=BOTTOM,pady=10)
    #Final Window-->

    def stats_window():
        file=open('stats','rb')
        #content=file.read()
        data=pickle.load(file)
        file.close()
        name=data['name']
        no_of_games=len(data['scores'])
        ttk.Label(stats,text=f'Hello {name}',font='lucida 20 bold').pack(pady=20)
        ttk.Label(stats,text=f'You have played {no_of_games} games',font='lucida 20').pack(pady=3)
        if no_of_games !=0:
            avg_score=sum(data['scores'])/len(data['scores'])
            max_score=max(data['scores'])
            min_score=min(data['scores'])
            percentage=(avg_score/15)*100
            
            ttk.Label(stats,text=f'{round(avg_score,2)}/15 is your average score',font='lucida 20').pack(pady=3)
            ttk.Label(stats,text=f'{round(percentage,2)}% is your average percentage',font='lucida 20').pack(pady=3)
            ttk.Label(stats,text=f'{max_score}/15 is your maximum score',font='lucida 20').pack(pady=3)
            ttk.Label(stats,text=f'{min_score}/15 is your minimum score',font='lucida 20').pack(pady=3)
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
    ttk.Button(sett_window,text="Change Music", command=change_music).pack(pady=5)
    ttk.Label(sett_window,text="Volume:").pack(pady=10)
    volume = ttk.Scale(sett_window, from_=0, to=100, orient=HORIZONTAL,length=300, command=volume_set)
    volume.set(60)
    volume.pack(pady=5)
    ttk.Button(sett_window,text='Change Theme', command=lambda:raise_frame(theme_window)).pack(pady=5)
    ttk.Button(sett_window,text='About', command=lambda:raise_frame(info)).pack(pady=60)
    ttk.Button(sett_window,text='Return to Mainmenu',command=lambda:raise_frame(intro)).pack(side=BOTTOM, pady=10)
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
    for frame in (intro,cate,info,sett_window,stats,theme_window, q1, q2, q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,final,enter_name):
        frame.grid(row=0, column=0, sticky='news')
        

    #home page
    
    #key binding
    for frame in (q1, q2, q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
        frame.bind("<space>",lambda:score_calc(0 , selected))
    #key binding


    temporary_frame=ttk.Frame(intro)
    temporary_frame.grid(row= 0 , column = 0 ,sticky='nw')
    settings_img=PhotoImage(file='settings.png')
    ttk.Button(temporary_frame, image=settings_img,command=lambda:raise_frame(sett_window)).pack(padx=(10,0) ,side='left')
    photo=PhotoImage(file="quiz_trans.png")
    pic=ttk.Label(intro, image=photo, borderwidth=0).grid(padx=(45 , 0), pady = 5, row= 1 , column = 0)

    start_img=PhotoImage(file='start.png')
    ttk.Button(intro, image=start_img ,command=name_check).grid(row= 2 , column = 0 , pady=(60,10))



    ttk.Button(temporary_frame,text="Your Stats",command=lambda:raise_frame(stats)).pack(padx=(560, 10),pady=5, side='right')

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

    status=1
    #loading_print()
    raise_frame(intro)
    home.mainloop()

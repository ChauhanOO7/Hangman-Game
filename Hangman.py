from tkinter import *
from PIL import Image,ImageTk
import csv
from tkinter import messagebox
import pygame

pygame.mixer.init()


def screen_end():
    root.destroy()

global chances,tell_page,counter
counter=-1
chances=0
tell_page=0

root=Tk()

root.geometry("500x700")
root.maxsize(500,700)
root.minsize(500,700)
root.title(" Hangman")
root.iconbitmap("./Images/capital.ico")

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

#frame2

frame2=LabelFrame(root,bg="red")
frame2.grid(row=0,column=0,sticky="nsew")
frame2["border"]=0

img2=Image.open("./Images/gi.jpg")    
img2=ImageTk.PhotoImage(img2.resize((500,700)))         
img_label2=Label(frame2,image=img2)     
img_label2.place(x=0,y=0,relwidth=1,relheight=1)
img_label2["border"]=0

ins_heading=Label(frame2,text="Game Instructions",bg="#C8AB81",font=("verdana",20))
ins_heading.grid(row=0,column=0,columnspan=7,padx=(0,480),pady=(30,0))

ins_heading1=Label(frame2,text="Objective:",font=("verdana",13),bg="#C8AB81")
ins_heading1.grid(row=1,column=0,columnspan=7,padx=(0,880),pady=(40,0))

text_1="""Save your friend from being hanged by guessing the correct word within a
limited number of chances while managing your score."""
inside_1=Text(frame2,width=110,height=2,font=("verdana",9),bg="#C8AB81")
inside_1.grid(row=2,column=0,columnspan=7,pady=(10,0),padx=(0,80))
inside_1.insert(END,text_1)
inside_1.config(spacing3=10,state=DISABLED)
inside_1["border"]=0

ins_heading2=Label(frame2,text="Setup:",font=("verdana",13),bg="#C8AB81")
ins_heading2.grid(row=3,column=0,columnspan=7,padx=(0,910),pady=(30,0))

text_2="""2 players: One guesses the word, the other is in danger.
Word to guess: Letters shown in brackets.
Total 11 words to Play."""
inside_2=Text(frame2,width=110,height=3,font=("verdana",9),bg="#C8AB81")
inside_2.grid(row=4,column=0,columnspan=7,pady=(10,0),padx=(0,80))
inside_2.insert(END,text_2)
inside_2.config(spacing3=10,state=DISABLED)
inside_2["border"]=0

ins_heading3=Label(frame2,text="Points:",font=("verdana",13),bg="#C8AB81")
ins_heading3.grid(row=5,column=0,columnspan=7,padx=(0,910),pady=(30,0))

text_3="""Correct guess: +3 points.
Incorrect guess:
2 extra chance given.
Each subsequent wrong guess: -1 point.
Hint use: 1 time per word."""

inside_3=Text(frame2,width=110,height=5,font=("verdana",9),bg="#C8AB81")
inside_3.grid(row=6,column=0,columnspan=7,pady=(10,0),padx=(0,80))
inside_3.insert(END,text_3)
inside_3["border"]=0
inside_3.config(spacing3=10,state=DISABLED)


ins_heading4=Label(frame2,text="Game Elements:",font=("verdana",13),bg="#C8AB81")
ins_heading4.grid(row=7,column=0,columnspan=9,padx=(0,910),pady=(30,0))

text_4="""Displayed: Player's score and target score.
Goal: Keep your score higher than the target score to save your friend."""

inside_4=Text(frame2,width=110,height=2,font=("verdana",9),bg="#C8AB81")
inside_4.grid(row=8,column=0,columnspan=7,pady=(10,0),padx=(0,80))
inside_4.insert(END,text_4)
inside_4["border"]=0
inside_4.config(spacing3=10,state=DISABLED)


#frame3

game_window=LabelFrame(root)
game_window.grid(row=0,column=0,sticky="nsew")
game_window["border"]=0
img3=Image.open("./Images/pexels-j-lee-6847584.jpg")    
img3=ImageTk.PhotoImage(img3.resize((500,700)))         
img_label3=Label(game_window,image=img3)     
img_label3.place(x=0,y=0,relwidth=1,relheight=1)


score=Label(game_window,text="Score :",font=("verdana",15),bg="#fef39e")
score.grid(row=0,column=1,pady=(50,0),padx=(30,0))
score_no=Label(game_window,text="",font=("verdana",15),bg="#fef39e")
score_no.grid(row=0,column=2,padx=(3,0),pady=(50,0),ipadx=10)

target=Label(game_window,text="Target :",font=("verdana",15),bg="#fcfac6")
target.grid(row=0,column=3,pady=(50,0),padx=(150,0))

target_no=Label(game_window,text="27",font=("verdana",15),bg="#fcfac6")
target_no.grid(row=0,column=4,padx=(3,0),pady=(50,0),ipadx=5)


question=Label(game_window,text="",width=13,height=1,font=("verdana",30),bg="#fdf19b")
question.grid(row=1,column=0,columnspan=4,pady=(90,0),padx=(80,0))

Guess=Label(game_window,text="Guess :",font=("verdana",16),bg="#fef090")
Guess.grid(row=2,column=0,columnspan=4,pady=(80,0),padx=(70,0))

answer=Entry(game_window,width=18,font=("verdana",15))
answer.grid(row=3,column=0,columnspan=4,pady=(30,0),padx=(70,0))

#buttons

hint=Button(game_window,text="Hint",width=5,font=("verdana",13),bg="black",fg="white",command=lambda:hint_win())
hint.grid(row=4,column=0,columnspan=4,padx=(70,0),pady=(20,0))
hint["border"]=0

confirm=Button(game_window,text="Confirm",width=7,font=("verdana",13),bg="black",fg="white",command=lambda:fun_confirm(answer.get()))
confirm.grid(row=5,column=0,columnspan=4,padx=(75,0),pady=(40,0))
confirm["border"]=0

Exit_to_mm=Button(game_window,text="Exit to MainMenu",width=15,font=("verdana",13),bg="black",fg="white",command=lambda:prev(start_frame))
Exit_to_mm.grid(row=6,column=0,columnspan=4,padx=(78,0),pady=(60,0))
Exit_to_mm["border"]=0

#frame4

game_win=LabelFrame(root)
game_win.grid(row=0,column=0,sticky="nsew")
game_win["border"]=0

img4=Image.open("./Images/win.jpg")    
img4=ImageTk.PhotoImage(img4.resize((500,700)))         
img_label4=Label(game_win,image=img4)     
img_label4.place(x=0,y=0,relwidth=1,relheight=1)
img_label4["border"]=0

you_win=Label(game_win,text="You Win!",font=("script",30),bg="#17181a",fg="white")
you_win.grid(row=0,column=0,columnspan=4,pady=(295,0),padx=(230,0))

target_label=Label(game_win,text="Target :",fg="white",bg="#17181a",font=("Roman",15))
target_label.grid(row=1,column=0,pady=(15,0),padx=(240,0))

target_score=Label(game_win,text="-",fg="white",bg="#17181a",font=("Roman",15))
target_score.grid(row=1,column=1,pady=(15,0))


score_label=Label(game_win,text="Score :",fg="white",bg="#17181a",font=("Roman",15))
score_label.grid(row=2,column=0,pady=(15,0),padx=(240,0))

score_score=Label(game_win,text="-",fg="white",bg="#17181a",font=("Roman",15))
score_score.grid(row=2,column=1,pady=(15,0))

play_again=Button(game_win,text="Play again",font=("Roman",15),command=lambda:window_frame(game_window))
play_again.grid(row=3,column=0,pady=(150,0))
play_again["border"]=0

exit_ga=Button(game_win,text="Exit",width=6,font=("Roman",15),command=lambda:window_frame(start_frame))
exit_ga.grid(row=3,column=1,pady=(150,0))
exit_ga["border"]=0

#frame5

lost=LabelFrame(root)
lost.grid(row=0,column=0,sticky="nsew")
lost["border"]=0

img5=Image.open("./Images/lost.jpg")    
img5=ImageTk.PhotoImage(img5.resize((500,700)))         
img_label5=Label(lost,image=img5)     
img_label5.place(x=0,y=0,relwidth=1,relheight=1)
img_label5["border"]=0


lost1_label=Label(lost,text="You",font=("san serif",40,"bold"))
lost1_label.grid(row=0,column=0,padx=(40,0),pady=(100,0))

lost2_label=Label(lost,text="Lose!",font=("san serif",40,"bold"))
lost2_label.grid(row=0,column=1,padx=(80,0),pady=(100,0))

target_label1=Label(lost,text="Target :",fg="white",bg="#17181a",font=("Roman",20,"bold"))
target_label1.grid(row=1,column=0,pady=(150,0),padx=(40,0))

target_score1=Label(lost,text="-",fg="white",bg="#17181a",font=("Roman",20,"bold"))
target_score1.grid(row=1,column=0,padx=(170,0),pady=(150,0))


score_label1=Label(lost,text="Score :",fg="white",bg="#17181a",font=("Roman",20,"bold"))
score_label1.grid(row=1,column=1,pady=(150,0),padx=(100,0))

score_score1=Label(lost,text="-",fg="white",bg="#17181a",font=("Roman",20,"bold"))
score_score1.grid(row=1,column=1,pady=(150,0),padx=(220,0))

play_again1=Button(lost,text="Play again",fg="white",bg="#17181a",font=("Roman",15,"bold"),command=lambda:window_frame(game_window))
play_again1.grid(row=2,column=0,pady=(210,0),padx=(50,0))
play_again1["border"]=0

exit_ga1=Button(lost,text="Exit",width=6,fg="white",bg="#17181a",font=("Roman",15,"bold"),command=lambda:window_frame(start_frame))
exit_ga1.grid(row=2,column=1,pady=(210,0),padx=(100,0))
exit_ga1["border"]=0

#start frame1

start_frame=LabelFrame(root)
start_frame.grid(row=0,column=0,sticky="nsew")
start_frame["border"]=0

img=Image.open("./Images/R.jpeg")    
img=ImageTk.PhotoImage(img.resize((500,700)))         
img_label=Label(start_frame,image=img)     
img_label.place(x=0,y=0,relwidth=1,relheight=1)
img_label["border"]=0

play=Button(start_frame,text="PLAY",bg="black",fg="white",command=lambda:window_frame(game_window))
play.grid(row=0,column=0,ipady=5,ipadx=10,pady=(370,0),padx=(35,0))
play["border"]=0
game_inst=Button(start_frame,text="GAME INSTRUCTIONS",bg="black",fg="white",command=lambda:window_frame(frame2))
game_inst.grid(row=1,column=0,ipady=5,ipadx=10,pady=(20,0),padx=(35,0))
game_inst["border"]=0
quit=Button(start_frame,text="QUIT",bg="black",fg="white",command=screen_end)
quit.grid(row=2,column=0,ipady=5,ipadx=10,pady=(20,0),padx=(35,0))
quit["border"]=0


#extra

prev_btn=Button(frame2,text="Back to MainMenu",font=("san serif",10),bg="black",fg="white",command=lambda:prev(start_frame))
prev_btn.grid(row=9,column=1,padx=(10,0),pady=(20,0))



pygame.mixer.music.load("./Audio/main_music.mp3")
pygame.mixer.music.play(loops=-1)

#logic part

def window_frame(frame):                #after clicking button(not every) in which frame application have to go.
    
    global counter,chances,tell_page
    tell_page=0
    chances=0
    counter=-1
    answer.delete(0,"end")
    pygame.mixer.music.load("./Audio/click-button.mp3")
    pygame.mixer.music.play(loops=0)
    if frame==start_frame:
        pygame.mixer.music.load("./Audio/main_music.mp3")
        pygame.mixer.music.play(loops=-1)

    frame.tkraise()
    if frame==game_window:
        score_no["text"]=0
        obj=open("words.csv","r")
        f=csv.reader(obj)
        for i in f:
            question["text"]=i[0]
            break
        obj.close()


def fun_confirm(ans_val):
    global tell_page,chances
    check=False
    pygame.mixer.music.load("./Audio/click-button.mp3")
    pygame.mixer.music.play(loops=0)
    if ans_val=="":
        messagebox.showinfo("Error","Please Enter Something...")
    
    else:                             

        obj=open("words.csv","r")
        f=csv.reader(obj)
        

        if tell_page<11:
            
            for i in f:
                if question["text"]==i[0] and ans_val.lower()==i[1]:
                    check=True
                    break

            if check==True:                     #if answer is right
                total=int(score_no["text"])+3
                score_no["text"]=str(total)
                tell_page=tell_page+1
                for j in f:
                    question["text"]=j[0]
                    break
                answer.delete(0,"end")
                chances=0
                if tell_page==11:
                    if int(score_no["text"])>int(target_no["text"]):
                        pygame.mixer.music.load("./Audio/game-win.mp3")
                        pygame.mixer.music.play(loops=0)
                        game_win.tkraise()
                        target_score["text"]=target_no["text"]
                        score_score["text"]=score_no["text"]

                    else:
                        pygame.mixer.music.load("./Audio/game-lost.mp3")
                        pygame.mixer.music.play(loops=0)
                        lost.tkraise()
                        target_score1["text"]=target_no["text"]
                        score_score1["text"]=score_no["text"]
                        

            else:                             #if answer is wrong
                chances=chances+1
                total=int(score_no["text"])-1
                score_no["text"]=str(total)
                if chances>=3:
                    lost.tkraise()
                    pygame.mixer.music.load("./Audio/game-lost.mp3")
                    pygame.mixer.music.play(loops=0)
                    target_score1["text"]=target_no["text"]
                    score_score1["text"]=score_no["text"]

        obj.close()


def hint_win():

    global counter,tell_page
    pygame.mixer.music.load("./Audio/click-button.mp3")
    pygame.mixer.music.play(loops=0)

    if counter!=tell_page:
        obj=open("words.csv","r")
        f=csv.reader(obj)

        for i in f:
            if question["text"]==i[0]:
                messagebox.showinfo("Hint",i[2])
                break
        obj.close()
    else:
        messagebox.showinfo("Limit over","You have utilized your hint...")
    counter=tell_page



def prev(frame):

    pygame.mixer.music.load("./Audio/click-button.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.load("./Audio/main_music.mp3")
    pygame.mixer.music.play(loops=-1)
    frame.tkraise()


root.mainloop()
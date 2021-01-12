from tkinter import *
import random

cpu_moves = ["Rock","Paper","Scissors"]
player_score = 0
cpu_score = 0
Sc_before = "Score before this round: "
Sc_after = "Score after this round: "

def disabled():
    brock.configure(state="disabled")
    bpaper.configure(state="disabled")
    bscissors.configure(state="disabled")
    bplay_again.configure(state="normal")


def display_score_before():
    global player_score
    global cpu_score
    lbscore.insert(END,Sc_before)
    lbscore.insert(END,"Player: "+str(player_score))
    lbscore.insert(END,"CPU: "+str(cpu_score))

def display_score_after():
    global player_score
    global cpu_score
    lbscore.insert(END,Sc_after)
    lbscore.insert(END,"Player: "+str(player_score))
    lbscore.insert(END,"CPU: "+str(cpu_score))

def cpu_turn():
    return random.randint(0,2)

def clear_move():
    tplayer.delete("1.0",END)
    tcpu.delete("1.0",END)
    lbscore.delete(0,END)

def rock_player():
    clear_move()
    global player_score
    global cpu_score
    if player_score == 10:
        lbscore.delete(0,END)
        lbscore.insert(END,"Player Wins!!!!!")
        disabled()
    elif cpu_score == 10:
        lbscore.delete(0,END)
        lbscore.insert(END,"CPU Wins!!!!!")
        disabled()
    else:
        display_score_before()
        tplayer.insert(END,"Rock")
        i = cpu_turn()
        tcpu.insert(END,cpu_moves[i])
        if cpu_moves[i] == "Scissors":
            player_score+=1
            display_score_after()
        elif cpu_moves[i] == "Paper":
            cpu_score+=1
            display_score_after()
        elif cpu_moves[i] == "Rock":
            display_score_after()
        else:
            pass



def paper_player():
    clear_move()
    global player_score
    global cpu_score
    if player_score == 10:
        lbscore.delete(0,END)
        lbscore.insert(END,"Player Wins!!!!!")
        disabled()
    elif cpu_score == 10:
        lbscore.delete(0,END)
        lbscore.insert(END,"CPU Wins!!!!!")
        disabled()
    else:
        display_score_before()
        tplayer.insert(END,"Paper")
        i = cpu_turn()
        tcpu.insert(END,cpu_moves[i])
        if cpu_moves[i] == "Rock":
            player_score+=1
            display_score_after()
        elif cpu_moves[i] == "Scissors":
            cpu_score+=1
            display_score_after()
        elif cpu_moves[i] == "Paper":
            display_score_after()
        else:
            pass

def scissors_player():
    clear_move()
    global player_score
    global cpu_score
    if player_score == 10:
        lbscore.delete(0,END)
        lbscore.insert(END,"Player Wins!!!!!")
        disabled()
    elif cpu_score == 10:
        lbscore.delete(0,END)
        lbscore.insert(END,"CPU Wins!!!!!")
        disabled()
    else:
        display_score_before()
        tplayer.insert(END,"Scissors")
        i = cpu_turn()
        tcpu.insert(END,cpu_moves[i])
        if cpu_moves[i] == "Paper":
            player_score+=1
            display_score_after()
        elif cpu_moves[i] == "Rock":
            cpu_score+=1
            display_score_after()
        elif cpu_moves[i] == "Scissors":
            display_score_after()
        else:
            pass

def play_again():
    global player_score
    global cpu_score
    brock.configure(state="normal")
    bpaper.configure(state="normal")
    bscissors.configure(state="normal")
    bplay_again.configure(state="disabled")
    player_score = 0
    cpu_score = 0
    lbscore.delete(0,END)

window = Tk()

window.title("Rock Paper Scissors")

brock = Button(window,text="Rock",height=3,width=6,command=rock_player)
brock.grid(row=0,column=0,rowspan=3,columnspan=3)

bpaper = Button(window,text="Paper",height=3,width=6,command=paper_player)
bpaper.grid(row=3,column=0,rowspan=3,columnspan=3)

bscissors = Button(window,text="Scissors",height=3,width=6,command=scissors_player)
bscissors.grid(row=6,column=0,rowspan=3,columnspan=3)

tplayer = Text(window,height=2,width=12)
tplayer.grid(row=2,column=7,rowspan=2,columnspan=6)

lplayer = Label(window,text="Player")
lplayer.grid(row=1,column=7)

lcpu = Label(window,text="CPU")
lcpu.grid(row=7,column=7)

tcpu= Text(window,height=2,width=12)
tcpu.grid(row=5,column=7,rowspan=2,columnspan=6)

lbscore = Listbox(window,height=11,width=30)
lbscore.grid(row=0,column=14,rowspan=9,columnspan=6)

bplay_again = Button(window,text="Play again",command=play_again,state="disabled")
bplay_again.grid(row=9,column=0)

window.mainloop()
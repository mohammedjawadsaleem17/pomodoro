#Bismillah ir-rahmaan ir-raheem

import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#D21312"
RED = "#e7305b"
GREEN = "#FDF4F5"
YELLOW = "#4A55A2"
WHITE="#FFF4F4"
FONT_NAME = "Courier"
WORK_MIN = 0.001
SHORT_BREAK_MIN = 0.001
LONG_BREAK_MIN = 20
reps=0
timer=None


# ---------------------------- TIMER RESET ------------------------------- #

#Reset Function
def reset_timer():
    try:
        windows.after_cancel(timer)
        canvas.itemconfig(timer_text,text="00:00")
        label.config(text="Timer",fg="#27374D")
        mark.config(text="")
    except:
        pass


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        #Long BreaK

        count_down(long_break_sec)
        label.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

#---------------------------- COUNT-DOWN MECHANISSM------------------#
def count_down(count):

    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = windows.after(1000,count_down,count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        marks=""
        for _ in range(work_sessions):
            marks+="✔"
        mark.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.title("Pomodoro")
windows.config(padx=100,pady=50,bg=YELLOW)

#Implementing Label
label = Label(text="Timer")
label.config(fg="#ACBCFF",bg=YELLOW,font=(FONT_NAME,32,"bold"))
label.grid(column=2,row=1)

canvas = Canvas(width=200,height=224,bg=YELLOW)

tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"), )
canvas.config(highlightthickness=0)


#Implementing Start and Reset Button
startbutton = Button(text="Start",highlightthickness=0)
startbutton.config(fg=PINK,font=("Times",11),width=6,command=start_timer,)
startbutton.config(width=7, height=1, bg="#537188", fg="#FFFAF4", font=("Arial", 12, "bold"))

resetButton = Button(text="Reset",highlightthickness=0)

startbutton.grid(column=1,row=3)
resetButton.grid(column=3,row=3)
resetButton.config(fg=PINK,font=("Times",11),width=6,command=reset_timer)
resetButton.config(width=7, height=1, bg="#537188", fg="#FFFAF4", font=("Arial", 12, "bold"))

canvas.grid(column=2,row=2)


#Implementing Tick mark✔
mark ="✔"


mark = Label(background=YELLOW,fg=GREEN)
mark.grid(column=2,row=4)

thanks = Label(text="Alhamdulillah")
thanks.grid(column=2,row=5)
thanks["fg"]="#ECC9EE"
thanks["bg"]="#4A55A2"

Namelabel = Label()
Namelabel["text"]="Developed by Mohammed Jawad Saleem"
Namelabel.grid(row=6,column=2)
Namelabel["fg"]="#ECC9EE"
Namelabel["bg"]="#4A55A2"
windows.mainloop()








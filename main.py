from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
resp = 0
thickMark = "✅"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def ResetTimer():
    global resp
    global thickMark
    resp = 0
    thickMark = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Set Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global thickMark
    global resp
    resp+=1
    workTime_second = WORK_MIN*60
    long_break_second = LONG_BREAK_MIN*60
    short_break_second = SHORT_BREAK_MIN*60
    if resp%2==1:
        counter(workTime_second)
        label.config(text="Work Time",fg=GREEN)
    elif resp%2==0:
        counter(short_break_second)
        label.config(text="Short Break",fg=RED)
        thick.config(text=thickMark)
        thickMark+="✅"
    else:
        counter(long_break_second)
        label.config(text="Long Break",fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    count_min = math.floor(count/60) # converting second to minute
    count_second = count%60 # Calculating how many seconds are left
    if count_second==0:
        count_second = "00"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_second}")
    if count>0:
        global timer
        timer = window.after(1000,counter,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(bg=YELLOW,padx=100,pady=50)

# Creating Canvas
canvas = Canvas(width=200,height=230,background=YELLOW,borderwidth=5,highlightthickness=0)
# Adding image to it
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(105,115,image=tomatoImage) # we want image to be in the center of the canvas so we place it at the half of its coordinate
# Creating Clock Text
timer_text = canvas.create_text(105,130,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(column=1,row=1)
# Creating Widget

label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,40,"bold"),background=YELLOW,highlightthickness=0)
label.grid(column=1,row=0)
start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)
reset_button = Button(text="Reset",command=ResetTimer)
reset_button.grid(column=2,row=2)
thick = Label(text="")
thick.grid(column=1,row=3)



window.mainloop()
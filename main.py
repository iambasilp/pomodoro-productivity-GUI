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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(1*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count/60)
    count_second = count % 60                   # it Turns 4.526 to 4
    if count_second < 10:   #int  Dynamic Typing its loop reasigning
        count_second = f"0{count_second}" #string  Dynamic Typing its loop reasigning

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}") #we replaced canvas so canvas.itemconfig funnction          # 245/60 =4 minute
    if count > 0:                                                                                         #245%60 = seconds
        window.after(1000, count_down, count-1) #after 1000 (1 sec) count_down fun call with count-1

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_loc = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_loc) # height and width of the image
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)



#label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(text="D", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

#Button
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0)
button_reset.grid(column=2, row=2)

window.mainloop()

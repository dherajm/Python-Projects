from tkinter import *
import math
import tkinter.messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.020
CYCLE = 0

timer = None
marks = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global CYCLE

    window.after_cancel(timer)
    check_mark.config(text="")
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50), highlightthickness=0)
    canvas.itemconfig(timer_count, text="00:00")
    CYCLE = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_pomodoro():
    global CYCLE

    CYCLE += 1

    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if CYCLE % 2 != 0:
        tkinter.messagebox.showinfo(title="Work", message="Start working~")
        count_down(work_time)
        timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50), highlightthickness=0)
    elif CYCLE % 8 == 0:
        tkinter.messagebox.showinfo(title="Break", message="Long break!")
        count_down(long_break)
        timer_label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50), highlightthickness=0)
    else:
        tkinter.messagebox.showinfo(title="Work", message="Small break!")
        count_down(short_break)
        timer_label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50), highlightthickness=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_pomodoro()

        global marks
        marks = ""
        work_sessions = math.floor(CYCLE / 2)
        for i in range(work_sessions):
            marks += "✔"

        check_mark.config(text=marks, fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW, highlightthickness=0)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)

# UI
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_count = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Label
timer_label = Label(window, text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50), highlightthickness=0)
timer_label.grid(row=0, column=1)

# Start Button
start_button = Button(window, text="Start", bg=YELLOW, highlightthickness=0, command=start_pomodoro)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(window, text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=3)

# Check Mark
check_mark = Label(window, fg=GREEN, font=(FONT_NAME, 30, "bold"), highlightthickness=0, bg=YELLOW)
check_mark.grid(row=4, column=1)

# Main Loop
window.mainloop()

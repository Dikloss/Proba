from  tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t=0

def set():
    global t
    rem = sd.askstring("Время напоминиания", "ВВедите время напоминания в формате чч.мм (в 24-часавом формате")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute)
            print(dt)
            t = dt.timestamp()
            print(t)
        except Exception as e:
            mb.showinfo("Ошибка!", f"Произощла ошибка {e}")


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play.snd()
            t = 0
    window.after(10000, check)





window = Tk()
window.title("Напоминание")
label = Label(text="Установить напоминание")
label.pack(pady=10)
set_button = Button(text="Установить напоминание",command=set)
set_button.pack()

window.mainloop()

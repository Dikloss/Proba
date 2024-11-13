from  tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from pygame import mixer
import datetime
import time


t = 0
music = False


def sett():
    global t, rem_text
    rem_time = sd.askstring("Время напоминания","Введите время напоминания в формате ЧЧ:ММ (в 24-часовом формате):")
    if rem_time:
        try:
            hour = int(rem_time.split(":")[0])
            minute = int(rem_time.split(":")[1])
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0)
            t = dt.timestamp()
            rem_text = sd.askstring("Текст напоминания","Введите текст напоминания:")
            label.config(text=f"Напоминание на {hour:02}:{minute:02} с текстом: {rem_text}",font=("Helvecia", 14))
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
    window.after (10000, check)


def play_snd():
    global music
    music = True
    mixer.init()
    mixer.music.load('R.mp3')
    mixer.music.play()


def stop_music():
    global music
    if music:
        mixer.music.stop()
        music = False
    label.config(text="Установить новое напоминание")

window = Tk()
window.title ("Напоминание со звуком")
window.geometry("400x200")

label = Label(text="Установите напоминание", font=("Helvecia", 14))
label.pack(pady=20)

set_button = Button(text="Установить напоминание",font=("Helvecia", 14), command=sett)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку",font=("Helvecia", 14), command=stop_music)
stop_button.pack(pady=10)

check()

window.mainloop()
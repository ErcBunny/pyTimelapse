import tkinter
import time
import threading
import datetime
import os
import subprocess
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.cron import CronTrigger

num = 0
paused = False
text = tkinter.StringVar()

def count():
    global num, text
    if paused == False:
        num += 1
        text.set(num)
    print('console output')

def pause():
    global paused
    paused = True
    print('paused')

def start():
    global paused
    paused = False
    print('starting')


if __name__ == "__main__":
    
    scheduler = BackgroundScheduler()
    Trigger1 = IntervalTrigger(seconds=1)
    Trigger2 = CronTrigger(minute="*/30", second="0")
    scheduler.add_job(count, Trigger1, id='0')
    scheduler.start()

    window = tkinter.Tk()
    window.title('window name')
    window.geometry('585x350')
    label = tkinter.Label(window, textvariable=text)
    button_p = tkinter.Button(window, text='pause', command=pause)
    button_s = tkinter.Button(window, text='start', command=start)

    button_p.pack()
    button_s.pack()
    label.pack()

    window.mainloop()


# reference https://xugaoxiang.com/2020/07/17/python-module-apscheduler/

import time
import datetime
import os
import subprocess

from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.cron import CronTrigger


def my_job():
    print('taking a picture, {}'.format(time.ctime()))
    os.system("adb shell input keyevent 26")
    time.sleep(1)
    # p = subprocess.Popen(['scrcpy', '-b', '2M'])
    # time.sleep(1)
    os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA")
    time.sleep(1)
    os.system("adb shell input keyevent 27")
    time.sleep(1)
    os.system("adb shell input keyevent 3")
    time.sleep(1)
    os.system("adb shell input keyevent 26")
    # p.kill()
    print("success")
    



if __name__ == "__main__":
 
    # 定时器类型: 后台方式相当于多线程
    scheduler2 = BackgroundScheduler()

    # 间隔设置为1秒，还可以使用minutes、hours、days、weeks等
    Trigger1 = IntervalTrigger(seconds=10)
    Trigger2 = CronTrigger(minute="*/30", second="0")

    # 给作业设个id，方便作业的后续操作，暂停、取消等
    scheduler2.add_job(my_job, Trigger2, id='0')
    scheduler2.start()
    print('=== successfully added tasks ===')
    start_time = time.time()
    while True:
        input("=== Enter to check status ===\n")
        current_time = time.time()
        formated_time = time.asctime(time.localtime(current_time))
        delta = int(current_time - start_time)
        t_sec = delta % 60
        t_min = (delta // 60) % 60
        t_hour = (delta // 3600) % 24
        t_day = (delta // (3600 * 24))
        print("Current time is %s." % formated_time)
        print("This script has been running for %d day(s) %d hour(s) %d min(s) %d sec(s)." % (t_day, t_hour, t_min, t_sec))
        

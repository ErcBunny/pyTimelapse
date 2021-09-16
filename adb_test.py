import time
import datetime
import os
import subprocess

from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.cron import CronTrigger


# print("taking a picture, {}".format(time.ctime()))
# os.system("adb shell input keyevent 26")
# time.sleep(1)
#p = subprocess.Popen(["scrcpy", "-b", "2M"])
# # time.sleep(1)
# os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA")
# time.sleep(1)
# os.system("adb shell input keyevent 27")
# time.sleep(1)
# os.system("adb shell input keyevent 3")
# time.sleep(1)
# os.system("adb shell input keyevent 26")
# # p.kill()
# print("success")
    
# myfilename = os.popen("adb shell ls -t /sdcard/DCIM/Camera/ | head -n 1 | tr -d "\n" ").read()
# print("--")
# print(myfilename) 
# print("--") #debug看看前后是否有换行符

def start_camera():
    os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA")

def switch_ultrawide():
    os.system("adb shell input tap 420 1600")

def take_a_picture():
    os.system("adb shell input keyevent 27")

def switch_108M():
    os.system("adb shell input tap 760 1800")

def return_home():
    os.system("adb shell input keyevent 3")
    os.system("adb shell input tap 320 2280")
    os.system("adb shell input tap 530 2000")

def power_button():
    os.system("adb shell input keyevent 26")

def func1():
    p = subprocess.run(["adb", "shell", "input", "keyevent", "26"])
    p = subprocess.run(["adb", "shell", "am", "start", "-a", "android.media.action.STILL_IMAGE_CAMERA"])
    p = subprocess.run(["adb", "shell", "input", "keyevent", "27"])
    p = subprocess.run(["adb", "shell", "input", "keyevent", "3"])
    p = subprocess.run(["adb", "shell", "input", "keyevent", "26"])

def func2():
    p = subprocess.run(["adb", "shell", "input", "keyevent", "27"])

def func3():
    os.system("adb shell input keyevent 26")
    os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA")
    os.system("adb shell input tap 735 1800")
    time.sleep(1.5)
    os.system("adb shell input keyevent 27")
    os.system("adb shell input keyevent 3")
    os.system("adb shell input tap 320 2280")
    os.system("adb shell input tap 530 2000")
    os.system("adb shell input keyevent 26")

def func4():
    myfilename = os.popen("adb shell ls -t /sdcard/DCIM/Camera/ | head -n 1 | tr -d '\n' ").read()
    print(myfilename)
    return myfilename

def savefile(type, filename):
    os.system("adb pull /sdcard/DCIM/Camera/" + filename + " ./" + type + "/" + filename)


if __name__ == "__main__":
    # power_button()
    # start_camera()
    # time.sleep(1)
    # switch_ultrawide()
    # time.sleep(2)
    # take_a_picture()
    # time.sleep(2)
    # ultrawide = func4()
    # switch_108M()
    # time.sleep(2)
    # take_a_picture()
    # time.sleep(5)
    # wide108 = func4()
    # return_home()
    # power_button()
    # savefile("ULTRAWIDE", ultrawide)
    # savefile("108MP", wide108)
    myfilename = os.popen("adb shell ls -t /sdcard/DCIM/Camera/ | head -n 1 | tr -d '\n'").read()
    print(myfilename[-1])
    print(myfilename[-2])
    print(myfilename[-3])
    
    
    

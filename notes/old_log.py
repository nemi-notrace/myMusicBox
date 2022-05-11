#!/usr/bin/python3

import datetime
import time as t
import RPi.GPIO as GPIO
import io, os

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def log_input(str):
    outfile = open(filename, 'a')
    ts = t.time()
    sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S - ')
    outfile.write(sttime + str + "\n")
    outfile.close()
    t.sleep(0.01)


filename = "GPIO.log"

start = t.time()


def gpio_func(i):
    switcher = {
        3: 'IO',
        17: 'Volume Up',
        27: 'Play/Pause',
        22: 'Previous',
        19: 'Said Something',
        23: 'Next',
        24: 'Volume down',
        16: 'Calender'
    }
    return switcher.get(i, "Invalid GPIO channel")


def my_callback(channel):
    global start
    if GPIO.input(channel):
        stopped = t.time() - start
        log_input(gpio_func(channel) + " pressed for " + str(round(stopped, 2)) + "s")
        t.sleep(0.3)
    else:
        start = t.time()


GPIO.add_event_detect(16, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(19, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(3, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(17, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(27, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(22, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(23, GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(24, GPIO.BOTH, callback=my_callback)

tty = io.TextIOWrapper(
    io.FileIO(
        os.open(
            "/dev/tty0",
            os.O_NOCTTY | os.O_RDWR),
        "r+"))

for line in iter(tty.readline, None):
    log_input("RFID-Tag read ")

while True:
    pass

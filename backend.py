from importlib.resources import path
import RPi.GPIO as GPIO
from vlc import Instance
import time
import os
from subprocess import call

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

play_flag = 0
playing_album = 0

path_album_one = r"/home/pi/1"
path_album_tow = r"/home/pi/2"
path_album_three = r"/home/pi/3"


class VLC:
    def __init__(self):
        self.Player = Instance('--loop')

    def addPlaylist(self, path):
        self.mediaList = self.Player.media_list_new()
        songs = os.listdir(path)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path, s)))
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)

    def play(self):
        self.listPlayer.play()

    def next(self):
        self.listPlayer.next()

    def pause(self):
        self.listPlayer.pause()

    def previous(self):
        self.listPlayer.previous()

    def stop(self):
        self.listPlayer.stop()



def gpio_control(channel, path):

    global play_flag
    global playing_album

    if GPIO.input(channel) == GPIO.LOW and play_flag == 1 and channel != playing_album and path != "volup" and path != "voldown":
        p.stop()
        p.addPlaylist(path)
        playing_album = channel
        p.play()
        time.sleep(0.3)

    if GPIO.input(channel) == GPIO.LOW and play_flag == 0 and path != "volup" and path != "voldown":
        p.addPlaylist(path)
        play_flag = 1
        playing_album = channel
        p.play()
        time.sleep(0.3)

    if GPIO.input(channel) == GPIO.LOW and play_flag == 1 and playing_album == channel and path != "volup" and path != "voldown":
        play_flag = 0
        playing_album = 0
        p.stop()
        time.sleep(0.3)

    if GPIO.input(channel) == GPIO.LOW and path == "volup":
        call(["/usr/bin/amixer", "-q", "-M", "set", "Headphone", "3%+"])

    if GPIO.input(channel) == GPIO.LOW and path == "voldown":
        call(["/usr/bin/amixer", "-q", "-M", "set", "Headphone", "3%-"])

p = VLC()

while True:
    if GPIO.input(17) == GPIO.LOW:
        gpio_control(17, path_album_one)
    if GPIO.input(22) == GPIO.LOW:
        gpio_control(22, path_album_tow)
    if GPIO.input(27) == GPIO.LOW:
        gpio_control(27, path_album_three)
    
    if GPIO.input(23) == GPIO.LOW:
        gpio_control(23, "volup")

    if GPIO.input(24) == GPIO.LOW:
        gpio_control(24, "voldown")


    else:
        pass

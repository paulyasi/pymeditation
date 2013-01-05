# meditation timer in python
#
# The python source code is released under the MIT license
# The tinsha.wav file referenced here is available on many buddhist websites
# The license of that file is unknown
#
# Copyright (c) 2013 Paul Yasi <paulyasi.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is furnished 
# to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.


import pygame as pg
from pygame.locals import *
from sys import exit

pg.init()

def play_sound(sound_file):
    """
    will load the whole sound into memory before playback
    """
    sound = pg.mixer.Sound(sound_file)
    clock = pg.time.Clock()
    sound.play()
    # how often to check active playback
    frame_rate = 30
    while pg.mixer.get_busy():
        clock.tick(frame_rate)


FREQ = 18000   # play with this for best sound
BITSIZE = -16  # here unsigned 16 bit
CHANNELS = 2   # 1 is mono, 2 is stereo
BUFFER = 1024  # audio buffer size, number of samples

pg.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)

# pick a wave (.wav) sound file you have
#sound_file = "Chimes.wav"
sound_file = "tinsha.wav"

my_font = pg.font.SysFont("arial", 28)

screen = pg.display.set_mode((240,185), 0, 24)

pg.display.set_caption("Py Meditation Timer");

# set the background screen to white
screen.fill((255,255,255))

# initialize mouse values
mouse_x, mouse_y = pg.mouse.get_pos()
leftbutton, middlebutton, rightbutton = pg.mouse.get_pressed()

while True:
    # event loop
    for event in pg.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEMOTION:
            mouse_x, mouse_y = pg.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            leftbutton, middlebutton, rightbutton = pg.mouse.get_pressed()
            mouse_x, mouse_y = pg.mouse.get_pos()
        if event.type == MOUSEBUTTONUP:
            leftbutton, middlebutton, rightbutton = pg.mouse.get_pressed()
            
        # fill white over everyting
        screen.fill((255,255,255))
        
        # draw 1 minute button
        oneminutes = pg.Rect(5, 5, 230, 40)
        pg.draw.rect(screen, (0,0,0), oneminutes, 1)
        text = my_font.render("Meditate 1 Minute", True, (0,0,0))
        screen.blit(text,(7,7))
        
        # draw 5 minute button
        fiveminutes = pg.Rect(5, 50, 230, 40)
        pg.draw.rect(screen, (0,0,0), fiveminutes, 1)
        text = my_font.render("Meditate 5 Minutes", True, (0,0,0))
        screen.blit(text,(7,52))
        
        # draw 10 minute button
        tenminutes = pg.Rect(5, 95, 230, 40)
        pg.draw.rect(screen, (0,0,0), tenminutes, 1)
        text = my_font.render("Meditate 10 Minutes", True, (0,0,0))
        screen.blit(text,(7,97))
        
        # draw 15 minute button
        fifteenminutes = pg.Rect(5, 140, 230, 40)
        pg.draw.rect(screen, (0,0,0), fifteenminutes, 1)
        text = my_font.render("Meditate 15 Minutes", True, (0,0,0))
        screen.blit(text,(7,142))

        
        # check if you clicked on something
        if leftbutton & oneminutes.collidepoint((mouse_x,mouse_y)):
            screen.fill((255,255,255))
            text = my_font.render("1 Minute", True, (0,0,0))
            screen.blit(text,(70,100))
            pg.display.update()
            pg.time.delay(60000)
            play_sound(sound_file)
        if leftbutton & fiveminutes.collidepoint((mouse_x,mouse_y)):
            screen.fill((255,255,255))
            text = my_font.render("5 Minutes", True, (0,0,0))
            screen.blit(text,(70,100))
            pg.display.update()
            pg.time.delay(300000)
            play_sound(sound_file)
        if leftbutton & tenminutes.collidepoint((mouse_x,mouse_y)):
            screen.fill((255,255,255))
            text = my_font.render("10 Minutes", True, (0,0,0))
            screen.blit(text,(70,100))
            pg.display.update()
            pg.time.delay(600000)
            play_sound(sound_file)
        if leftbutton & fifteenminutes.collidepoint((mouse_x,mouse_y)):
            screen.fill((255,255,255))
            text = my_font.render("15 Minutes", True, (0,0,0))
            screen.blit(text,(70,100))
            pg.display.update()
            pg.time.delay(900000)
            play_sound(sound_file)

        pg.display.update()

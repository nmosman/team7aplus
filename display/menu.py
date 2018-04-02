#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

from bluetooth import *
import time
import sys
import math
import time
import numpy as np
from luma.core.render import canvas
from luma.core.sprite_system import framerate_regulator
# For connecting to the physical device
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306


bd_addr = "00:21:13:04:50:F4"
port = 1
sock = BluetoothSocket (RFCOMM)
sock.connect((bd_addr,port))


def radians(degrees):
    return degrees * 3.14 / 180


def bounce_animation():
    origin = 0
    while True:
        yield -abs(math.sin(radians(origin)))
        origin = (origin + 13.5) % 360 # Essentially same as += 1 for sin
        
def sigmoid(x):
    return 1 / (1 + math.exp(10.895 - 0.0219*x))


def main():
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial)
    
    

    while True:
        prev_time = time.time()

        count = 1000
        heart_data = []
        for i in range(50):
            heart_data.append(0.5)

        ha = bounce_animation()

        prev_x = 0
        prev_y = 0

            
        while True:
            print("here")
            data = ""
            #data = "100"
            try:
                data = sock.recv(5).decode("ascii")
            except:
                data = ""
            
            while True:
             if (len(data) != 0):
                 if ((data[0] == "c" and data[-1] == "d")):
                     break
                 else:
                    try:
                        data = sock.recv(5).decode("ascii")
                    except:
                        data = ""
                    print("not working {}".format(data))
 
            print(data[1:-1])
            data = sigmoid(int(data[1:-1]))
            print(data)
            heart_data.append(data)
            heart_data = heart_data[1:]
            
            heart_detected = True
            with canvas(device, dither=True) as draw:
                if heart_detected:
                    draw.text((10,4), "Reading heart data")
                else:
                    draw.text((10,4), "No heart data detected")
                    
                # Menu options
                for i, el in enumerate(heart_data):
                    if i % 1 == 0:
                        x = int(i*2 + 55)
                        y = device.height - (device.height - 17) * el
                        if i != 0:
                            draw.polygon((x, y, prev_x, prev_y), fill="white")
                        prev_x, prev_y = x,y

                

                # Animation
                x, y = (15, 32)
                radius = 4
                anim = next(ha) # Get the next location & scale for the heart sprite
                y_anim = anim * 15 + y
                scale = anim * 15 + 15

                # The heart
                draw.ellipse((x, y_anim, x+2*radius, y_anim+2*radius), outline="white", fill="white")
                draw.ellipse((x+2*radius, y_anim, x+4*radius, y_anim+2*radius), outline="white", fill="white")
                draw.polygon([(x, y_anim+1.48*radius), (x+4*radius, y_anim+1.48*radius), (x+2*radius, y_anim+4*radius)], outline="white", fill="white")
                # The shadow
                draw.ellipse((x+radius-scale/2, y+6*radius, x+3*radius+scale/2, y+7*radius), outline="white", fill="white")





if __name__ == "__main__":
    main()



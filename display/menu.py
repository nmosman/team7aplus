#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

import sys
import math
import time
import numpy as np
from time import sleep
from luma.core.render import canvas
from luma.core.sprite_system import framerate_regulator
from demo_opts import get_device


# For connecting to the physical device
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306


def radians(degrees):
    return degrees * 3.14 / 180


def bounce_animation():
    origin = 0
    while True:
        yield -abs(math.sin(radians(origin)))
        origin = (origin + 3.5) % 360 # Essentially same as += 1 for sin


sigmoid = lambda x: (1 / (1 + np.exp(10.985 - 0.0219*x)))


def main():
    # serial = i2c(port=1, address=0x3C)
    # device = ssd1306(serial)
    device = get_device()

    while True:
        prev_time = time.time()

        count = 1000
        heart_data = []
        for i in range(50):
            count += 1
            val = (np.sin(count) + 1) / 2
            val += (np.sin(count*2+80) + 1) / 2
            heart_data.append(val)

        ha = bounce_animation()

        prev_x = 0
        prev_y = 0

        while (time.time() - prev_time) < 100000:
            with canvas(device, dither=True) as draw:
                count += 1

                val = (np.sin(count) + 1) / 2
                val += (np.sin(count*2+80) + 1) / 2
                val += (np.sin(count/4+10) + 1) / 2
                heart_data.append(val)
                heart_data = heart_data[1:]


                # Menu options
                for i, el in enumerate(heart_data):
                    # if i % 10 == 0:
                    x = int(2*i + 55)
                    y = (device.height/3 - 1) * el
                    if i != 0:
                        draw.polygon((x, y, prev_x, prev_y), fill="white")
                    prev_x, prev_y = x,y


                # Animation
                x, y = (15, 23)
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



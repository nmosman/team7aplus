#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

import sys
import math
from time import sleep
from demo_opts import get_device
from luma.core.render import canvas
from luma.core.sprite_system import framerate_regulator


def radians(degrees):
    return degrees * 3.14 / 180


def bounce_animation():
    origin = 0
    while True:
        yield -abs(math.sin(radians(origin)))
        origin = (origin + 3.5) % 360 # Essentially same as += 1 for sin


class Menu(object):
    """docstring for Menu"""
    def __init__(self, menu_options):
        assert len(menu_options["options"]) <= 6 # Limit to 6 options
        self.options = menu_options
        self.ha = bounce_animation()

    def run(self, device, updated_options=None):
        if updated_options is not None:
            assert len(updated_options["options"]) <= 6 # Limit to 6 options
            self.options = updated_options

        with canvas(device, dither=True) as draw:
            # Menu options
            for i, option in enumerate(self.options["options"]):
                draw.text((50, 2+i*10), option, fill="white")
                if i == self.options["cursor"]:
                    draw.text((40, 2+i*10), ">", fill="white")

            x, y = (15, 23)
            radius = 4
    
            # Animation
            anim = next(self.ha) # Get the next location & scale for the heart sprite
            y_anim = anim * 15 + y
            scale = anim * 15 + 15

            # The heart
            draw.ellipse((x, y_anim, x+2*radius, y_anim+2*radius), outline="white", fill="white")
            draw.ellipse((x+2*radius, y_anim, x+4*radius, y_anim+2*radius), outline="white", fill="white")
            draw.polygon([(x, y_anim+1.48*radius), (x+4*radius, y_anim+1.48*radius), (x+2*radius, y_anim+4*radius)], outline="white", fill="white")
            # The shadow
            draw.ellipse((x+radius-scale/2, y+6*radius, x+3*radius+scale/2, y+7*radius), outline="white", fill="white")


if __name__ == "__main__":

    menu_options = {
        "options": ["Option 1", "Option 2", "85 bpm", "Option 4"],
        "cursor": 2,
    }

    try:
        device = get_device()
        m = Menu(menu_options)
        while True:
            m.run(device)
    except KeyboardInterrupt:
        pass

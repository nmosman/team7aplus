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


def heart_animation():
    heart_origin = 0
    shadow_scale = 1
    while True:
        yield -abs(math.sin(radians(heart_origin))), shadow_scale
        heart_origin = (heart_origin + 2) % 360 # Essentially same as += 1 for sin


class Menu(object):
    """docstring for Menu"""
    def __init__(self, menu_options):
        assert len(menu_options["options"]) <= 6 # Limit to 6 options
        self.options = menu_options
        self.ha = heart_animation()

    def run(self, device, updated_options=None):
        if updated_options is not None:
            assert len(updated_options["options"]) <= 6 # Limit to 6 options
            self.options = updated_options

        with canvas(device, dither=True) as draw:
            # Animation
            x, scale = next(self.ha) # Get the next location & scale for the heart sprite
            draw.text((15, x*20+30), "+", fill="white")
            # Menu options
            for i, option in enumerate(self.options["options"]):
                draw.text((50, 2+i*10), option, fill="white")
                if i == self.options["cursor"]:
                    draw.text((40, 2+i*10), ">", fill="white")


if __name__ == "__main__":

    menu_options = {
        "options": ["Option A", "Something b", "Other C", "Also D"],
        "cursor": 3,
    }

    try:
        device = get_device()
        m = Menu(menu_options)
        m.run()
    except KeyboardInterrupt:
        pass

# -*- coding: utf-8 -*-
from . import He
from . import Led

def start():
    he = He()
    he.hmm()

    led = Led()
    led.do_flash()

start()




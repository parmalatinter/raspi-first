# -*- coding: utf-8 -*-

from time import sleep

import RPi.GPIO as GPIO

class Led:
    def do_flash(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.OUT)

        while True:
            GPIO.output(25, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(25, GPIO.LOW)
            sleep(0.5)

test = Led()
test.do_flash()
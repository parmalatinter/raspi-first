# -*- coding: utf-8 -*-

import os
import time
import grovepi


class Led:

    # Digital ports that support Pulse Width Modulation (PWM)
    # D3, D5, D6

    # Digital ports that do not support PWM
    # D2, D4, D7, D8

    # Connect the Grove LED to digital port D5
    # SIG,NC,VCC,GND
    led = 0

    def __init__(self, led = 5):
        self.led = led
        grovepi.pinMode(self.led, "OUTPUT")

    def do_flash(self):
        print(1)
        
        time.sleep(1)
        i = 0

        is_loop = True

        while is_loop:
            try:
                # Reset
                if i > 255:
                    i = 0

                # Current brightness
                print (i)

                # Give PWM output to LED
                grovepi.analogWrite(self.led, i)

                # Increment brightness for next iteration
                i = i + 20
                time.sleep(.5)

            except KeyboardInterrupt:
                grovepi.analogWrite(self.led, 0)
                break
            except IOError:
                print ("Error")
                return False
            is_loop = os.environ.get('IS_PROD')
        return True

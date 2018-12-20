# -*- coding: utf-8 -*-

import os
import time
import grovepi


class Led_fade:
    def do_flash(self):

        # Connect the Grove Rotary Angle Sensor to analog port A0
        # SIG,NC,VCC,GND
        potentiometer = 0

        # Connect the LED to digital port D5
        # SIG,NC,VCC,GND
        led = 5

        grovepi.pinMode(potentiometer, "INPUT")
        grovepi.pinMode(led, "OUTPUT")
        time.sleep(1)

        # Reference voltage of ADC is 5v
        adc_ref = 5

        # Vcc of the grove interface is normally 5v
        grove_vcc = 5

        # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
        full_angle = 300

        is_loop = True

        while is_loop:
            try:
                # Read sensor value from potentiometer
                sensor_value = grovepi.analogRead(potentiometer)

                # Calculate voltage
                voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

                # Calculate rotation in degrees (0 to 300)
                degrees = round((voltage * full_angle) / grove_vcc, 2)

                # Calculate LED brightess (0 to 255) from degrees (0 to 300)
                brightness = int(degrees / full_angle * 255)

                # Give PWM output to LED
                grovepi.analogWrite(led, brightness)

                print("sensor_value = %d voltage = %.2f degrees = %.1f brightness = %d" % (
                sensor_value, voltage, degrees, brightness))
            except KeyboardInterrupt:
                grovepi.analogWrite(led, 0)
                break
            except IOError:
                print ("Error")
            is_loop = os.environ.get('IS_PROD')


test = Led_fade()
test.do_flash()
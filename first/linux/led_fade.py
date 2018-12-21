# -*- coding: utf-8 -*-

import os
import time
import grovepi


class Led_fade:

    # Connect the Grove Rotary Angle Sensor to analog port A0
    # SIG,NC,VCC,GND
    potentiometer = 0

    # Connect the LED to digital port D5
    # SIG,NC,VCC,GND
    led = 0

    # Reference voltage of ADC is 5v
    __adc_ref = 5

    # Vcc of the grove interface is normally 5v
    __grove_vcc = 5

    # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
    __full_angle = 300

    def __init__(self, potentiometer = 0, led = 5):
        self.potentiometer = potentiometer
        self.led = led

        grovepi.pinMode(self.potentiometer, "INPUT")
        grovepi.pinMode(led, "OUTPUT")

    def do_flash(self):

        time.sleep(1)



        is_loop = True

        while is_loop:
            try:
                # Read sensor value from potentiometer
                sensor_value = grovepi.analogRead(self.potentiometer)

                # Calculate voltage
                voltage = round((float)(sensor_value) * self.__adc_ref / 1023, 2)

                # Calculate rotation in degrees (0 to 300)
                degrees = round((voltage * self.__full_angle) / self.__grove_vcc, 2)

                # Calculate LED brightess (0 to 255) from degrees (0 to 300)
                brightness = int(degrees / self.__full_angle * 255)

                # Give PWM output to LED
                grovepi.analogWrite(self.led, brightness)

                print("sensor_value = %d voltage = %.2f degrees = %.1f brightness = %d" % (
                sensor_value, voltage, degrees, brightness))
            except KeyboardInterrupt:
                grovepi.analogWrite(self.led, 0)
                break
            except IOError:
                print ("Error")
                return False
            is_loop = os.environ.get('IS_PROD')
        return True


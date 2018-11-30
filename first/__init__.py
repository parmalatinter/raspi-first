import platform

from .he import He

if platform.system() == 'Linux' :
    from linux.led import Led
    from linux.led_fade import Led_fade
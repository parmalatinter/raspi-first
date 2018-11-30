# -*- coding: utf-8 -*-
import platform
if platform.system() == 'Linux' :

    from linux.he import He
    from linux.led import Led
    
    def start():
        he = He()
        he.hmm()
    
        led = Led()
        led.do_flash()
    
    start()
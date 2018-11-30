import platform
if platform.system() == 'Linux' :
	
	from .led import Led
	from .led_fade import Led_fade
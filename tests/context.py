# -*- coding: utf-8 -*-

import sys
import os
import platform

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if platform.system() == 'Linux' :
	sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../linux')))
	
import first

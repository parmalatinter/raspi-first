# -*- coding: utf-8 -*-
from .context import first

import unittest


class LedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        led = first.Led_fade()
        led.do_flash()

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
from .context import first

import unittest


class LedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        led = first.Led(5)
        res = led.do_flash()
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()

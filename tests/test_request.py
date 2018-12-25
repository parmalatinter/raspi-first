# -*- coding: utf-8 -*-
from .context import first

import unittest


class RequestTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        request = first.request()
        res = request.get('https://www.google.com')
        self.assertEquals(200, res.status_code)

if __name__ == '__main__':
    unittest.main()

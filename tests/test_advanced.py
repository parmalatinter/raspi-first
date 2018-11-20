# -*- coding: utf-8 -*-

from .context import first

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        he = first.He()
        self.assertEqual(he.get_hmm(), 'hmmm...')


if __name__ == '__main__':
    unittest.main()

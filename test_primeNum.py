# -*- coding: utf-8 -*-
from primeNum import primeNumber


__author__ = 'hotta.yoshinori'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pm = primeNumber(10)
        ret = pm.checkPrimeNum(8)
        self.assertEqual(ret, True)


if __name__ == '__main__':
    unittest.main()

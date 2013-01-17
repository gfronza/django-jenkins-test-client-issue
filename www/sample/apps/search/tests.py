# -*- coding: utf-8 -*-
import unittest

from apps.search.test_cases.test_views import TestSimple


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSimple))
    return suite

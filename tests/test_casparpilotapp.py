#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from casparpilot.casparpilotapp import CasparpilotApp


class TestCasparpilotApp(unittest.TestCase):
    """TestCase for CasparpilotApp.
    """
    def setUp(self):
        self.app = CasparpilotApp()

    def test_name(self):
        self.assertEqual(self.app.name, 'casparpilot')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from casparpilot.casparpilotapp import CasparPilotApp


class TestCasparPilotApp(unittest.TestCase):
    """TestCase for CasparPilotApp.
    """
    def setUp(self):
        self.app = CasparPilotApp()

    def test_name(self):
        self.assertEqual(self.app.name, 'casparpilot')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

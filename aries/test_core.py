#!/usr/bin/python

import os
import unittest

from core import Aries


class TestCreateAriesInstance(unittest.TestCase):

    # Tests
    def test_create_aries(self):

        # With
        test_object = Aries(os.path.dirname(os.path.abspath(__file__)))

        # Assert
        self.assertTrue(test_object.journal_path.endswith('aries'))
        self.assertEqual(['aries'], test_object.resources.keys())

        self.assertTrue(test_object.get_uri('aries/__index__.py').endswith('aries/__index__.py'))

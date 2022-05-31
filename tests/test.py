#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from unittest.mock import patch
import unittest

from utils import main


class TestUtils(unittest.TestCase):
    def test_utils(self):
        self.assertIsInstance(main.hello(), str)
        self.assertEqual(main.hello(), "GM World!")

    def test_config(
        self,
    ):
        print(main.use_config())

    def test_this(self):
        self.assertEqual(main.use_config(), "hello world")

    def test_that(self):
        print(main.return_all_keys())
        self.assertEqual(type(main.return_all_keys()), dict)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

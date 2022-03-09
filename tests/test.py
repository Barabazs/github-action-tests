#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from utils import main
import unittest


class TestUtils(unittest.TestCase):
    def test_utils(self):
        self.assertIsInstance(main.hello(), str)
        self.assertEqual(main.hello(), "GM World!")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

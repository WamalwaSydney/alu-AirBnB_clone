#!/usr/bin/python3
"""Unittest for console.py."""
import unittest
import subprocess


class TestConsole(unittest.TestCase):
    """Test console help/quit."""

    def test_help(self):
        p = subprocess.run(['./console.py'], input='help\nquit\n', text=True, capture_output=True)
        self.assertIn('Documented commands', p.stdout)

"""Test playful/lingo.py"""
import unittest

from playful.lingo import correct_letters, misplaced_letters


class TestLingo(unittest.TestCase):
    """Test Lingo functions"""

    def test_correct_letters(self):
        """Test identifying correct letters, given a secret word and a guess"""
        self.assertEqual(correct_letters("tacos"), ("", "", "", "", ""))
        self.assertEqual(correct_letters("tacos", "tails"), ("t", "a", "", "", "s"))
        self.assertEqual(correct_letters("misos", "mosso"), ("m", "", "s", "", ""))
        self.assertEqual(correct_letters("misos", "sassy"), ("", "", "s", "", ""))
        self.assertEqual(correct_letters("sorts", "funds"), ("", "", "", "", "s"))

    def test_misplaced_letters(self):
        """Test identifying misplaced letters, given a secret word and a guess"""
        self.assertEqual(misplaced_letters("tacos"), ("", "", "", "", ""))
        self.assertEqual(misplaced_letters("tacos", "teach"), ("", "", "a", "c", ""))
        self.assertEqual(misplaced_letters("misos", "sumps"), ("s", "", "m", "", ""))
        self.assertEqual(misplaced_letters("misos", "mosso"), ("", "o", "", "s", ""))
        self.assertEqual(misplaced_letters("misos", "sassy"), ("s", "", "", "", ""))

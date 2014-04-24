# spec_romans.py
# A test suite for romans.py

import unittest
from romans import Romans

class TestRomans(unittest.TestCase):

	def setUp(self):
		self.romans = Romans()

	def test_convert(self):
		self.assertEqual(self.romans.convert(1), 'I')
		self.assertEqual(self.romans.convert(2), 'II')
		self.assertEqual(self.romans.convert(5), 'V')
		self.assertEqual(self.romans.convert(6), 'VI')
		self.assertEqual(self.romans.convert(10), 'X')
		self.assertEqual(self.romans.convert(11), 'XI')

if __name__ == '__main__':
	unittest.main()

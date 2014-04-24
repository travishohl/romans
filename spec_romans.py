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
		self.assertEqual(self.romans.convert(4), 'IV')
		self.assertEqual(self.romans.convert(5), 'V')
		self.assertEqual(self.romans.convert(6), 'VI')
		self.assertEqual(self.romans.convert(9), 'IX')
		self.assertEqual(self.romans.convert(10), 'X')
		self.assertEqual(self.romans.convert(11), 'XI')
		self.assertEqual(self.romans.convert(15), 'XV')
		self.assertEqual(self.romans.convert(20), 'XX')
		self.assertEqual(self.romans.convert(50), 'L')
		self.assertEqual(self.romans.convert(100), 'C')
		self.assertEqual(self.romans.convert(500), 'D')
		self.assertEqual(self.romans.convert(1000), 'M')
		self.assertEqual(self.romans.convert(2014), 'MMXIV')

if __name__ == '__main__':
	unittest.main()

# spec_romans.py
# A test suite for romans.py

import unittest
from romans import Romans

class TestRomans(unittest.TestCase):

	def setUp(self):
		self.romans = Romans()

	def test_convert(self):
		self.assertEqual(self.romans.convert(1), 'I')

if __name__ == '__main__':
	unittest.main()

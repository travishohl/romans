# romans.py
# A simple program that converts decimal to roman numeral

class Romans:

	def convert(self, decimal):
		if decimal >= 5:
			return 'V'
		return 'I' * decimal

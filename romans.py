# romans.py
# A simple program that converts decimal to roman numeral

class Romans:

	def __init__(self):
		self.conversions = [
			[10, 'X' ],
			[ 9, 'IX'],
			[ 5, 'V' ],
			[ 4, 'IV'],
			[ 1, 'I' ]
		]

	def convert(self, decimal):
		answer = ""
		for conversion in self.conversions:
			while decimal >= conversion[0]:
				answer += conversion[1]
				decimal -= conversion[0]
		return answer

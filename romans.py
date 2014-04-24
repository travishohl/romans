# romans.py
# A simple program that converts decimal to roman numeral

class Romans:

	def convert(self, decimal):
		answer = ""
		if decimal >= 5:
			answer += 'V'
			decimal -= 5
		answer += ('I' * decimal)
		return answer

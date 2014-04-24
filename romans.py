# romans.py
# A simple program that converts decimal to roman numeral

class Romans:

	def convert(self, decimal):
		answer = ""
		while decimal >= 10:
			answer += 'X'
			decimal -= 10
		while decimal >= 5:
			answer += 'V'
			decimal -= 5
		answer += ('I' * decimal)
		return answer

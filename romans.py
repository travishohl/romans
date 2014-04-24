# romans.py
# A simple program that converts decimal to roman numeral

class Romans:

	def convert(self, decimal):
		answer = ""
		while decimal >= 10:
			answer += 'X'
			decimal -= 10
		while decimal >= 9:
			answer += 'IX'
			decimal -= 9
		while decimal >= 5:
			answer += 'V'
			decimal -= 5
		while decimal >= 4:
			answer += 'IV'
			decimal -= 4
		while decimal >= 1:
			answer += 'I'
			decimal -= 1
		return answer

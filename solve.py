"""
formula:
abs(lengh_1 - length_2) = shorter side
abs(x_1 - x_2) = longer side

lengths = f(x)
"""
from math import *

class func_struct:
	def __init__(self, f):
		self.f = f

	def return_val(self, val):
		x = val
		return eval(self.f)

def solve(f: func_struct, interval, MIN, MAX):
	interval_value = (MAX - MIN) / interval

	total_sum = 0
	for i in range(interval):
		x_1 = MIN + (i * interval_value)
		x_2 = MIN + ((i+1) * interval_value)
		
		length_1 = f.return_val(x_1)
		length_2 = f.return_val(x_2)

		side_1 = abs(length_1-length_2)
		side_2 = abs(x_1-x_2)

		hypotenuse = sqrt(side_1**2 + side_2**2)

		total_sum += hypotenuse
	return total_sum

def main(real_f, INTERVAL, MIN, MAX):
	r = solve(real_f, INTERVAL, MIN, MAX)
	print(r)

if __name__ == "__main__":
	_f = "sqrt(9-x**2)"
	MIN, MAX = -3, 3
	INTERVAL = 1000
	
	real_f = func_struct(_f)
	main(real_f, INTERVAL, MIN, MAX)

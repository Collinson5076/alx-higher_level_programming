#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
	print("{} is positive".format(number))
elif number == 0:
	print(f"{number} is zero")
elif number < 0:
	print(f"{number} is negative")

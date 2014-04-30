import random

import time

print "please guess and I will track down the times you got it correctly and you can press 'q' to quit at any time"

guess = 0

while True:
	chance = random.choice(['heads','tails'])
	person = raw_input("please guess heads or tails:")
	print "the coin has been flipped!"
	if person == 'q':
		print "thanks for playing"
		break
	elif person == chance:
		print "you are correct!"
		guess += 1
	elif person != chance:
		print "you are incorrect!"
		break
print "your high score was ",guess
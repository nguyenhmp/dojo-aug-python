def coin():
	import random
	x = 0 
	y = 0

	for i in range (1, 5001): 
		random_number = random.random()
 
		if round(random_number) == 1: 
			x = x + 1 
			print 'Attempt #' ,i, ': Throwing a coin... Its a head!... Got' ,x, 'head(s) so far and' ,y, 'tail(s) so far'
		elif round(random_number) ==0:
			y = y +1 
			print 'Attempt #' ,i, ': Throwing a coin... Its a tails!... Got' ,x, 'head(s) so far and' ,y, 'tail(s) so far'

coin()

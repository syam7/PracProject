heads = int(input("Give the no of heads"))
legs = int(input("Give the total no of legs"))

rabbits = (legs/2)-heads
chickens = heads - rabbits

if rabbits>0 and chickens>0 and rabbits+chickens == heads:
	print "No of rabbits are", rabbits
	print "No of chickens are", chickens
else:
	print "Not a valid data" 

string = list(raw_input().split())
string.reverse()

for i in range(0,len(string)):
	#string[i]= "".join((list(string[i])).reverse())
	temp = list(string[i])
	temp.reverse()
	string[i] = "".join(temp)
	
print " ".join(string)

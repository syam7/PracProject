string = list(raw_input().split())

output = []

for x in string :
	if x.isdigit():
		output.append(x)
		
print output


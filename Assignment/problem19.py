import collections

string = list(raw_input())

x = collections.Counter(string)

for i in range(0,len(x)):
	print x.keys()[i],x.values()[i]




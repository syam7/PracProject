_list = [12,24,35,24,88,120,155,88,120,155]

_set = list(set(_list))

for i in _list:
	if i in _set:
		print i,
		_set.remove(i)

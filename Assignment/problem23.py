
def binary_search(list,value,l,r):
	if r>=l:
		
		mid = (l+r)/2	
		if list[mid] == value:
			return mid
		elif list[mid]>value:
			return binary_search(list,value,l,mid-1)
		else:
			return binary_search(list,value,mid+1,r)
	return -1



if __name__ == "__main__":
	
	list = [1,2,3,4,8,12,15,19,23,27]
	value = 235	
	l = 0
	r = len(list) - 1
	index = binary_search(list,value,l,r)
	
	if index == -1:
		print "Value is not present"
	else:
		print "Index of the value is ", index


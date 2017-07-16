def permute(list,l,r):
	if l==r:
		print list
	else:
		for i in range(l,r):
			list[l],list[i] = list[i],list[l]
			permute(list,l+1,r)
			list[l],list[i] = list[i],list[l]
			
if __name__=="__main__":
	list = [1,2,3]
	permute(list,0,len(list))

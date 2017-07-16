
def isNumThere(s):
    return any(i.isdigit() for i in s)

def isUppCase(s):
    return any(i.isupper() for i in s)

def isLowCase(s):
    return any(i.islower() for i in s)

def specChar(s):
    list = ['$','#','@']
    return any(i in list for i in s)

def lenTest(s):
    return (len(s)>5 and len(s)<17)

if __name__ =="__main__":
	
	list_inp = raw_input().split(',')
	output = []
	
	for s in list_inp:
		if(isNumThere(s) and isUppCase(s) and isLowCase(s) and specChar(s)and lenTest(s)):
			output.append(s)
			
	for x in output:
		print x

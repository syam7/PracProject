class badPassword(Exception):
   pass

if __name__=="__main__":

	passLength = 10
	
	while True:
		try:
			input_ = raw_input("Give the password")
			if len(input_)<passLength:
				raise badPassword
			break
			
		except badPassword:
			print("Password is too small")
	
	print 'Succesfully Terminated'

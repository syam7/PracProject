class Account:
	
	def __init__(self,accountName):
		self.accountName = accountName
		self.balance = 0

	def deposit(self, value):
		self.balance += value

	def withdrawal(self, value):
		if value>self.balance:
			raise RuntimeError("Insufficient Funds")
		
		self.balance -= value

if __name__ == "__main__":
	syamAccount = Account("shyam")
	
	inp = raw_input().split()
	list = ['D','W']	
	
	while inp[0] in list:
				
		if inp[0] == 'W':
			syamAccount.withdrawal(int(inp[1]))
		elif inp[0] == 'D':
			syamAccount.deposit(int(inp[1]))
		
		inp = raw_input()
		if inp:
			inp = inp.split()
		else:
			break

	print(syamAccount.balance)
	



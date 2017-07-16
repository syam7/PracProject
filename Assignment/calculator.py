class Calculator:
	def __init__(self,x,y):
		self.a = x
		self.b = y
		
	def addition(self):
		return self.a+self.b	
		
	def subtraction(self):
		return self.a-self.b
		
	def multiplication(self):
		return self.a*self.b
		
	def division(self):
		return self.a/self.b


if __name__ == "__main__":

	print "Addition:0","Subtraction:1","Multiplication:2","Division:3"

	oper = raw_input("Give the operation number")
	a,b = map(float,raw_input("Give the two numbers: ").split())
	c = Calculator(a,b)

	if(oper=='0'):
	    print "Addition of two numbers is",c.addition()
	elif(oper=='1'):
	    print "Subtraction of two numbers is",c.subtraction()
	elif(oper=='2'):
	    print "Multiplication of two numbers is",c.multiplication()
	elif(oper=='3'):
	    print "Division of two numbers is",c.division()
	

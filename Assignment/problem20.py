class Person:
	def __init__(self,first,last):
		self.firs_name = first
		self.last_name = last
		
		
class Male(Person):
	gender = 'M'
	
	def __init__(self,first,last):
		Person.__init__(self,first,last)
		
	def getGender(self):
		return self.gender
		

class Female(Person):
	gender = 'F'
	
	def __init__(self,first,last):
		Person.__init__(self,first,last)
		
	def getGender(self):
		return self.gender
		
		
if __name__ == "__main__":
	
		m = Male('shyam','kumar')
		f = Female('sri','harini')
		
		print m.getGender()
		print f.getGender()	


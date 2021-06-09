nameall= 'weRichard Smith'
first, last =nameall.split(' ' )
'''print(first)
print(last)
#first=first[3:]#################################################################
print(first)
print(first[0].isupper())

def cap_short(first):
	for i in range(0,len(first)):
		while  not first[i].isupper():
			i+=1

		if first[i].isupper():
			first= first[i:]
			break

	print(first)
cap_short('dfwRobert Lewandowski')


'''


def first_cap(first):
	for i in range(0,len(first)):
		if  not first[i].isupper():
			i+=1
		else:
			first= first[i:]
			break
	#print(first)
	return first
	
	
def mfirst_cap(first):
	for i in range(0,len(first)):
		if  not first[i].isupper():
			i+=1
		else:
			
			first= first[i:]
			break
	#print(first)
	return first
	
	
	

print(mfirst_cap('swjmegsdjcefewkgkrthT'))
#**********************************************************
class Worker:
	def __init__(self,vname,sname,job):
		self.vname=vname
		self.sname =sname
		self.job=job





class Undercover(Worker):
	def __init__(self,vname,sname,job,projekt,deckname):
		super().__init__(vname,sname,job)
		self.projekt =projekt
		self.deckname=deckname






class Manager(Worker):
	def __init__(self,vname,sname,job,emps = None ):

		super().__init__(vname,sname,job)
		if emps is None:
			self.emps=[]
		else:
			self.emps =emps
	def print_emps(self):
		""" p
		Prints subordinate's surname and if worker type is Undercover then
		also prints worker's deckname
		"""
		for emp in self.emps:
			print('-->',emp.sname)
			if isinstance( emp,Undercover):  #***if worker class is Undercover then print deckname****
				print(f'{emp.deckname} is involved in {emp.projekt}')

e1=Worker('Don','Johnson','Detective')
candy =Undercover('Candy','Dulfer','Spionin','Operation Fledermaus',
	'Sax')
		
capo =Manager('Jimmy','James','Police Captain',[e1,candy])
print(capo.sname,capo.job)
print(e1.job)
capo.print_emps()



#*******************************************

print(isinstance(candy,Undercover))
#



def myfunc():
	""" docstring fo myfunc"""
	print('myfunc')

myfunc()
print(myfunc.__doc__)

print(Manager.print_emps.__doc__) ####Object method therefore object name required###########





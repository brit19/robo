#This is a comment for git 1 added
import itertools as it
'''data1=erto[[123,50],[123,56,77], [633,45,2346],[9,70]]
d1=[[1000,2000],[3,3,5,67,44,2,12]]
dataflat= it.chain(*data1)
d1flat=it.chain(*d1)
fl=list(it.chain(dataflat, d1flat))

#+++++++++++++try
'''
b=[[1,2,3],[4,5,6,7],[8,9,10]]
c=[[20,21],[9001,87,"where does this come?"],[23,24,25,26,50,'not here']]
d=[[4,55,6],[56,int('68'),99]]
tryl =list(it.chain(*b,*c,*d)) #flatten all items of all lists to one list
print (len(tryl))
#+list type of each entry in tryl
for i in tryl:
	#print(type(i))
	if  isinstance(i,str):	
			ca=i.upper()
			eo =tryl.index(i)
			#print(eo)
			print(f' list item {eo} --> {ca} is not an integer')


trylint=[x for x in tryl if isinstance(x,int)]

print(trylint)
'''

#create	 new list with only integers from tryl


print(tryl)
tryl.sort()
print (tryl)
# trylsort=sorted(tryl)
# print(trylsort)
# print(sum(tryl))
# print(tryl[-2:3:-3])

# step=-7
# print(tryl[-5::step])


lst2 =[x for x in lst if isinstance(x,int)]
print(lst2)
'''

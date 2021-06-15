import random
'''b=random.randint(1,15)
a=random.sample(range (56,179),12)
print(f'LENGTH OF A IS: {len(a)}  ')

c=sorted(a)
print(c)
# if  (n:= len(a)>10):
print(f' len of sorted a {sorted(a)} is greater than 10 shortened to {sorted(a)[0:10]}')
# 	print(f'' len of a {a} is less than 10')
print(c[0:10])
print(sorted(a))
print(sorted(a)[0:10 ])
print(a[0:10])
#print('f len of a {a} is greater than 1
print(f' {a}, {c}, { sorted(a)[0:10]} {a[0:10]} { sorted(a)[0:10]}')
'''
#********************************************************************************************************
# import smtplib, ssl

# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "rob.arfaleg@gmail.com"
# receiver_email = "robert.green@web.de.com"
# password = input("Type your password and press enter:")
# message = """\
# Subject: Hi there

# This message is sent from Python."""

# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
'''
qw=[1,2,3,4]
qw.pop(1)
print(qw)

print(qw)
del qw[1:3]
print(qw)
#qw#.append((*range(45,90)))
# print(qw)
# import itertools

# a=[1,2,3]
# b=[3,4,5]
# c=itertools.chain(a,b)
# print(list(c))

# asd=itertools.chain(qw)
# print(list(asd))
# #print(qw)
# #b=[list(itertools.chain(*qw))]
# #print(ab)
# '''
# #*************************************
# # #Combinations
# import math
anz=[2,3,4,5]
com=['doubles','trebles','fours','fives']
# # for b in (com):
# # 	for a in range(2):
	
# # 	 print(b ,math.comb(5,a))
# #print(com[1])

# for a in range(len(com)):

# 	for b in range(2,len(com)):
# 		x=math.comb(4,b)
# 		print (com[a],b)


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)
# print(a)

# anz=[1,2,3]
# com=['red','green','blue']

# for x in anz:
# 	for y in com:
# 		print(x,y[x])
#***************************************************************************+
a=[2,3,4,5]
b=['double','treble','fours','fives']

for x, y in zip(a, b):
    print (x, y)
    print('\n')
#***************************************************************************
import itertools
ab= [1,2,3,4,5,6]
bc=(list(range(11,18)))
for x,y in itertools.zip_longest(ab[:3],bc[:4],fillvalue='There is no entry'):
	print(x,y)

#hamming_distance
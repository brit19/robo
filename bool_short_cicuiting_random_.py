



print([] and 3)

def p(arg):
    print(f"Inside p with arg={arg}")
    return arg

print(p(False) or p(3))
print(5 or 6)
import pathlib

import os
print( pathlib.Path.cwd())
from iteration_utilities import deepflatten
import random
ran=random.sample(range(2,100),25)
#print(sorted(ran))

ranlst=[[56,[*sorted(random.sample(range(2,100),25))],[5,5,5]]]
ranlstflat=deepflatten(ranlst)
#print(len(list(ranlstflat)))
ranlstsort=(sorted(list(ranlstflat)))
print(ranlstsort)
print(len(ranlstsort))

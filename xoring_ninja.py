import time 
start_time = time.time()

from itertools import *
power_set = [1,2,3]
len_p = 2**len(power_set)
def findsubsets(S,m):
	return set(iterators.combinations(S,m))
print findsubsets(power_set,len_p)

dead = time.time() - start_time
import math
n = int(raw_input())
lista = [int(raw_input()) for _ in range(n)]
for i in lista:
	sq_sum = (i*(i+1)*(2*i+1))/6
	whole_sqsum = (i*(i+1))/2
	whole_sqsum = whole_sqsum**2
	print abs(sq_sum - whole_sqsum)
	'''
	j=1
	sq_sum = 0
	whole_sqsum = 0
	using formula above
	while j<=i:
		sq_sum += j**2
		whole_sqsum += j
		j+=1
	#print sq_sum, whole_sqsum**2
	print abs(sq_sum - whole_sqsum**2)'''


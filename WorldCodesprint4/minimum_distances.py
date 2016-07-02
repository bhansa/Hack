#!/bin/python
import math
n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
lis = dict()
dup = list()
yes = 0
for i in range(len(A)):
	if A[i] in lis.keys():
		lis[A[i]] = abs(lis[A[i]] - i)
		dup.append(lis[A[i]])
		yes = 1
	else:
		lis[A[i]] = i
if yes == 1:
	print min(dup)
else:
	print -1


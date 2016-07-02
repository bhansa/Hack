import math
n= int(raw_input())
lis = [int(raw_input()) for i in range(n)]
#import time 
#start = time.time()
#n=1
#lis=[1000000000]
'''
Using O(n^1/2)
'''
for i in lis:
	flag = 0
	if i==1:
		print "Prime"
		break
	for j in range(2,int(math.sqrt(i))):
		if i%j == 0:
			flag = 1
			break
	if(flag == 1):
		print "Not prime"
	else:
		print "Prime"
print "Time: ",time.time() - start
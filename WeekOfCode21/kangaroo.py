x1,v1,x2,v2=map(int,raw_input().split())
if x1==x2:
	print "YES"
	exit()
if x1!=x2 and v1==v2:
	print "NO"
	exit()
if x1<x2 and v1<v2 or x1>x2 and v1>v2:
	print "NO"
	exit()
else:
	#SIMPLY PRINT YES
	print "YES"
	'''
	#FOR Education purpose
	t1=x1
	t2=x2
	while(t1!=t2):
		#print t1,
		t1 = t1 + v1
		#print t2
		t2 = t2 +v2
	print "YES"'''
print t1,t2
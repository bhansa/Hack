import time
start = time.time()
#n=int(raw_input())
#_input_var = [int(raw_input()) for i in range(0,n)]
n = 2
_input_var = [100000000,20]
def reverse(num):
	return int(str(num)[::-1])
def isDigitOdd(num):
	for i in str(num):
		if int(i)%2==0:
			flag = False
			return flag
		else:
			flag = True
	return flag
def main(_iter):
	bhansa = set()
	#count=0
	i=1
	while(i<_iter):
		if i%10==0:
			i+=1
			continue
		if i in bhansa:
			i+=1
			#count+=1
			#print i,"OWW"
			continue
		rev = reverse(i)
		k = i + rev
		#print "i: ",i*2,"k(number generated) : ",k
		if isDigitOdd(k):
			#another method is to use dictionary, i'm using list for now
			#print "number accept: ",k
			#count+=1
			bhansa.add(i)
			bhansa.add(rev)

		i+=1
	#print count
	#print bhansa
	print len(bhansa)
for i in _input_var:
	main(i)
print "Time: ",time.time() - start
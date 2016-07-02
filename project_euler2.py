n = int(raw_input())
lista = [int(raw_input()) for _ in range(n)]
#print lista
def fibbo(n):
	fib=[0,1]
	i=2
	sum=0
	next=0
	while len(fib)<n :
		next = fib[i-2]+fib[i-1]
		if next>n:
			break
		fib.append(next)
		i+=1
	#print fib
	for i in fib:
		if i%2==0:
			sum+=i
	print sum

def main(_iter):
	fibbo(_iter)
for i in lista:
	main(i)


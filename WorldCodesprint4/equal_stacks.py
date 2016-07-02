n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))
'''
n1,n2,n3 = 5,3,4
h1 = [3,2,1,1,1]
h2 = [4,3,2]
h3 = [1,1,4,1]
'''
s1,s2,s3 = sum(h1),sum(h2),sum(h3)
if s1==s2==s3:
	print s1
	exit()
while not s1 == s2==s3:
	if s1<s2:
		d = s2-s1
		if d == h2[0]:
			h2.pop()
			if d == h3[0]:
				h3.pop()
			else:
				h3.pop(0)
		else:
			h2.pop(0)
			
	else:
		if s1 == s2:
			h3.pop(0)
		else:
			h1.pop(0)
			continue



print s1
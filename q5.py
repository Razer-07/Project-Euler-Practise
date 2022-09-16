def f(n):
	#l=[x for x in range(11,20)]
	l=[11,13,17,19]
	m=0
	for i in range(len(l)):
		if(n%l[i] ==0):
			m=m+1
		else :
			m=m+0

	if(m>=len(l)):
		return(n)
	else:
		return 0		

n=831402
n=float(n)
while(True):
	if((f(n)==n)==True):
		print(n)
		break
	else:
		n=n+1	
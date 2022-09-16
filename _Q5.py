def f(n):
	#l=[x for x in range(11,20)]
	l=[11,13,17,19]
	m=0
	k=0
	for i in range(len(l)):
		k=n%l[i] 
		if(k==0):
			m=m+1
		else :
			break

	if(m>=len(l)):
		return(n)
	else:
		return (k)		

n=831
n=float(n)
while(True):
	if((f(n)==n)==True):
		print(n)
		break
	else:
		n=n+1	

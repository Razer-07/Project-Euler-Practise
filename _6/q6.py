def sq_sum(n):
	return(int((n*(n+1)*((2*n)+1))/6))

#print(sq_sum(10))	

def sum_sq(m):
	return(int(m*(m+1)/2)**2)

print(sum_sq(100)- sq_sum(100))	

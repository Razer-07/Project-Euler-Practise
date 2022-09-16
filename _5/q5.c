#include<stdio.h>

long func(long n){
	int l[]={11,13,17,19};
	int m=0;
	for(int i;i<=sizeof(l);i++){
		if(n%l[i]==0){
			m=m+1;
		}
		else{
			m=m+0;
		}
	}
	if(m>= sizeof(l)){
		return n;
	}
	else{
		return 0;
	}
}

int main(){
	n=831402;

	while(true){
		if((f(n)==n)==true){
			printf(n);
			break;
		}
		else{
			n=n+1;
		}
	}
}
		
			
		

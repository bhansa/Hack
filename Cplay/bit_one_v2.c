//updated copy
#include <stdio.h>
#include<stdint.h>
uint64_t pow(uint64_t n,uint64_t d);
int main(){

	uint64_t a,x,n;
	printf("Number:");
	scanf("%llu",&a);
	printf("power:");
	scanf("%llu",&n);
	x = pow(n,a);
	printf("%llu\n",x);
}
uint64_t pow(uint64_t n,uint64_t d){
	if(n+1==1)
		return 1;
	return d*pow(n-1,d);
}

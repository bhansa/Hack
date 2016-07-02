//@author bhansa
//Project Euler #145
#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include<time.h>
#define size(type) sizeof(type-1)/sizeof(type[0])
#define INT_MAX 999999999
#define INT_MIN -99999999
uint64_t reverse(uint64_t rev);
uint64_t checkAllOdd(uint64_t oddy);
int main(){
	clock_t begin, end;
	uint64_t time_spent;
	begin = clock();
	//starting all jobs
	uint64_t i,j,k,nib,rev;
	uint64_t a[sizeof(uint64_t)];
	int dictionary[sizeof(uint64_t)];
	int count,n;
	//int n=5,count;
	//int a[] = {10000000,9840,14545,121212,45};
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%llu",&a[i]);
	}
	for(i=0;i<n;i++){
		count = 0;
		for(j=1;j<a[i];j++){
			rev = reverse(j);
			nib = j+rev;
			if(checkAllOdd(nib) && j%10!=0){
				count++;
				//printf("num: %llu  geb: %llu\n",j,nib);
			}
		}
		printf("%llu\n",count);
	}


	//finishing up
	end = clock();
	time_spent = (uint64_t)(end - begin) / CLOCKS_PER_SEC;
	printf("Execution Time : %d\n",time_spent);

}
uint64_t reverse(uint64_t rev){

	uint64_t revnum = 0;
	while(rev!=0){
		revnum = revnum*10 + (rev%10);
		rev/=10;
	}
	return revnum;
}
uint64_t checkAllOdd(uint64_t oddy){

	uint64_t oddynum = 0;
	while(oddy!=0){
		if((oddy%10)%2==0)
			return 0;
		oddynum = oddynum*10 + (oddy%10);
		oddy/=10;
	}
	return 1;

}
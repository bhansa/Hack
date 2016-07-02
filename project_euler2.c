//@author bhansa
//project_euler002
#include<stdio.h>
#include<stdint.h>
#define INT_MAX 99999
uint64_t getevenfibbo(uint64_t n);
int main(int argc, char const *argv[])
{
	uint64_t n;
	int a[INT_MAX],i=0;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
		printf("%llu\n",getevenfibbo(a[i]));
	}

	return 0;
}
uint64_t getevenfibbo(uint64_t n){

	int j,ksum=0;
	uint64_t b[INT_MAX],next=0;
	b[0]=0;b[1]=1;
	for(j=2;j<j<n;j++){
		next = b[j-2] +b[j-1];
		b[j] = next;
		if(b[j]>n)
			break;
		if(next%2==0){
			ksum+=next;
		}
		//printf("%d\n",b[j]);
	}
	return ksum;

}
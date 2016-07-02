#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main()
{
	int i,n;
	unsigned int flipper;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{ 
		scanf("%u",&flipper);
		printf("%u\n",~flipper);
	}
	return 0;
}
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int xor_ninja(int a_size,int *a){

	//finding subsets
	unsigned int pow_set_size = pow(2, a_size);
    int counter, j;
 
   	for(counter = 0; counter < pow_set_size; counter++)
    {
      for(j = 0; j < a_size; j++)
       {
       	if(counter & (1<<j))
            printf("%d", a[j]);
       }
       printf("\n");
    }

}

int main() {

    int a_size,item,test,test_item;
    int a[a_size];
    scanf("%d",&test);
    for(test_item=0;test_item<test;test_item++){
    	scanf("%d",&a_size);
    	for(item=0;item<a_size;item++){
    		scanf("%d",&a[item]);
    	}
    }
    xor_ninja(a_size,a);
    return 0;
}

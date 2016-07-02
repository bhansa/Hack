#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
int maxXor(int l, int r) {

	int i,j,max=-999,xor;
	for(i=l;i<=r;i++){
		//printf("i :%d\n",i);
		for(j=i;j<=r;j++){
			xor = i^j;
			//printf("%d\n",xor);
			if(xor>max){
				max = xor;
			}
		}
	}
	return max;

}
int main() {
    int res;
    int _l;
    scanf("%d", &_l);
    
    int _r;
    scanf("%d", &_r);
    res = maxXor(_l, _r);
    printf("%d", res);
    
    return 0;
}

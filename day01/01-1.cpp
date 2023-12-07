#include <stdio.h>
char line[3000];
int main()
{
	int ans = 0;
	while(scanf("%s",line)==1){
		int first=-1, last=-1;
		for(int i=0; line[i]!=0; i++){
			char c = line[i];
			if(c>='0' && c<='9'){
				if(first==-1) first = c-'0';
				last = c-'0';
			}
		}
		ans += first*10+last;
		//printf("%d %d %d\n", first, last, first*10+last);
	}
	printf("%d", ans);
}

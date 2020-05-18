#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> //Header file for sleep(). man 3 sleep for details. 
#include <pthread.h> 
#include <time.h>
int h=0,m=0,s=0;
 
void *clocksecond(void *vargp) 
{  
	if(s==59){
		s=0;
	}
	else{
		s+=1;	
	}
	return NULL; 
} 
void *clockminute(void *vargp) 
{ 
	if(s==0){
		if(m==59){
			m=0;
		}
		else{
			m+=1;
		}
	}
	return NULL; 
}
void *clockhour(void *vargp) 
{ 
	if(m==0&&s==0){	 
		if(h==23){
			h=0;
		}
		else{
			h+=1;
		}
	}
	return NULL; 
}

int main() 
{ 
	while(1){
        	pthread_t thread_id; 
		pthread_create(&thread_id, NULL, clocksecond, NULL);
		pthread_create(&thread_id, NULL, clockminute, NULL);
		pthread_create(&thread_id, NULL, clockhour, NULL);  
		sleep(1);
		system("clear");
        	printf("\n%d:%d:%d",h,m,s);
	}
	exit(0); 
}


#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>
pthread_mutex_t lock;
int hrs = 0,min = 0,sec = 0;
pthread_t t1,t2,t3;
void* calsec(){
	while(1){
		printf("%d:%d:%d\n",hrs,min,sec);
		sleep(1);
		fflush(stdout);
		pthread_mutex_lock(&lock);
		sec++;
		pthread_mutex_unlock(&lock);
	}
}

void * calmin(){
	
	while(1){
		if(sec == 10){
			sec = 0;
			pthread_mutex_lock(&lock);
			min++;
			pthread_mutex_unlock(&lock);
		}
	}
	
}
void * calhrs(){
	
	while(1){
		if(min == 2){
			min = 0;
			pthread_mutex_lock(&lock);
			hrs++;
			pthread_mutex_unlock(&lock);
		}
	}
	
}
int main(){
	pthread_mutex_init(&lock, NULL);
	
	pthread_create(&t1, NULL, calsec,NULL);
	pthread_create(&t2, NULL, calmin,NULL);
	pthread_create(&t3, NULL, calhrs,NULL);
	pthread_join(t1,NULL);
	pthread_join(t2,NULL);
	pthread_join(t3,NULL);
	pthread_mutex_destroy(&lock);
	return 0;
}
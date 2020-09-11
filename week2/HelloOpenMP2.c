/*
 ============================================================================
 Name        : HelloOpenMP.c
 Author      : 
 Version     :
 Description : Hello OpenMP World in C
 ============================================================================
 */
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[]) {


  int numThreads, tid, idx;
  int limit = 10;
  int sum = 0;


  /* This creates a team of threads; each thread has own copy of variables  */
#pragma omp parallel private(numThreads, tid, sum) num_threads(30)
 {
   tid = omp_get_thread_num();

   #pragma omp parallel for
   for ( idx = 0; idx < limit; idx++)
   {
	   printf("Hello World from thread number %d and idx = %d\n", tid, idx);
	   sum = sum + idx;
   }

   printf( " Sum for thread %d is %d\n", tid, sum);

   /* The following is executed by the master thread only (tid=0) */
   if (tid == 0)
     {
       numThreads = omp_get_num_threads();
       printf("Number of threads is %d\n", numThreads);
     }
 }
 return 0;
}



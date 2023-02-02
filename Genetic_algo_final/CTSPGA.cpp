/*Truth Is Beauty*/
/*  crisp(simple)TSP with 10 node solve by GA With RW selection,Cyclic Cross Over without any constraint*/
/*  noc=85,maxgen=500,pc=0.4,pm=0.3,seed=9,the optimum result found at the generation=470,optimal cost=99.00,pat:5-3-2-6-7-1-9-4-8-0*/
#include<stdio.h>
#include<math.h>             
#include<stdlib.h>
#include<conio.h>
#define node 10
#define noc 5 //noc= no of chromosome//
#define maxgen 5
#define pc 0.4
#define pm 0.3 

//_____________________________________________part_1_______________________________________________

/*float COST[node][node][3]={{{1000,1100,1200},{15,16,17},{30,32,35},{4,4.5,5}},
												{{6,7,8},{1000,1100,1200},{4,4.5,5},{1,1.24,1.5}},
												 {{10,12,13},{15,17,18},{1000,1100,1200},{16,17,18}},
												{{7,8,9},{18,20,22},{13,14,15},{1000,1100,1200}}};*/

/*float COST[node][node]={{1000,2,5,7,1},{6,1000,3,8,2},{8,7,1000,4,7},{12,4,6,1000,5},{1,3,2,8,1000}};*/
/*float COST[node][node]={{1000,12,15,10,8},{8,1000,15,12,8},{9,11,1000,15,11},{7,12,19,1000,11},{9,12,16,10,1000}}; */
float COST[node][node]={{1000,25,28,32,20,6,35,37,40,30},{37,1000,20,28,35,40,30,42,28,4},{42,28,1000,30,25,35,9,32,40,30},{28,30,7,1000,20,25,30,35,22,37},{37,22,35,30,1000,20,25,30,9,28},{25,30,25,8,28,1000,32,40,32,30},{28,25,30,22,37,40,1000,10,32,20},{20,5,32,40,35,25,40,1000,22,37},{30,40,35,25,20,22,37,32,1000,28},{28,30,28,20,11,32,37,40,30,1000}};
float cumuprob[50],prob[50];

int nparr[100];  /* new population array*/

	double TOU[10][10],total;
	 struct chrom
	 {
	  int pt[node];
	  float fitness;
	  }ch[noc];
	struct chrom popu[100];
	struct chrom npopu[100];
	struct chrom fpopu[100];

	void calfitness(int pv);
   void selection(int pv);
	void crossover( int pv);
	void cross(int p0,int p1,int pv);
	void mutation(int pv);
	void mutate(int p,int pv); 

//_____________________________________________part_2_______________________________________________
 float check(int pv);
	int main()
	 {
			int seed,i,j,t2,path[20],j1,flag;
			int z,r,p,z1[node];
		  int count,x,y,pv=0;
			 float y1,y2[2];
		//	clrscr();
			printf("\n Please enter seed:");
			scanf("%d",&seed);

			srand(seed);
			 for(i=0;i<node;i++)
			 for(j=0;j<node;j++)
				 TOU[i][j]=1/COST[i][j];
				for(i=0;i<noc;i++)
					 {
						 t2=0;
						 path[t2]=1;
						 t2++;
						//	 printf("\nt2=%d,i=%d",t2,i);
							v: r=rand()%node;
						  //printf("r=%d",r);
							 flag=1;
							 for(j1=0;j1<t2;j1++)
								 if(r==path[j1])
								 flag=0;

							if(flag==1)
							 {
							  path[t2]=r;
							  t2++;
							  }
							 // printf("tt2=%d",t2);
						  if(t2==node)
						  goto k;
						  goto v;

						 k:
							//printf("Path=%d ",i);
							for(z=0;z<t2;z++)
						  //	printf("%d\t",path[z]);
						  //	printf("\n");
						/* cheak that it is repeated path or not*/
						 for(z=0;z<node;z++)
					  ch[i].pt[z]=path[z];
						 for(x=0;x<i;x++)
							{
							 count=0;
							 for(y=0;y<node;y++)
							 {
								if(path[y]==ch[x].pt[y])
								count++;
							 }

							if(count==node)
							 goto skip;
						 }


					 /* for(z=0;z<node;z++)
					  ch[i].pt[z]=path[z]; */

					  for(z=0;z<node;z++)
					  popu[pv].pt[z]=path[z];

					  pv++;
					  skip :;
					 }

				 /* for(i=0;i<noc;i++)
					 {
						for(j=0;j<node;j++)
						printf("11 %d ",ch[i].pt[j]);
						printf("\n");
					 }
						*/
				  printf("size of popu:%d",pv);
				  printf("\n");

//_______________________________________________part_3_________________________________________________
				//	for(i=0;i<pv;i++)  /* here pv is the  no of chromosome*/
					// {
					 //	for(j=0;j<node;j++)
					 //	printf(" %d ",popu[i].pt[j]);
					  //	printf("\n");
					// }
					// fpopu[0]=10000;
				  /* APPLY GENETIC LGORITHM */
					y2[0]=10000;
				  for(i=1;i<=maxgen;i++)
				  {
				  //printf("\nGeneration=%d\n",i);
					 calfitness(pv);
					 selection(pv);
					 crossover(pv);
					 mutation(pv);
					 y1=check(pv);
					// y2[0]=y1;
					 if(y2[0]>y1)
					 {
					 y2[0]=y1;
					 p=i;
					 for(j=0;j<node;j++)
					 {
					  z1[j]=fpopu[0].pt[j];
					 }
					 //printf("\nff final fitness y2[%d]= %f\n",p,y2[0]);
					  }
					 
					}
					printf("\nOptimum Result Found At TheGeneration=%d\n",p);
					printf("Optimum Value=%f\n",y2[0]);
				   printf("\nFinal path\n");
					for(j=0;j<node;j++)
					printf("%d\t",z1[j]);
				 getch();
				}

//_______________________________________________part_4_________________________________________________

	void calfitness(int pv)
	{
		 int i,j;
		 float sum;

		for( i=0;i<pv;i++)
		  {
			  sum=0;
			 for(j=0;j<node-1;j++)
				  sum=sum+COST[popu[i].pt[j]][popu[i].pt[j+1]];
				  sum=sum+COST[popu[i].pt[node-1]][popu[i].pt[0]];
			 popu[i].fitness=sum;
		  //	 fpopu[i].fitness=sum;
			 }

		 for( i=0;i<pv;i++)
		  {
			 fpopu[i].fitness=1000;
			 //for(j=0;j<node;j++)
			 //printf("%d\t",popu[i].pt[j]);
			 //printf("fittness=%f\n",popu[i].fitness);
		  }

		 }
	void selection(int pv)
	{

	  float s=0,r;
	  int i,k,count,p,j;

	  for( i=0;i<pv;i++)
				 s+=popu[i].fitness;

	  for( i=0;i<pv;i++)
			prob[i]=popu[i].fitness/s;

		 s=0;
		for(i=0;i<pv;i++)
		  {
			s=s+prob[i];
		  cumuprob[i]=s;
		 }
		 for(i=0;i<pv;i++)
		 // printf("cump=%f\t ",cumuprob[i]);

		count=0;

			for(i=0;i<pv;i++)
		{
			r=(rand()%1000)/1000.	;
		  //	printf("%f",r);
			 for(k=0;k<pv;k++)
			 {
				if(r<cumuprob[k])
			  {
				 nparr[count]=k;
			  //	printf("%d",k);
				 count++;
				 goto u;
				}
			}
		  u:;
		}
		  /*printf("pos:");
		 for(i=0;i<pv;i++)
		 printf("%d\t",nparr[i]);   */

		 for(i=0;i<pv;i++)
			{
				 p=nparr[i];
				for(j=0;j<node;j++)
				 npopu[i].pt[j]=popu[p].pt[j];
			 }
			  //display //
			 // printf("\nSelective population\n");
			 // for(i=0;i<pv;i++)
			 // {
			  //	 printf("pos=%d  ",nparr[i]);
			  //	for(j=0;j<node;j++)

			  //	printf("%d\t",npopu[i].pt[j]);
			  //	printf("\n");

			// }
		  }
//_______________________________________________part_5_________________________________________________
	  void crossover( int pv)
			{
				 int i,pos[2],count=0;
					float r;
				 for(i=0;i<pv;i++)
				 {
					 r=(rand()%1000)/1000.;
				  //	 printf("r=%f",r);
					  if(r<=pc)
					 {
						pos[count]=i;
						count++;
					 //	printf("count=%d",count);
						if(count==2)
						  {
						 // printf("\npos[0]=%d,pos[1]=%d\n",pos[0],pos[1]);
								cross(pos[0],pos[1],pv);
								count=0;
						  }
					 }
			  }
			 //display //
			 // printf("\nafter cross over\n");
			 // for(i=0;i<pv;i++)
			 // {
			  //	for(int j=0;j<node;j++)
			  //	printf("%d\t",npopu[i].pt[j]);
			 //	printf("\n");
			// }

//return (1);
		  }

		  void cross(int p0,int p1,int pv)
		  {
				int i,j,pos,k,temp;
				int pr1[node],ch1[node],pr2[node],ch2[node];

			//copy 1st chromosome into pr1[]
			for(i=0;i<pv;i++)
			{
				 if(p0==i)
				 {
				  for(j=0;j<node;j++)
				  pr1[j]=npopu[i].pt[j];
				  }

			 }

			 //copy 2nd  chromosome into pr2[]
				for(i=0;i<pv;i++)
			{
				 if(p1==i)
				 {
				  for(j=0;j<node;j++)
				  pr2[j]=npopu[i].pt[j];

				  }

			 }
			/* for(i=0;i<node;i++)
			 {
			  printf("%d ",pr1[i]);
			  }
			  printf("\n");
				 for(i=0;i<node;i++)
				 {
				printf("%d ",pr2[i]);
				}   */

			//  cross general method//
			pos=rand()%node ;

		 //	printf("cross pos=%d\n",pos);
			for(i=0;i<node;i++)
			{
			ch1[i]=10000;
			ch2[i]=10000;
			}
			/* cyclic crossover for child1*/
			for(i=0;i<node;i++)
			{
			  if(pr1[i]==pos)
				 {
					k=i;
			  l1:	temp=pr1[k];
					if(ch1[k]==temp)
					{
					 goto l2;
					}
					else
					{
					  ch1[k]=temp;
					  for(j=0;j<node;j++)
					  {
						if(pr2[j]==temp)
						{
						k=j;
						temp=pr1[k];
						goto l1;
						}
					  }
					}
				 }
			}
			l2: for(j=0;j<node;j++)
			{
			 if(ch1[j]!=pr1[j])
			 {
			 ch1[j]=pr2[j];
			 }
			}
			/* Cyclic crossover for child2*/

			 for(i=0;i<node;i++)
			{
			  if(pr2[i]==pos)
				 {
					k=i;
			  l12:	temp=pr2[k];
					if(ch2[k]==temp)
					{
					 goto l21;
					}
					else
					{
					  ch2[k]=temp;
					  for(j=0;j<node;j++)
					  {
						if(pr1[j]==temp)
						{
						k=j;
						temp=pr2[k];
						goto l12;
						}
					  }
					}
				 }
			}
			l21: for(j=0;j<node;j++)
			{
			 if(ch2[j]!=pr2[j])
			 {
			 ch2[j]=pr1[j];
			 }
			}
	  /*	  printf("\nAfter crossover\n");

			for(i=0;i<node;i++)
			printf("%d\t",ch1[i]);
			printf("\n");
			for(i=0;i<node;i++)
			printf("%d\t",ch2[i]);   */

		  /*	for(i=0;i<=pos;i++)
				 ch1[i]=pr1[i];
			 for(i=(pos+1);i<node;i++)
				 ch1[i]=pr2[i];

				for(i=0;i<=pos;i++)
				 ch2[i]=pr2[i];
			 for(i=(pos+1);i<node;i++)
				 ch2[i]=pr1[i];
									  */
			// again copy 1st child chromosome to the population//
				for(i=0;i<pv;i++)
			{
				 if(p0==i)
				 {
					for(j=0;j<node;j++)
					npopu[i].pt[j]=ch1[j];
				  }
			 }

		  // again copy 2nd child chromosome to the population//
			for(i=0;i<pv;i++)
			{
				 if(p1==i)
				 {
				  for(j=0;j<node;j++)
				  npopu[i].pt[j]=ch2[j];
				  }
			 }

	  }
//_______________________________________________part_6_________________________________________________
	void mutation(int pv)
	  {
			int i,p,j,i1;
			float r;
			for(i=0;i<pv;i++)
				 {
					 r=(rand()%1000)/1000.;
					  if(r<=pm)
					 {
						p=i;
						mutate(p,pv);
					 }
			  }
			// copy new chromosome to the new population//
		  //	printf("\nAfter Mutation\n");

			 for(i1=0;i1<pv;i1++)
					 {
						for(j=0;j<node;j++)
						{
						popu[i1].pt[j]=npopu[i1].pt[j];
						fpopu[i1].pt[j]=npopu[i1].pt[j];
					// printf("%d\t",fpopu[i1].pt[j]);
						}
					  //	printf("fittness=%f\n",popu[i1].fitness);
					  //	printf("\n");
					 }
					 calfitness(pv);
				}

	 void mutate(int p,int pv)

	 {

				int i,j,a,b,c;
				int pr1[node];


			for(i=0;i<pv;i++)   //copy that chromosome into pr1[]//
			{
				 if(p==i)
				 {
				  for(j=0;j<node;j++)
				  pr1[j]=npopu[i].pt[j];
				  }
			 }
			 // mutate//
			 a=rand()%(node-1);
			 b=rand()%(node-1);
			 if(a!=b)
			 {
			  c=pr1[a];
			  pr1[a]=pr1[b];
			  pr1[b]=c;
			 }

			 // again copy this chromosome to the population//
				for(i=0;i<pv;i++)
				{
				 if(p==i)
				 {
					for(j=0;j<node;j++)
					npopu[i].pt[j]=pr1[j];
				  }
			 }



		 }
//_______________________________________________part_7_________________________________________________
float check(int pv)
		  {
			int i,j,k ;
			  float y1;

			 for(i=0;i<pv;i++)
				 {       // printf("%f<%f ",popu[i].fitness,fpopu[i].fitness);
					if(popu[i].fitness<fpopu[0].fitness)
					{
					 fpopu[0].fitness=popu[i].fitness;
					 j=i;
					// printf("i=%d  ",i);
					for(k=0;k<node;k++)
					{
					  fpopu[0].pt[k]=popu[j].pt[k];
					 }
					 y1=fpopu[0].fitness ;
				 }


			  }

				// printf("\nfinal fitness=%f\n",fpopu[0].fitness);
			// for(i=0;i<node;i++)
			 // printf("%d\t",fpopu[0].pt[i]);
			 return(y1);
		 }

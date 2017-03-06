'''
Let the universe be [n], the hash-array is of the same size. Create
a fully random hash function h : U → [n]. Hash every element and
calculate the maximum load in any of the buckets. For every choice
of n, choose 100 such hash functions and take the average of the (100)
maximum loads. Make a plot of n versus this maximum load. You
should take n in [10k, 100k] in steps of 1k.

'''

import matplotlib.pyplot as plt
import random
random.seed(231)
start=timeit.default_timer()
def hash(n):
	sum_=0
	for j in range(100):
		H={}
		for i in range(1,n+1):
			H[i]=0

		for i in range(1,n+1):
			H[random.randint(1,n)]+=1
		max_=0
		for i in range(1,n+1):
			max_=max(max_,H[i])
		sum_+=max_
	average=sum_/100.0
	return average
Hp={}
for i in range(10000,100001,1000):
	Hp[i]=hash(i)
lists=sorted(Hp.items())
x,y=zip(*lists)
plt.plot(x,y)
plt.show()



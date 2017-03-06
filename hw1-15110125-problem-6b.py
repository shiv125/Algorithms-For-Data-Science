'''
Fix a size n, create two
such hash functions g and f . For every item x, first calculate load of
the buckets f (x) and g(x) and put x in the one that contains lesser.
If both have same load, break the tie by putting it in the smaller
numbered bucket of the two. Do the same exercise— i.e. for each
n, in [10k, 100k] in steps of 1k, repeat this 100 times and take the
average of the maximum loads.
'''
import matplotlib.pyplot as plt
import random
random.seed(231)
def hash(n):
	sum_=0
	for j in range(100):
		bucket={}
		for i in range(1,n+1):
			bucket[i]=0
		for i in range(1,n+1):
			fx=random.randint(1,n)
			gx=random.randint(1,n)
			if bucket[fx]>bucket[gx]:
				bucket[gx]+=1
			elif bucket[fx]<bucket[gx]:
				bucket[fx]+=1
			else:
				bucket[min(fx,gx)]+=1
		max_=0
		for i in range(1,n+1):
			max_=max(max_,bucket[i])
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

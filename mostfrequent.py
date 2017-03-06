#find a user which appears more than 50% in input stream
#algo pick first user, say it x and suppose it is most frequent, if different users appear
#subtract the counter of the x and proceed if counter becomes 0, then stop and take next user as the most
#frequent one, the last one will be our most frequent user
import random
def most_frequent(users):
	e=users[0]
	count=1
	for i in users:
		if count!=0:
			if (i==e):
				count+=1
			else:
				count-=1
		else:
			e=i
			count=1
	return e

#create random input
n=100#size of input
users=[0]*n
p=107
x=3#most frequent
for i in range(n/2):
	users[i]=3
for i in range(n):
	if users[i]==0:
		users[i]=random.randint(0,n-1)
print users
k=most_frequent(users)
counter=0
for i in range(n):
	if users[i]==3:
		counter+=1
print k
print counter



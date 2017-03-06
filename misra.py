#data stream algorithm, find k most frequent itmes
def misra(stream,k):
	A={}
	for j in stream:
		if j in A:
			A[j]+=1
		elif (len(A)<k):
			A[j]=1
		else:
			for i in A.keys():
				A[i]-=1
				if A[i]==0:
					A.pop(i,None)
	return A
stream=raw_input("Enter stream ")
k=input("Enter how many most frequent items you want=")
t=misra(stream,k)
print t

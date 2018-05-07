def merge(A, p, q, r):
 	L = [0] * (r +1)

 	for i in range(p , q+1):
 		L[i] = A[i]

 	for j in range(q+1 , r+1):
 		L[r+q+1-j] = A[j]

	i = p
	j = r
	k = p  

	for k in range (p, r+1):

		if L[i] <= L[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = L[j]
			j -= 1
 
 
def mergeSort(A,p,r):
    if p < r:
        q = (p+(r-1))/2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)


def selectMedian(A, n):
	mergeSort(A, 0,n-1)
	i = (n) /2
	return (A[i])



A = [10,9,5,3,2,4,1,7,6,8]
print(A)
#mergeSort(A,0,9)
mediana = selectMedian(A, 10)
print (A)
print (mediana)

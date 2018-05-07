import cv2
import math 
import random

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
	i = (n)/2
	return (A[i])

def troca(A,i,j):
	aux = A[i]
	A[i] = A[j]
	A[j] = aux

def particione(A, p, r):
	pivo = A[r]
	i = p-1

	for j in range(p, r):
		if (A[j] <= pivo):
			i+=1
			troca(A,i,j)
	troca(A,i+1, r)
	return (i+1)

def particione_aleatorio(A, p, r):
	j = random.randrange(p,r)
	troca(A, j, r)
	print ("j=", j)
	
	return particione(A, p, r)

def select_NL(A, p, r, i):
	if (p == r):
		return A[p]
	q = particione_aleatorio(A, p,r)
	k = q - p + 1
	if (i == k):
		return A[q]
	elif (i < k):
		return select_NL(A, p, q-1, i)
	else:
		return select_NL(A, q+1, r, i-k)


def readImage (nome):
	imagem = cv2.imread(nome)
	gray_image = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	print "Altura (height): %d pixels" % (gray_image.shape[0])
	print "Largura (width): %d pixels" % (gray_image.shape[1])

	cv2.imshow("IMAGE", gray_image)
	cv2.waitKey(0)
	return gray_image

def filtro_mediana(image, p, q):
	if ( (p<2 or p >= image.shape[0]) or (q<2 or q >= image.shape[1])):
		print ("Tamanho invalido para janela de filtro!")

A = [10,9,5,3,2,4,1,7,6,8]
print(A)
#mergeSort(A,0,9)
#mediana = selectMedian(A, 10)
#mediana = select_NL(A,0,9, math.ceil((10+1)/2.0))
#mediana = select_NL(A,0,9,math.floor((10+1)/2.0))
#print (A)
#print (mediana)

#readImage("tucano.jpeg")
image = readImage("cinza.jpg")
filtro_mediana(image, 300, 120)
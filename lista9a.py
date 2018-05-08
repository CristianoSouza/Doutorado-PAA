import cv2
import math 
import random
import time
import numpy 
import copy

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

	return gray_image

def aplica_janela(imagem, p, q, i, j):
	vetor = [0] * (p*q)
	k = 0
	for r in range( i - (p/2), i + (p/2)):
		for l in range(j - (q/2), j+(q/2)):
			vetor[k] = imagem[r,l]
			k += 1

	print("Vetor: ", vetor)
	#exit()
	#a = selectMedian(vetor, k)
	a = select_NL(vetor, 0, k-1, math.ceil((k+1)/2.0) )
	print(a)
	return a


def filtro_mediana(imagem, p, q):
	#imagem_filtrada = numpy.zeros((imagem.shape[0],imagem.shape[1]), dtype=numpy.float64)
	imagem_filtrada = copy.copy(imagem)
	#print(imagem.channels)
	print(imagem_filtrada)
	#exit()
	if ( (p<2 or p >= imagem.shape[0]) or (q<2 or q >= imagem.shape[1])):
		print ("Tamanho invalido para janela de filtro!")
	else:
		for i in range(0,imagem.shape[0]):
			for j in range(0, imagem.shape[1]):
				print ("M[",i ,",", j, "]= ", imagem[i,j])
				if ( (i - (p/2) >= 0) and (j - (q/2) >= 0) and (i+(p/2) < imagem.shape[0]) and (j+(p/2) < imagem.shape[1]) ):
					#print(imagem)
					#exit()
					#imagem_filtrada[i,j] = imagem[i,j]
					imagem_filtrada[i,j]= aplica_janela(imagem, p, q, i, j)
					print("Imagem original- [i, j]= ", imagem[i,j])
					print("Imagem filtrada- [i, j]= ", imagem_filtrada[i,j])
					#exit()
					#if (p)
				else:
					imagem_filtrada[i,j] = 0
	return imagem_filtrada


#A = [10,9,5,3,2,4,1,7,6,8]
#print(A)
#mergeSort(A,0,9)
#mediana = select_NL(A,0,9, math.ceil((10+1)/2.0))
#mediana = select_NL(A,0,9,math.floor((10+1)/2.0))
#print (A)
#print (mediana)

imagem_global = readImage("tucano.jpeg")
#image = readImage("cinza.jpg")
#image = readImage("camera.jpg")
#cv2.imshow("IMAGE", image)
#cv2.waitKey(0)

ini = time.time()
imagem_filtro = filtro_mediana(imagem_global[:], 10, 10)
print imagem_filtro
fim = time.time()
print "Tempo de execucao: ", fim-ini

cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)
cv2.imshow("Imagem Original", imagem_global)
cv2.waitKey(0)

cv2.namedWindow('Imagem Filtro', cv2.WINDOW_NORMAL)
cv2.imshow("Imagem Filtro", imagem_filtro)
cv2.waitKey(0)

median = cv2.medianBlur(imagem_global,3)

cv2.namedWindow('Imagem Filtro Opencv', cv2.WINDOW_NORMAL)
cv2.imshow("Imagem Filtro Opencv", median)
cv2.waitKey(0)
cv2.destroyAllWindows()


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
	return gray_image

def aplica_janela(imagem, p, q, i, j):
	vetor = [0] * (p*q)
	k = 0
	if ((p % 2) == 0 or (q % 2) == 0):
		for r in range( i - (p/2), i + (p/2) -1):
			for l in range(j - (q/2), j+(q/2) -1):
				vetor[k] = imagem[r,l]
				k += 1	
	else:
		for r in range( i - (p/2), i + (p/2)):
			for l in range(j - (q/2), j+(q/2)):
				vetor[k] = imagem[r,l]
				k += 1
	a = select_NL(vetor, 0, k-1, math.floor((k+1)/2.0) )
	return a


def filtro_mediana(imagem, p, q):
	imagem_filtrada = copy.copy(imagem)
	if ( (p<2 or p >= imagem.shape[0]) or (q<2 or q >= imagem.shape[1])):
		print ("Tamanho invalido para janela de filtro!")
	else:
		for i in range(0,imagem.shape[0]):
			for j in range(0, imagem.shape[1]):
				print ("M[",i ,",", j, "]= ", imagem[i,j])
				if ( (i - (p/2) >= 0) and (j - (q/2) >= 0) and (i+(p/2) < imagem.shape[0]) and (j+(q/2) < imagem.shape[1]) ):
					imagem_filtrada[i,j]= aplica_janela(imagem, p, q, i, j)
				else:
					imagem_filtrada[i,j] = 0
	return imagem_filtrada

#640x480
nome_imagem = "tucano.jpeg"
#nome_imagem = "camera.jpg"
nome_imagem = "futebol.jpg"
imagem_global = readImage(nome_imagem)
tamanho_janela_p = 3
tamanho_janela_q = 3

ini = time.time()
imagem_filtro = filtro_mediana(imagem_global[:], tamanho_janela_p, tamanho_janela_q)
print imagem_filtro
fim = time.time()

file = open("result.txt","w+") 
 
file.write("""IMAGEM: """ + nome_imagem  + """
-- Tamanho da Janela: """+ str(tamanho_janela_p) +""" X """ + str(tamanho_janela_q)+ """
-- Tempo inicial: """+ str(ini) + """
-- Tempo final: """+ str(fim) + """
-- Tempo execucao total: """+ str(fim-ini) + """  
""") 
 
file.close() 

cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)
cv2.imshow("Imagem Original", imagem_global)
cv2.waitKey(0)

cv2.namedWindow('Imagem Filtro', cv2.WINDOW_NORMAL)
cv2.imshow("Imagem Filtro", imagem_filtro)
cv2.waitKey(0)

median = cv2.medianBlur(imagem_global,tamanho_janela_p)

cv2.namedWindow('Imagem Filtro Opencv', cv2.WINDOW_NORMAL)
cv2.imshow("Imagem Filtro Opencv", median)
cv2.waitKey(0)
cv2.destroyAllWindows()


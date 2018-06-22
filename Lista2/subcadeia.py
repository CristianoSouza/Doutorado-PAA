import numpy as n
import Queue as q
import numpy as np

class SubCadeia:

	c = []
	b = []

	def inicialiar_matriz(self, m , n):
		for i in range(0,m+1):
			self.c.append( [0] * (n+1) )
			self.b.append( [' '] * (n+1))		

	def SCM(self, X, m, Y, n):
		self.inicialiar_matriz(m,n)
		for i in range(1,m+1):
			for j in range(1,n+1):
				print(i,j)
				if X[i-1] == Y[j-1]:
					self.c[i][j] = self.c[i-1][j-1] + 1
					self.b[i][j] = "Diagonal"
				else:
					if (self.c[i][j-1] > self.c[i-1][j]):
						self.c[i][j] = self.c[i][j-1]
						self.b[i][j] = "Horizontal"
					else:
						self.c[i][j] = self.c[i-1][j]
						self.b[i][j] = "Vertical"
		return self.c[m-1][n-1], self.b


	def imprimir_matriz_c(self, m, n):
		print (np.matrix(self.c))

	def imprimir_matriz_b(self, m, n):
		print (np.matrix(self.b))

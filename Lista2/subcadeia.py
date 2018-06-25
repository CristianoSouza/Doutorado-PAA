import numpy as n
import Queue as q
import numpy as np

class SubCadeia:

	c = []
	b = []
	subcadeia = []

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
					self.b[i][j] = "D"
				else:
					if (self.c[i][j-1] > self.c[i-1][j]):
						self.c[i][j] = self.c[i][j-1]
						self.b[i][j] = "H"
					else:
						self.c[i][j] = self.c[i-1][j]
						self.b[i][j] = "V"
		return self.c[m][n], self.b

	def imprimir_matriz_c(self, m, n):
		print (np.matrix(self.c))

	def imprimir_matriz_b(self, m, n):
		print (np.matrix(self.b))

	def recupera_SCM(self, X, i, j):
		self.subcadeia = []
		if (i == 1 & j == 1):
			return
		if (self.b[i][j] == "D"): 
			print("D")
			self.recupera_SCM(X, i-1, j-1)
			self.subcadeia.append(X[i-1])
		else:
			if (self.b[i][j] == "V"):
				print("V")
				self.recupera_SCM(X, i-1, j)
			else:
				print("H")
				self.recupera_SCM(X, i, j-1)

	def getSubcadeia(self):
		return self.subcadeia

	def inicialiar_matriz_memoizado(self, m , n):
		for i in range(0,m+1):
			self.c.append( [-1] * (n+1) )
			self.b.append( [' '] * (n+1))

		for i in range(0,m+1):
			self.c[i][0] = 0
		for j in range(1,n+1):
			self.c[0][j]= 0

	def SCM_memoizado(self, X, m, Y, n):
		self.inicialiar_matriz_memoizado(m,n)
		self.imprimir_matriz_c(m,n)
		return self.sub_problem(X, Y, m, n)

	def sub_problem(self, X, Y, i, j):
		if (self.c[i][j] != -1):
			return self.c[i][j]
		else:
			print(i, j)
			if ( i != 0 or j != 0):
				if X[i-1] == Y[j-1]:
					self.c[i][j] = self.sub_problem(X, Y, i-1, j-1) + 1
					self.b[i][j] = "D"
				else:
					c1 = self.c[i][j] = self.sub_problem(X, Y, i, j-1)
					c2 = self.c[i][j] = self.sub_problem(X, Y, i-1, j)
					if (c1 > c2):
						self.c[i][j] = c1
						self.b[i][j] = "H"
					else:
						self.b[i][j] = "V"
						self.c[i][j] = c2
			else:
				self.c[i][j] = 0
		return self.c[i][j]


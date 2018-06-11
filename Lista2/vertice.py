class Vertice():
    def __init__(self, id):
        self.id = id
        self.distancia = 999999
        self.input = 0
        self.output = 0
        self.visitado = False
        self.cor = "BRANCO"
        self.pai = []

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado
    
    def setCor(self, valor):
        self.cor = valor

    def getCor(self):
        return self.cor

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setImput(self, inp):
        self.input = inp

    def setOutput(self, out):
        self.output = out

    def setDistancia(self, distancia):
        self.distancia = distancia

    def getEstimativa(self):
        return self.distancia

    def __str__(self):
        return (" Vertice  : %s \n Estimativa: %i \n Tempo(%i\%i): " % (
            self.id, self.distancia, self.input, self.output))  # imprimir o predecesso

    def __lt__(self, v):
        return self.distancia < v.distancia

    def __eq__(self, v):
        return self.distancia == v.distancia

    def __eq__(self, v):
        return self.id == v.id

    def __gt__(self, v):
        return self.distancia > v.distancia
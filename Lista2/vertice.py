class Vertice():

    _id = 0
    distancia = 0
    _input = 0
    _output = 0
    cor = "BRANCO"
    pai = None

    def __init__(self, id):
        self._id = id
        self.distancia = 999999
        self._input = 0
        self._output = 0
        self.cor = "BRANCO"
        self.pai = []

    def setCor(self, valor):
        self.cor = valor

    def getCor(self):
        return self.cor

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def getPai(self):
        return self.pai
    
    def setPai(self, pai):
        self.pai = pai

    def setImput(self, inp):
        self._input = inp

    def setOutput(self, out):
        self._output = out

    def setDistancia(self, distancia):
        self.distancia = distancia

    def getDistancia(self):
        return self.distancia

    def getEstimativa(self):
        return self.estimativa

    def __str__(self):
        return (" %s  Tempo(%i\%i): " % (
            self._id,self._input, self._output)) 

    def __lt__(self, v):
        return self.distancia < v.distancia

    def __eq__(self, v):
        return self.distancia == v.distancia

    def __eq__(self, v):
        return self._id == v._id

    def __gt__(self, v):
        return self.distancia > v.distancia